import logging
import sys
from pythonjsonlogger import jsonlogger
from datetime import datetime as dt
#import childlogtest

import logging
import sys
from pythonjsonlogger import jsonlogger
from datetime import datetime as dt

class StackdriverJSONFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(StackdriverJSONFormatter, self).add_fields(log_record, record, message_dict)
        if not log_record.get('timestamp'):
            if record.created:
                ts = dt.fromtimestamp(record.created)
            else:
                ts = dt.utcnow()
            ts = ts.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            log_record['timestamp'] = ts

        if log_record.get('level'):
            log_record['severity'] = log_record['level'].upper()
        else:
            log_record['severity'] = record.levelname
            log_record['level'] = record.levelname

        log_record['type'] = "python"
        log_record['app'] = self.app

def setup_stackdriver_logging(app_name, log_level=logging.INFO):
    formatter = StackdriverJSONFormatter('(timestamp) (level) (name) (message)')
    formatter.app = app_name
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
    setup_stackdriver_logging(log_level=0, app_name="Test")
    test = LoggingTest()