import os
from dotenv import load_dotenv

BASEDIR = os.path.abspath(os.path.dirname(__file__))
print("----------------- BASE DIR ----------------")
print(BASEDIR)

load_dotenv(os.path.join(BASEDIR, ".env"))


class Config(object):
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    AUTHORITY = os.environ.get('AUTHORITY')
    CLIENT_ID = os.environ.get('CLIENT_ID')
    REDIRECT_PATH = os.environ.get('REDIRECT_PATH')
    SCOPE = [os.environ.get('SCOPE')]
    SESSION_TYPE = os.environ.get('SESSION_TYPE')
