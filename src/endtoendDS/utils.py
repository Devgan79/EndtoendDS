import os
import pymysql
from dotenv import load_dotenv
import pandas as pd
from src.endtoendDS.exception import CustomException
from src.endtoendDS.logger import logging




load_dotenv()
host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")


  ## this is to read from mysql

def read_sql_data():
    logging.info("Reading SQL Data in utils.py file ")
    try:
        mydb=pymysql.connect(host=host,user=user,password=password,db=db)
        logging.info("Connected to MySQL DB sussefully")
        df=pd.read_sql_query("select * from student", mydb)
        print(df)
        return df

    except Exception as e:
        raise CustomException(e,sys)