#!/usr/bin/env python
import csv
import sqlite3

conn = sqlite3.connect('nengo.db')

csvReader = csv.reader(open('seeds/mojules.csv', 'rb'))
header = csvReader.next()
sql = u"insert into mojules values (?, ?, ?)"
for row in csvReader:
    try:
        conn.execute(sql, (None, row[0], row[1]))
    except:
        pass

conn.commit()

csvReader = csv.reader(open('seeds/connections.csv', 'rb'))
header = csvReader.next()

sql = u"insert into connections values (?, ?, ?, ?)"
for row in csvReader:
    try:
        conn.execute(sql, (None, row[0], row[1], row[2]))
    except:
        pass

conn.commit()

csvReader = csv.reader(open('seeds/cortexes.csv', 'rb'))
header = csvReader.next()

sql = u"insert into cortexes values (?, ?, ?, ?, ?, ?)"
for row in csvReader:
    try:
        conn.execute(sql, (None, row[0], row[1], row[2], row[3], row[4]))
    except:
        pass

conn.commit()

conn.close()
