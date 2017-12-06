import sqlite3
from flask import request, flash
import hashlib

if __name__ == '__main__':
    f = "../data/santa.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    #create user/pwd and history table
    c.execute("CREATE TABLE admin (user TEXT, pass TEXT, PRIMARY KEY(user))")
    c.execute("CREATE TABLE list(code TEXT, name TEXT, likes TEXT)")
    db.commit() #save changes
    db.close()  #close database


# -----FUNCTIONS FOR LOGIN SYSTEM-----
def connect():
    name = "data/santa.db"
    db = sqlite3.connect(name)
    return db

def disconnect(db):
    db.commit()
    db.close()


# returns a dictionary for user data {user: pass}
def getUsers():
    db = connect()
    c = db.cursor()
    a = 'SELECT user, pass FROM admin'
    x = c.execute(a)
    users = {}
    for line in x:
        users[line[0]] = line[1]
    disconnect(db)
    return users
    

# add the login to the database
def addUser(user, password):
    db = connect()
    c = db.cursor()
    hash_object = hashlib.sha224(password)
    hashed_pass = hash_object.hexdigest()
    vals = [user, hashed_pass]
    c.execute("INSERT INTO admin VALUES(?, ?)", vals)
    disconnect(db)

# --------------------------------------------------


#----------------FUNCTIONS FOR USERS----------------
'''
def get_user_history(user):
    db = sqlite3.connect("data/filmadillo.db")
    c = db.cursor()
    x = c.execute("SELECT movie, plot, url FROM history WHERE user= ?", [user])
    movies = []
    for line in x:
        movies.append(line)
    db.close()
    return movies

#add movie into user's list of saved movies 
def add(user, movie, plot, url):
    db = sqlite3.connect("data/filmadillo.db")
    c = db.cursor()
    vals = [user, movie, plot, url]
    #hass the movie already saved?
    if check(user, movie) == True:
        x = c.execute("INSERT INTO history VALUES(?, ?, ?, ?)", vals)
    db.commit()
    db.close()

#looks for this movie where the person who saved it is this user
#to check if the movie has already been saved
def check(user, movie):
    db = sqlite3.connect("data/filmadillo.db")
    c = db.cursor()
    x = c.execute("SELECT movie FROM history WHERE user= ?", [user])
    print x
    for line in x:
        print line
        if movie == line[0]:
            db.close()
            return False
    db.close()
    return True

#remove this movie from the user's list
def remove(user, movie):
    db = sqlite3.connect("data/filmadillo.db")
    c = db.cursor()
    x = c.execute("DELETE FROM history WHERE user= ? AND movie = ?", [user, movie])
    db.commit()
    db.close()

#print "---------\n\n" +  + "\n\n-------------"

'''
