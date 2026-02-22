import os
import pymysql
from dotenv import load_dotenv
import pandas as pd
from src.endtoendDS.exception import CustomException
from src.endtoendDS.logger import logging

import pickle
import numpy as np



load_dotenv()
host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")


  ## this is to read from mysql

def read_sql_data():
    logging.info("Trying to  Establish DB connection in utils.py")
    try:
        mydb=pymysql.connect(host=host,user=user,password=password,db=db)
        df=pd.read_sql_query("select * from student", mydb)
        print(df)
        logging.info(" Connection is Established sucesfully the DB is printed in utils.py ")
        return df

    except Exception as e:
        raise CustomException(e,sys)

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)