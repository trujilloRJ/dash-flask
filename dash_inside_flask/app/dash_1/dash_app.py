# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 17:56:15 2019

@author: javtruji
"""

from dash import Dash
import dash_core_components as dcc
import dash_html_components as html

url_dash = '/dash/'

def Add_Dash(server):
    """Create Dash app."""
    external_stylesheets = ['/static/css/bootstrap.min.css']
                    
    dash_app = Dash(server=server,
                    external_stylesheets=external_stylesheets,
                    url_base_pathname=url_dash)
    
    dash_app.index_string = '''<!DOCTYPE html>
        <html>
            <head>
                {%metas%}
                <title>{%title%}</title>
                {%favicon%}
                {%css%}
            </head>
            <body>
                <div class='container-fluid'>
			<nav class="navbar navbar-expand-lg navbar-light bg-light">
				<a class="navbar-brand" href="/index">
					<img src="/static/images/report.svg" width="30" height="30" class="d-inline-block align-top" alt="">
					Dash-Flask
				</a>
				<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
					<span class="navbar-toggler-icon"></span>
				</button>
				<div class="collapse navbar-collapse" id="navbarNav">
					<ul class="nav navbar-nav ml-auto">
						<li class='nav-item'><a class="nav-link" href="/login">
							Logout
						</a></li>
					</ul>
				</div>
				<hr>
			</nav>
                {%app_entry%}
                <footer>
                    {%config%}
                    {%scripts%}
                    {%renderer%}
                </footer>
            </body>
        </html>'''

    # Create Dash Layout
    layout = html.Div(id='dash-container',
                      children=[
                          'Hello Flask I Dash'        
                      ],className='container')

    dash_app.layout = layout

    return dash_app.server

#def init_callbacks(dash_app):
#    @app.callback(
#        # ... Callback input/output
#        )
#    def update_graph():
#        # ... Insert callback stuff here