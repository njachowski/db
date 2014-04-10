These python scripts require the psycopg2 library to be installed on your machine. 
You will need pip to install psycopg2. If you're on a mac, some of the recent versions 
of pip cannot find psycopg2, in those cases you will need to downgrade. Here are the steps:

On linux: 


On mac: 

downgrade pip to version 1.2.1
install libpqxx
pip install psycopg2

How to run on your machine:
I like to add an alias in my bash profile like this:

alias db="python /path/to/file/db.py" 
