""" config.py for manage configuration variables for the process in different environments """
""" change for your token and rename the file to config.py """

class Config():
    TOKEN = "YOUR_TOKEN_HERE"
    URL_BASE = "https://api.codenation.dev/v1/challenge/dev-ps/"
    FILE_PATH = "./data/answer.json" 
    GET_EXT = "generate-data"
    POST_EXT = "submit-solution"