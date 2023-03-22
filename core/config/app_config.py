import os

from addict import Dict
from dotenv import load_dotenv

load_dotenv()

BASE_URL = 'https://www.saucedemo.com'
USER = Dict(username='standard_user', password=os.environ.get('PASSWORD'))
