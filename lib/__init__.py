# Author: Sakthi Santhosh
# Created on: 08/09/2023
from flask import Flask

from lib.config import Config

app_handle = Flask(__name__)

app_handle.config.from_object(obj=Config)

import lib.routes
