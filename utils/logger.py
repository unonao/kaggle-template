import logging
import time
from logging import INFO, FileHandler, StreamHandler
from pathlib import Path


def get_logger(file_name: str, file_dir: Path | str) -> logging.Logger:
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(file_name)
    logger.setLevel(logging.INFO)

    stream_handler = StreamHandler()
    stream_handler.setLevel(INFO)
    logger.addHandler(stream_handler)

    file_name = Path(file_dir) / f"{time.strftime('%Y%m%d_%H%M%S')}.log"
    file_handler = FileHandler(file_name)
    file_handler.setLevel(INFO)
    formatter = logging.Formatter("[%(asctime)s : %(levelname)s - %(filename)s] %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.propagate = False
    return logger
