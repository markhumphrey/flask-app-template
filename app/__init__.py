from flask import Flask
app = Flask(__name__)

# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.bp_hello.views import bp as bp_hello

# Register blueprint(s)
app.register_blueprint(bp_hello)
# app.register_blueprint(bp_xyz)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()

# need to initialize sqllite in-memory db after app.run()
# https://gehrcke.de/2015/05/in-memory-sqlite-database-and-flask-a-threading-trap/
#@app.before_request
#def before_request():
#    with app.app_context():
        # Extensions like Flask-SQLAlchemy now know what the "current" app
        # is while within this block. Therefore, you can now run........
#       db.create_all()
