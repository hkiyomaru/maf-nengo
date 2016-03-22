#!/usr/bin/env python
import sqlite3

conn = sqlite3.connect('nengo.db')

cur = conn.cursor()

cur.execute("""create table mojules (id integer PRIMARY KEY AUTOINCREMENT,name varchar(10) UNIQUE,region varchar(30));""")

cur.execute("""create table connections (id integer PRIMARY KEY AUTOINCREMENT,sourceName varchar(10),destinationName varchar(10),type varchar(4));""")

cur.execute("""create table cortexes (id integer PRIMARY KEY AUTOINCREMENT,sourceRegion varchar(30),destinationRegion varchar(30),type varchar(4), sourceCortex varchar(10), destinationCortex varchar(10));""")

conn.close()
