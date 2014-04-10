ABOUT

These are a compilation of scripts I've written to help me connect to remote postgres-like
databases, run commands and get the results locally. Specifically, these have been designed
for datascience use-cases. You can see possible use-cases in the EXAMPLES section below. 

Please follow the INSTALLATION INSTRUCTIONS to install the scripts on your machine. 
If anything is unclear and you can't install the scripts please let me know. 
Make sure you create a config file to access your specific databases using the 
example given in the INSTALLATION INSTRUCTIONS.


INSTALLATION INSTRUCTIONS

These python scripts require the psycopg2 library to be installed on your machine. 
You will need pip to install psycopg2. If you're on a mac, some of the recent versions 
of pip cannot find psycopg2, in those cases you will need to downgrade. Here are the steps:

On linux: 
$ sudo apt-get install libpq-dev
$ sudo apt-get install python-dev
$ sudo pip install psycopg2

On mac: 
$ easy_install pip==1.2.1 #downgrade pip to version 1.2.1
$ brew install libpqxx
$ pip install psycopg2

How to run on your machine:
I like to add an alias in my bash profile like this:

>> alias db="python /path/to/file/db.py" 

also, if you plan to use my transpose.sh script, then you can add this to bash_profile as well:

>> alias transpose="bash /path/to/file/transpose.sh"

Creating the config file:
$ touch db_config.py

edit the db_config.py file to include your database entries as such:
