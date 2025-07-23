import time
import logging
from datetime import datetime

logging.basicConfig(
    filename="monitoring.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def monitor(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            duration = time.time() - start_time
            logging.info(f"Function '{func.__name__}' executed successfully in {duration:.4f} seconds.")
            return result
        except Exception as e:
            duration = time.time() - start_time
            logging.error(f"Function '{func.__name__}' failed after {duration:.4f} seconds. Error: {e}")
            raise
    return wrapper
