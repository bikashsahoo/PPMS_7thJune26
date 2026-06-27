# This code only:
#
# 1. Creates the Logs folder.
# 2. Configures logging.
# 3. Creates/gets a logger object.
# 4. Returns the logger object.

import logging
import os


class LogGen:
    @staticmethod
    def loggen():
        # Create Logs folder if it does not exist
        os.makedirs("Logs", exist_ok=True)
        logging.basicConfig(filename=".\\Logs\\automation.log",format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",datefmt="%m/%d/%Y %I:%M:%S %p",level=logging.INFO,force=True)
        logger = logging.getLogger() # want to create a object of logging then from getLogger() u can crt object after that u can access all the functionality of logging module
        logger.setLevel(logging.INFO)
        return logger








    # logging.basicConfig(
    #     filename=".\\Logs\\automation.log",
    #     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    #     datefmt="%m/%d/%Y %I:%M:%S %p",
    #     level=logging.INFO,
    #     force=True
    # )