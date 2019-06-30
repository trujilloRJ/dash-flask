# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:04:44 2019

@author: javtruji
"""
from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main import routes

