#dbConstruct.py
import numpy as np
import tables
import matplotlib.pyplot as plt
import os
from datetime import datetime
import shutil

#blank log class to create a table with
class consLog(tables.IsDescription):
    #refID          = tables.StringCol(128)
    pass

#constructing a custom database using the fields given to us from req_bos.py
## args: list of of json; type field and id field , and name of file to create,
## the title of the file to create

## example json args (sample source: 'EARNINGS_2021'):
### [{'type': 'int', 'id': '_id'},
### {'type': 'text', 'id': 'NAME'},
### {'type': 'text', 'id': 'DEPARTMENT_NAME'},
### {'type': 'text', 'id': 'TITLE'},
### {'type': 'text', 'id': 'REGULAR'},
### {'type': 'text', 'id': 'RETRO'},
### {'type': 'text', 'id': 'OTHER'},
### {'type': 'text', 'id': 'OVERTIME'},
### {'type': 'text', 'id': 'INJURED'},
### {'type': 'text', 'id': 'DETAIL'},
### {'type': 'text', 'id': 'QUINN_EDUCATION_INCENTIVE'},
### {'type': 'text', 'id': 'TOTAL_GROSS'},
### {'type': 'text', 'id': 'POSTAL'}]

def constructLog(schema, filename):
    logObj = consLog
    constructedColumns = {}
    for x in range(0, len(schema)):
        column_id = schema[x]['id']
        column_type = schema[x]['type']
        if(column_type=='text'):
            logObj.columns[column_id]=tables.StringCol(1024)
        elif(column_type=='int'):
            logObj.columns[column_id]=tables.Float64Col()

    h5file = tables.open_file("data/"+filename+".h5", mode="w", title="constructedlog")
    group = h5file.create_group("/", 'group0', filename+" first group")
    table = h5file.create_table(group, 'table0', logObj, filename+" first table")
    table.flush()
    h5file.close()

#takes a filename, opens the log, and returns the group0 table0
def openLog(filename):
    h5file = tables.open_file(filename, mode="a", title="constructedlog")
    table = h5file.root.group0.table0
    return(h5file, table)

#takes a table, returns a ragged list [[names of each column], length of table (row wise),]
def describeLog(table):
    names = table.coldescrs.keys()
    rowCount = 0
    columnIDs = []
    for name in names:
        columnIDs.append(name)
    for row in table:
        rowCount+=1
    return([columnIDs, rowCount])

def closeLog(h5file, table):
    table.flush()
    h5file.close()
    return(True)

#takes row json: {columnKey: value}
def addRowLog(table, row):
    r = table.row
    for key in row:
        r[key] = row[key]
    r.append()
    return(True)

#takes table, dumps entire table into print
def rowDump(table):
    names = table.coldescrs.keys()
    arr = []
    for row in table:
        q = []
        for name in names:
            c = row[name]
            if(isinstance(c, (bytes, bytearray))):
                q.append(c.decode())
            else:
                q.append(c)
        arr.append(q)
    return(arr)

def snapshot(filename):
    now = datetime.now()
    dt_string = now.strftime("%d:%m:%Y:%H:%M:%S")
    shutil.copy("data/"+filename+".h5", "data/snapshot-"+filename+"-" + dt_string + ".h5")

#snapshot()
#create_empty_logs()
