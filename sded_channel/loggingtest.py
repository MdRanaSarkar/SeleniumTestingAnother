import logging
logging.basicConfig(filename="D://SeleniumTestCode//sded_channel//test.log",
                    format='%(asctime)s : %(levelname)s : %(message)s',
                    datefmt='%m/%d/%Y  %I:%M:%S %p')

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.debug("This is debug msg")
logger.info("This is for info msg")
logger.warning("This is for warning msg")
logger.error("This is for error msg")
logger.critical("This is for critical msg")

