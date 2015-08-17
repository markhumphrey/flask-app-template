# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

from app import db

bp = Blueprint(name='root', import_name=__name__, url_prefix='/',
                      static_folder='static', template_folder='templates')

@bp.route('/', methods=['GET'])
def index():
    return render_template(bp.name + "/index.html")
