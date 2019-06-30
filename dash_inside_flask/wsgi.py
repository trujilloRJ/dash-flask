# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:08:37 2019

@author: javtruji
"""

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()