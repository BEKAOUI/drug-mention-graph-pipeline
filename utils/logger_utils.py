import logging
from config.config import LOG_FILE_PATH


def get_logger(name=__name__):
    # Creates (or retrieves) a logger with a specific name
    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s", 
            datefmt="%Y-%m-%d %H:%M:%S"                    
        )

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)        

        file_handler = logging.FileHandler(LOG_FILE_PATH)
        file_handler.setFormatter(formatter)   
        logger.addHandler(file_handler)          


    return logger

