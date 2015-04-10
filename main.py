#!/usr/bin/env python
#######################################################################
# Ham Radio Logbook                                                   #
#######################################################################
# Copyright (C) 2015 Silas Cutler / KC1BTV <Silas.Cutler@Gmail.com>   #
#######################################################################
# This file is subject to the terms and conditions of the BSD License.#
#######################################################################

from core import r_server

def main():
	server = r_server()
	server.start()

if __name__ == "__main__":
	main()




