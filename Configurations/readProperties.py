import os
import configparser

config = configparser.RawConfigParser()

config_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "Configurations",
    "config.ini"
)

config.read(config_path)

class readProperties():
    @staticmethod
    def getURL():
        url = config.get("common info", "base_url")
        return url

    @staticmethod
    def getUsername():
        username = config.get("common info", "username")
        return username

    @staticmethod
    def getPassword():
        password = config.get("common info", "password")
        return password

    @staticmethod
    def getOTP():
        otp = config.get("common info", "otp")
        return otp