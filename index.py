import os
import sys
path = os.path.dirname(os.path.abspath(__file__))
if path not in sys.path:
    sys.path.insert(1, path)
from appblog import app
from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app)


