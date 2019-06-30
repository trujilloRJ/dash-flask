# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 15:52:51 2019

@author: javtruji
"""

from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required

bootstrap = Bootstrap()
db = SQLAlchemy()
login = LoginManager()
login.login_view = 'auth.login'

def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config_class)
    
    with app.app_context():
        from app.main import bp as main_bp
        from app.auth import bp as auth_bp
        
        # importing blueprints
        app.register_blueprint(main_bp, url_prefix='/')
        app.register_blueprint(auth_bp, url_prefix='/')
        
        # importing dash app
        from app.dash_1 import dash_app
        app = dash_app.Add_Dash(app)
        
        # binding login to dash
        url_dash = dash_app.url_dash
        for view_func in app.view_functions:
            if view_func.startswith(url_dash):
                app.view_functions[view_func] = login_required(app.view_functions[view_func])
        

    bootstrap.init_app(app)
    db.init_app(app)
    login.init_app(app)
    
    return app

