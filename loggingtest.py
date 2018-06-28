import logging
import sys
from pythonjsonlogger import jsonlogger
#import childlogtest

class StackdriverJSONFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(StackdriverJSONFormatter, self).add_fields(log_record, record, message_dict)
        if not log_record.get('time'):
            # this doesn't use record.created, so it is slightly off
            #now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            #log_record['timestamp'] = now
            log_record['time'] = record.created
        if log_record.get('level'):
            log_record['severity'] = log_record['level'].upper()
        else:
            log_record['severity'] = record.levelname
        del log_record['level']

def setup_stackdriver_logging(log_level=logging.INFO):
    formatter = StackdriverJSONFormatter('(time) (level) (name) (message)')
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    root_logger = logging.getLogger()
    root_logger.addHandler(handler)
    root_logger.setLevel(log_level)

class LoggingTest():

    def __init__(self):
        logger = logging.getLogger(__name__)
        logger.debug("This is a debug log.")
        logger.info("This is an info log.")
        logger.warn("This is a warn log.")
        logger.error("This is an error log.")
        logger.critical("This is a critical log.")
        logger.exception("This is an exception log.")
        logger.warning("This is a warning log.")

  #  def subtest():
  #      childlogtest.run()

if __name__ == '__main__':
    setup_stackdriver_logging()
    test = LoggingTest()