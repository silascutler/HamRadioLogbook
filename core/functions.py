#!/usr/bin/env python
#######################################################################
# Ham Radio Logbook                                                   #
#######################################################################
# Copyright (C) 2015 Silas Cutler / KC1BTV <Silas.Cutler@Gmail.com>   #
#######################################################################
# This file is subject to the terms and conditions of the BSD License.#
#######################################################################

import sqlite3
import os

# Check to see if file exists and if it does not, print and continue
# IN: 
# OUT: boolean()
def db_pre_check():
	if (os.path.isdir("./db") == False):
		os.mkdir("./db")

	try:
		with open( 'db/logs.db') as handle_db_check:
			return False
	except IOError:
		print " [+] Creating New Database"
		return True

# Class for Database object
# 
class db_handle(object):
	def __init__(self):
		try:
			bool_new_db = db_pre_check()
			self.connection = sqlite3.connect('db/logs.db')
			if (bool_new_db):
				self.db_initialize()	

			self.status = True
		except Exception, e:
			print "Error: %s" % (e)
			self.status = False
	# Create Database schema if db does not exit
	# IN: self
	# OUT: true 
	def db_initialize(self):
		self.connection.execute('''CREATE TABLE contacts(
						timestamp int(20) NOT NULL,
						station varchar(20) NOT NULL,
						band varchar(30) NOT NULL,
						mode varchar(30) NOT NULL,
						country varchar(20),
						frequency varchar(30) NOT NULL,
						notes text NOT NULL
								)''')
		self.connection.commit()
		return True

	# Shutdown Database connection
	# IN: 
	# OUT:
	def shutdown(self):
		self.connection.close()

	# List recent // all previous contacts
	# IN:
	# OUT: array(array(timestamp, station, band, mode, country, frequency, notes))
        def list_recent(self):
                cursor = self.connection.cursor()
                try:
                        cursor.execute("select timestamp, station, band, mode, country, frequency, notes from contacts ORDER BY timestamp DESC") 
                        matches = cursor.fetchall()
			if matches:
	                        return matches
			else:
				return ["", "", "", "", "", "", "" ]

                except Exception, e:
                        print "EXCEPTION : %s " % e
                        return []

	# submit contact
	# IN:  station, band, mode, country, frequency, notes
	# OUT: boolean()
        def log(self, r_stat, r_band, r_mode, r_cnty, r_freq, r_note ):
                cursor = self.connection.cursor()
		query = "INSERT INTO contacts(timestamp, station, band, mode, country, frequency, notes) VALUES ( strftime('%s', 'now'), ?, ?, ?, ?, ?, ? )"
		try:
	                cursor.execute(query, ( r_stat, r_band, r_mode, r_cnty, r_freq, r_note ) )
			self.connection.commit()
                except Exception, e:
                        print "EXCEPTION : %s " % e
                        return False
		return True 

