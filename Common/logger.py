import logging
from Common.path_object import *
class Logger:
    def my_logger(self,msg,level):
        logger=logging.getLogger('Consumer_WEB_TEST')
        logger.setLevel(level)

        formater=logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')
        fh=logging.FileHandler(log_path,encoding='utf-8')
        fh.setLevel(level)
        fh.setFormatter(formater)
        logger.addHandler(fh)

        if level.upper()=='DEBUG':
            logger.info(msg)
        elif level.upper()=='INFO':
            logger.info(msg)
        elif level.upper()=='WARNING':
            logger.warning(msg)
        elif level.upper()=='ERROR':
            logger.error(msg)
        elif level.upper()=='CRITICAL':
            logger.critical(msg)
        logger.removeHandler(fh)
    def logger_debug(self,msg):
        self.my_logger(msg,'DEBUG')
    def logger_info(self,msg):
        self.my_logger(msg,'INFO')
    def logger_warning(self,msg):
        self.my_logger(msg,'WARNING')
    def logger_error(self,msg):
        self.my_logger(msg,'ERROR')
    def logger_critical(self,msg):
        self.my_logger(msg,'CRITICAL')
if __name__ == '__main__':
    logging.getLogger('SMB_WEB_TEST')