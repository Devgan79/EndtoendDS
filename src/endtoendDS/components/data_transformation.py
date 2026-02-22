import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from src.endtoendDS.utils import save_object

from src.endtoendDS.exception import CustomException
from src.endtoendDS.logger import logging
import os



@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('Dataset','preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        this function is responsible for data transformation
        '''
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course", #from model notebook
            ]
            num_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy='median')),#This pipline will help to work on new values if they are missing or outliers and other things will me reaplced ny median
                ('scalar', StandardScaler())
#               #This is only for mumerical Features
            ])
            cat_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="most_frequent")),#THis will make a pipleine for missing values to most frequent values that repeat if in future if u get missin  values in cat colomuns
                ("one_hot_encoder", OneHotEncoder()),
                ("scaler", StandardScaler(with_mean=False))
            ])

            logging.info(f"Categorical Columns:{categorical_columns} in data_trafomation.py ") #we are logging them
            logging.info(f"Numerical Columns:{numerical_columns}in data_trafomation.py")

            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, numerical_columns),
                    ("cat_pipeline", cat_pipeline, categorical_columns)
                ]

            )
            return preprocessor


        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transormation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Reading the train and test file returns of Data_ingetion in data_tranformation.py")

            preprocessing_obj = self.get_data_transformer_object()# calling the above fun

            target_column_name = "math_score"
            numerical_columns = ["writing_score", "reading_score"]

            ## divide the train dataset to independent and dependent feature

            input_features_train_df = train_df.drop(columns=[target_column_name])
            target_feature_train_df = train_df[target_column_name]

            ## divide the test dataset to independent and dependent feature

            input_feature_test_df = test_df.drop(columns=[target_column_name])
            target_feature_test_df = test_df[target_column_name]

            logging.info("Applying Preprocessing on training and test dataframe in data_trafomation.py")

            input_feature_train_arr = preprocessing_obj.fit_transform(input_features_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)#data leckage concept

            train_arr = np.c_[#test and train array are concatnated
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object in data_trafomation.py")
            logging.info(f"###### ----- Data Transformation is completed ------######")
            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return (

                train_arr,
                test_arr,
                #self.data_transformation_config.preprocessor_obj_file_path
            )








        except Exception as e:
            raise CustomException(sys, e)