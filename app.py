from src.endtoendDS.logger import logging
from src.endtoendDS.exception import CustomException
import sys



if __name__ == "__main__":
    logging.info("The Exceution has Started ")

    try:
        a=1

    except Exception as e:
        logging.info("CustomException occured")
        raise CustomException(e,sys)



