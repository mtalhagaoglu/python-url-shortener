import sqlite3
import time


connection = sqlite3.connect('url_shortener.db',check_same_thread=False)
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS links
             (url TEXT, shortened TEXT, createdAt TEXT, count INT)''')
connection.commit()

def addLink(url,shorten):
    created_at = time.time()
    cursor = connection.cursor()
    if(url.startswith("https://")):
        pass
    elif (url.startswith("http://")):
        url = url.replace("http","https")
    else:
        url = "https://" + url
    cursor.execute('INSERT INTO links values (?,?,?,?)',(url,shorten,created_at,0))
    connection.commit()

def removeLink(shorten):
    cursor = connection.cursor()
    cursor.execute('DELETE from links where shortened = ?',(shorten,))
    connection.commit()

def getLink(shortened):
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM links WHERE shortened=?", (shortened,))
        data = list(cursor.fetchall()[0])
        url,count = data[0],data[3]
        cursor.execute("Update links set count = ? where shortened = ?",(count+1,shortened,))
        connection.commit()
        return url
    except:
        return False

