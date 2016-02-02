import numpy as np
import pandas as pd
import sqlite3

## Connect to .Analysis File

df = pd.read_csv('raw.csv')

columns_raw = list(df.columns)
columns = [column.split('=')[0] for column in columns_raw]

patientid = columns[4]
columns[4] = 'Reads'
columns[:0] = ['GeneID', 'PatientID']

column_types = [column+' TEXT,' for column in columns]
column_types[0] = column_types[0][:-5]+'INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,'


column_types[3] = column_types[3][:-5]+'INTEGER,'
column_types[8] = column_types[8][:-5]+'NUMBER,'
column_types[9] = column_types[9][:-5]+'NUMBER,'
column_types[10] = column_types[10][:-5]+'NUMBER,'
column_types[26] = column_types[26][:-5]+'NUMBER,'
column_types[27] = column_types[27][:-5]+'NUMBER,'
column_types[39] = column_types[39][:-5]+'NUMBER,'
column_types[41] = column_types[41][:-5]+'NUMBER,'
column_types[42] = column_types[42][:-5]+'NUMBER,'
column_types[43] = column_types[43][:-5]+'NUMBER,'
column_types[44] = column_types[44][:-5]+'NUMBER,'
column_types[45] = column_types[45][:-5]+'NUMBER,'

body = ' '.join(column_types)

body_cleaned = ''
i = 0
for l in body:
    if l == '-':
        i = 1
        continue
    elif l == '.':
        body_cleaned +='__'
    elif l == '#':
        body_cleaned +=''
    elif l == '+':
        body_cleaned +=''
    elif i == 1:
        body_cleaned += l.upper()
        i = 0
    else:
        body_cleaned += l        

body_cleaned = body_cleaned[:-1]
create_command = 'CREATE TABLE IF NOT EXISTS Combined' + '(' + body_cleaned + ')'

columns_withoutid = columns[1:]
columns_joined = ', '.join(columns_withoutid)
columns_joined

headers_cleaned = ''
i = 0
for l in columns_joined:
    if l == '-':
        i = 1
        continue
    elif l == '.':
        headers_cleaned +='__'
    elif l == '#':
        headers_cleaned +=''
    elif l == '+':
        headers_cleaned +=''
    elif i == 1:
        headers_cleaned += l.upper()
        i = 0
    else:
        headers_cleaned += l        

headers_cleaned

## Connect to DB

conn = sqlite3.connect('AnalysisDB.sqlite')
curr = conn.cursor()

curr.execute(create_command)

value = list(df.ix[1])

for i in range(len(df.index)):
    value = list(df.ix[i])
    value[:0] = [patientid]
    value[2] = int(value[2])
    value = tuple(value)
    insert_command = 'INSERT INTO Combined' + '(' + headers_cleaned + ') VALUES(' + '?, '*(len(columns)-2) +'?' +')'
    curr.execute(insert_command, value)

type(value[1])

conn.commit()

conn.close()