import google.cloud.logging
import logging

client = google.cloud.logging.Client()
#handler = client.get_default_handler()
client.setup_logging(log_level=logging.INFO)

logging.debug("This is a debug log.")
logging.info("This is an info log.")
logging.warn("This is a warn log.")
logging.error("This is an error log.")
logging.critical("This is a critical log.")
logging.exception("This is an exception log.")
logging.warning("This is a warning log.")