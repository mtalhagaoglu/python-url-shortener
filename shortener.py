import sqlite3
import time
import ast
from datetime import datetime

connection = sqlite3.connect('url_shortener.db',check_same_thread=False)
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS links
             (url TEXT, shortened TEXT, createdAt TEXT, count INT,visitors TEXT)''')
connection.commit()


def isValidIp(ip,hash):
    cursor = connection.cursor()
    ip = str(ip)
    try:
        cursor.execute("SELECT * FROM links WHERE shortened=?", (hash,))
        data = list(cursor.fetchall()[0])
        visitors = ast.literal_eval(data[4])
        if ip in visitors.keys():
            return False
        else:
            now = datetime.now()
            date = now.strftime("%d/%m/%Y %H:%M:%S")
            visitors[ip] = {"date": date}
            visitors = str(visitors)
            cursor.execute("Update links set visitors = ? where shortened = ?", (visitors, hash,))
            return True
    except:
        return True

def addLink(url,shorten):
    created_at = time.time()
    cursor = connection.cursor()
    if(url.startswith("https://")):
        pass
    elif (url.startswith("http://")):
        url = url.replace("http","https")
    else:
        url = "https://" + url
    cursor.execute('INSERT INTO links values (?,?,?,?,?)',(url,shorten,created_at,0,'{}'))
    connection.commit()

def removeLink(shorten):
    cursor = connection.cursor()
    cursor.execute('DELETE from links where shortened = ?',(shorten,))
    connection.commit()

def getLink(shortened,ip):
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM links WHERE shortened=?", (shortened,))
        data = list(cursor.fetchall()[0])
        url,count = data[0],data[3]
        isValid = isValidIp(ip, shortened)
        if isValid:
            cursor.execute("Update links set count = ? where shortened = ?",(count+1,shortened,))
            connection.commit()
        return url
    except:
        return False

def getCount(shortened):
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT count FROM links WHERE shortened=?", (shortened,))
        data = list(cursor.fetchall()[0])[0]
        return str(data)
    except:
        return 0
