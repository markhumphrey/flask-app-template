# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

# Import the database object from the main app module
from app import db

# Define the blueprint: 'hello', set its url prefix: app.url/hello
bp = Blueprint(name='root', import_name=__name__, url_prefix='/',
                      static_folder='static', template_folder='templates')

@bp.route('/', methods=['GET'])
def index():
    return render_template(bp.name + "/index.html")
