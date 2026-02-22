from src.endtoendDS.logger import logging
from src.endtoendDS.exception import CustomException
import sys
from src.endtoendDS.components.data_ingestion import DataIngestion, DataIngestionConfig

from src.endtoendDS.components.data_transformation import DataTransformationConfig, DataTransformation



if __name__ == "__main__":
    logging.info("The Exceution has Started in app.py")

    try:##### for Data ingestion verfiy
        #data_ingestion_config = DataIngestionConfig()
        data_ingestion=DataIngestion()
        #data_ingestion.initiate_data_ingestion() # top 3 is before you write the transormation code when ur connecting it to the db
        train_data_path,test_data_path = data_ingestion.initiate_data_ingestion()

        ##### for Data taransformation verfiy
        #data_transformation_config=DataTransformationConfig()
        data_transformation=DataTransformation()
        data_transformation.initiate_data_transormation(train_data_path,test_data_path)






    except Exception as e:
        logging.info("CustomException occured")
        raise CustomException(e,sys)



