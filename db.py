#!/usr/bin/python
import psycopg2 
import sys 
import csv
import db_options as eo
import os
import subprocess

query_path = os.getcwd()+'/'
save_path = os.getcwd()+'/'

(options, args) = eo.argsOptions()
if options.edit:
    config_path = os.path.dirname(os.path.realpath(__file__)) + '/db_config.py'
    try: subprocess.call(['vi', config_path])
    except: 
        print('!!! Requires vi to edit default options using this options\n alternately you can open '+config_path+' manually and edit it using an editor of your choice.')
        sys.exit()
    options.info = True 
    print('Editing: '+config_path)

if options.info: 
    #reload(eo)
    eo.printDefaults()
    sys.exit()

#######################################
#### does this only if path is set, which likely will happen only during master.py
if options.path != '':
    save_path = options.path
    query_path = options.path
#########################################
csvfile = save_path + options.save_file
queryfile = query_path + options.psql_query_file
query = options.psql_query
database = options.database
conn_string = eo.getConnection(database)

# If an argument is provided, it is the same as if you specified -q "[sql query]"
# however, only one argument is allowed otherwise it will print an error message
if len(args)==1:
    query = args[0]
if len(args) > 1: 
    print('\nYou have provided more than one argument. \nAt this time only one query (i.e. one argument in quotes) is allowed.\nPlease re-run the command with only one argument\n')
    sys.exit()

if options.psql_query_file is not '':
    if csvfile==save_path+"test.csv":
        csvfile = save_path+options.psql_query_file[:-4]+".csv"
    with open (queryfile,"r") as myfile:
        query = myfile.read()
        print "done reading query from file!!!"

if query[-1]!=';': query = query + ';'
print("\nUsing database: "+database+'\n')
print('Query: '+query+'\n')

conn = psycopg2.connect(conn_string)
cursor = conn.cursor()

cursor.execute(query)
has_output = False

if options.no_output: print('This query has no output.')
else:
    print('If this query has output, it will save to: '+'\n'+csvfile+'\n')
    try:
        records=cursor.fetchall()
        # If title is empty string then don't print header
        if not options.title=='':
            header = [desc[0] for desc in cursor.description]
            header = ','.join(header)
            # if title option given (and not empty) then set to header
            if options.title!='none': header=options.title
            print('Succeeded. Output written with header:')
            print(header)
            with open(csvfile, "w") as output:
                output.write(header+'\n')
        else: print('Succeeded. Title is empty, so header is suppressed \n')
        with open(csvfile, "a") as output:
            writer = csv.writer(output, lineterminator='\n')
            writer.writerows(records)
    except: 
        print('This query has no output.')
    
conn.commit()
cursor.close()
conn.close()
