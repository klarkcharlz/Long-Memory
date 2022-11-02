import logging


logger = logging.getLogger(f'support_api')
log_level = logging.INFO
log_format = '%(asctime)s %(name)s: %(levelname)s: %(message)s'
formatter = logging.Formatter(log_format)
stderr = logging.StreamHandler()
stderr.setFormatter(formatter)
logger.setLevel(log_level)
logger.handlers = [stderr]
logger.log(log_level, 'log level: %s', logging.getLevelName(log_level))
