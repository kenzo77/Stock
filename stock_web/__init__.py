from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object('stock_web.config')
db = SQLAlchemy(app)

import stock_web.views
import stock_web.control.search_company
import stock_web.control.company_info
