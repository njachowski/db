#!/usr/bin/env python
from optparse import OptionParser
import db_config

def argsOptions():
	usage = "usage: db [query] [options]" 
	parser = OptionParser(usage=usage)
	parser.add_option("-d", "--db", action="store", dest="database", default=db_config.DEFAULT_DATABASE, help="database to connect to, either rs or pg")
	parser.add_option("-q", "--query", action="store", dest="psql_query", default=None, help="psql query to run")
	parser.add_option("-f", "--file_query", action="store", dest="psql_query_file", default='', help="file containing psql query to run")
	parser.add_option("-s", "--save_location", action="store", dest="save_file", default=db_config.DEFAULT_OUT_FILE, help="location to save file [default=test.csv if -q, <file>.csv if -f]")
	parser.add_option("-p", "--path", action="store", dest="path", default='', help="path to directory to store file (use -s for filename)")
	parser.add_option("-n", "--no_output", action="store_true", dest="no_output",  default=False, help="optional flag to set if query doesn't return anything (e.g. update, drop)")
	parser.add_option("-t", "--title", action="store", dest="title", default="none", help="alternate header rather than using default header derived from query")
	parser.add_option("-a", "--append", action="store_true", dest="append", default=False, help="append to file if exists")
	parser.add_option("-i", "--info", action="store_true", dest="info", default=False, help="get info on current defaults")
	parser.add_option("-e", "--edit-config", action="store_true", dest="edit", default=False, help="edit defaults")

	(options,args) = parser.parse_args()
	return (options,args)

def getConnection(abbreviation):
	if abbreviation == 'rs':
		return db_config.redshift
	if abbreviation == 'pg':
		return db_config.postgres_athena

def printDefaults():
	reload(db_config)
	print('\nDefault database: '+db_config.DEFAULT_DATABASE)
	print('Default out file: '+db_config.DEFAULT_OUT_FILE+'\n')