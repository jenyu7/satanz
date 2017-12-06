import sqlite3

f = "../data/santa.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#create user/pwd and history table
c.execute("CREATE TABLE admin (user TEXT, pass TEXT, PRIMARY KEY(user))")
c.execute("CREATE TABLE list(code TEXT, name TEXT, likes TEXT)")

db.commit() #save changes
db.close()  #close database
