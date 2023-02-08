# app.py

# import sys
# # Adds higher directory to python modules path. No need to use .. when trying import modules from "below"
# sys.path.append("..")

from werkzeug.middleware.dispatcher import (
    DispatcherMiddleware,
)  # use to combine each Flask app into a larger one that is dispatched based on prefix

from index import app as index
from I.boilerplate.main import app as boilerplate
from I.input_url.main import app as input_url
from I.keliamieji.main import app as keliamieji
from I.arkeliamieji.main import app as arkeliamieji
from I.biudzetas.main import app as biudzetas

from II.main import app as blog

application = DispatcherMiddleware(
    index,
    {
        "/boilerplate": boilerplate,
        "/input_url": input_url,
        "/keliamieji": keliamieji,
        "/arkeliamieji": arkeliamieji,
        "/biudzetas": biudzetas,
        "/blog": blog,
    },
)
