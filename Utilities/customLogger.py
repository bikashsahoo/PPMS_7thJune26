import logging
import os


class LogGen:
    @staticmethod
    def loggen():
        # Create Logs folder if it does not exist
        os.makedirs("Logs", exist_ok=True)

        logging.basicConfig(
            filename=".\\Logs\\automation.log",
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%m/%d/%Y %I:%M:%S %p",
            level=logging.INFO,
            force=True
        )

        logger = logging.getLogger()
        return logger