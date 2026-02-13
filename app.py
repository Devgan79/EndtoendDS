from src.endtoendDS.logger import logging
from src.endtoendDS.exception import CustomException
import sys
from src.endtoendDS.components.data_ingestion import DataIngestion



if __name__ == "__main__":
    logging.info("The Exceution has Started ")

    try:
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()




    except Exception as e:
        logging.info("CustomException occured")
        raise CustomException(e,sys)



