#!/usr/bin/env python
from optparse import OptionParser
from db_config import *

def argsOptions():
	usage = "usage: db [query] [options]  ### check/set query_path and save_path when running in a new system"
	parser = OptionParser(usage=usage)
	parser.add_option("-d", "--db", action="store", dest="database", default=DEFAULT_DATABASE, help="database to connect to, either rs or pg")
	parser.add_option("-q", "--query", action="store", dest="psql_query", default=None, help="psql query to run")
	parser.add_option("-f", "--file_query", action="store", dest="psql_query_file", default='', help="file containing psql query to run")
	parser.add_option("-s", "--save_location", action="store", dest="save_file", default=DEFAULT_OUT_FILE, help="location to save file [default=test.csv if -q, <file>.csv if -f]")
	parser.add_option("-p", "--path", action="store", dest="path", default='', help="path to directory to store file (use -s for filename)")
	parser.add_option("-n", "--no_output", action="store_true", dest="no_output",  default=False, help="optional flag to set if query doesn't return anything (e.g. update, drop)")
	parser.add_option("-r", "--raw", action="store_true", dest="raw", default=False, help="raw without header")
	parser.add_option("-t", "--title", action="store", dest="title", default="none", help="alternate header rather than using default header derived from query")
	parser.add_option("-a", "--append", action="store_true", dest="append", default=False, help="append to file if exists")

	(options,args) = parser.parse_args()
	return (options,args)

def getConnection(abbreviation):
	if abbreviation == 'rs':
		return redshift
	if abbreviation == 'pg':
		return postgres_athena
