import logging
import sys
from pythonjsonlogger import jsonlogger

handler = logging.StreamHandler(sys.stdout)
formatter = StackDriverJsonFormatter()
handler.setFormatter(formatter)

root_logger = logging.getLogger()
root_logger.addHandler(handler)

class StackdriverJsonFormatter(jsonlogger.JsonFormatter, object):

    def __init__(self, fmt="%(levelname) %(message)", style='%', *args, **kwargs):
        jsonlogger.JsonFormatter.__init__(self, fmt=fmt, *args, **kwargs)

    def process_log_record(self, log_record):
        log_record['severity'] = log_record['levelname']
        del log_record['levelname']
        return super(StackdriverJsonFormatter, self).process_log_record(log_record)

logging.debug("This is a debug log.")
logging.info("This is an info log.")
logging.warn("This is a warn log.")
logging.error("This is an error log.")
logging.critical("This is a critical log.")
logging.exception("This is an exception log.")
logging.warning("This is a warning log.")

logging.error('{"severity":"WARNING","message":"Testing warning"}')