import os
import sys
path = os.path.dirname(os.path.abspath(__file__))
if path not in sys.path:
    sys.path.insert(1, path)
from flask import Flask
app = Flask(__name__)
from appblog import views
