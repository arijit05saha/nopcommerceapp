import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('base page details', 'baseURL')
        return url

    @staticmethod
    def getUserEmail():
        username = config.get('base page details', 'useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('base page details', 'password')
        return password