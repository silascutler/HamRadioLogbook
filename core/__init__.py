#!/usr/bin/env python
#######################################################################
# Ham Radio Logbook
#######################################################################
# Copyright (C) 2015 Silas Cutler / KC1BTV <Silas.Cutler@Gmail.com>   #
#######################################################################
# This file is subject to the terms and conditions of the BSD License.#
# See the file LICENSE in the main directory for details              #
#######################################################################

import flask
import functions
import os


# Main server object
class r_server(object):
	def __init__(self):
		self.app = flask.Flask(__name__)	
		self.app.debug = True
		self.static_pages()
		self.db = functions.db_handle()

	# Defines Static pages of the server
	def static_pages(self):
		# Main Index
                @self.app.route('/')
                def main():
			db = functions.db_handle()
			recent = db.list_recent()
			db.shutdown()
                        return flask.render_template('index.html', db_results = recent)

		# Add request
                @self.app.route('/add')
                def pull():
                        if flask.request.args.get('r_stat') and flask.request.args.get('r_band') and flask.request.args.get('r_mode') and flask.request.args.get('r_cnty') and flask.request.args.get('r_freq') and flask.request.args.get('r_note'):
	                        db = functions.db_handle()
				db.log(flask.request.args.get('r_stat'), flask.request.args.get('r_band'), flask.request.args.get('r_mode'), flask.request.args.get('r_cnty'), flask.request.args.get('r_freq'), flask.request.args.get('r_note'))
	                        recent = db.list_recent()

				db.shutdown()
                                return flask.render_template('index.html', db_results = recent,
						alert_vis='', 
						alert_msg='Logged contact to %s' % flask.request.args.get('r_stat'), 
						alert_bnr='Success', 
						type='alert alert-success'
						)

			else:
				return flask.render_template('index.html',
					alert_vis=' ', 
					alert_msg='Not all fields filled out', 
					alert_bnr='Error!', 
					type='alert'
					)

	# Start server
	def start(self):
		self.app.run(host = '127.0.0.1', port = 8080)


				
