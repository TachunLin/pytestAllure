import inspect
import logging
import os
import datetime


def customLogger(logLevel=logging.INFO):
    # Gets the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    # By default, log all messages
    logger.setLevel(logLevel)

    current_day = (datetime.datetime.now().strftime("%Y_%m_%d_%H_%S"))
    # logPath = ensure_dir(os.path.join("./Log", current_day))

    fileHandler = logging.FileHandler("./Log/" + current_day + ".log", mode='a')
    # fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(formatter)

    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)
    logger.addHandler(consoleHandler)

    return logger

