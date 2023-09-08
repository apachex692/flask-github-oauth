# Author: Sakthi Santhosh
# Created on: 08/09/2023
from secrets import token_hex

class Config:
    SECRET_KEY = token_hex(8)
