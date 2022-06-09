#eda.py

import req_bos
import dbConstruct
import matplotlib.pyplot as plt
import numpy as np
import graphUtil
import random
def getNewEx():
    sourcenames = req_bos.list_sources()
    print("==== Available sources: ====")
    for x in range(0, len(sourcenames)):
        print(sourcenames[x])
    rid = req_bos.sourcetorid("EARNINGS_2021")
    rid_fields = req_bos.return_fields(req_bos.n_recent(rid, 1))
    print("==== ", rid, " fields: ====")
    for x in range(0, len(rid_fields)):
        print(rid_fields[x])
    dbConstruct.constructLog(rid_fields, "EARNINGS_2021")
    ofile, table = dbConstruct.openLog('data/EARNINGS_2021.h5')
    log_desc = dbConstruct.describeLog(table)
    print("==== Created a table with the following columns: ====")
    for x in range(0, len(log_desc[0])):
        print(log_desc[0][x])
    print("==== Table is ", str(log_desc[1]), " rows long ====")
    n = 5000
    print("==== Requesting ", str(n), "entries from ", rid, " ====")
    re = req_bos.eat_result(req_bos.n_recent(rid, n))
    for x in range(0, len(re)):
        dbConstruct.addRowLog(table, re[x])

    dumpedtable = dbConstruct.rowDump(table)
    for x in range(0, len(dumpedtable)):
        print(dumpedtable[x])
        print('\n')


    for x in range(0, len(log_desc[0])):
        print(log_desc[0][x])
    log_desc = dbConstruct.describeLog(table)
    print("==== Table is ", str(log_desc[1]), " rows long ====")
    print("==== Closing table ====")
    dbConstruct.closeLog(ofile, table)

def graphOldEx():
    ofile, table = dbConstruct.openLog('data/EARNINGS_2021.h5')
    log_desc = dbConstruct.describeLog(table)
    dumpedtable = dbConstruct.rowDump(table)
    print("==== Created a table with the following columns: ====")
    for x in range(0, len(log_desc[0])):
        print(log_desc[0][x])
    color_gen = []

    gross = []
    departments = []
    dumpedtable = random.sample(dumpedtable, 100)
    for x in range(0, len(dumpedtable)):
        p_dept = dumpedtable[x][0]
        p_gross = (dumpedtable[x][len(dumpedtable[x])-2])
        p_gross = p_gross.replace(",","")
        if(p_gross == "None"):
            p_gross = 0
        p_gross = float(p_gross)
        gross.append(p_gross)
        departments.append(p_dept)

    d_set = set(departments)
    uniquedepartments = len(d_set)
    c = graphUtil.colormap(uniquedepartments)
    d_set=list(d_set)
    gross = np.array(gross)
    legendd = {}
    for iterat in range(0, len(d_set)):
        legendd[d_set[iterat]] = c[iterat]
    cd = []
    for x in range(0, len(departments)):

        cd.append(legendd[departments[x]])
    plt.rcParams.update({'font.size': 5})
    fig, ax = plt.subplots()
    xaxis = [x for x in range(len(gross))]
    for x in range(0, len(xaxis)):
        xaxis[x]=xaxis[x]*xaxis[x]
    ax.scatter(xaxis, gross, color = cd)
    for q in range(0, len(xaxis)):

          plt.annotate(departments[q], (xaxis[q], gross[q] + 0.2))
          pass

    ax.ticklabel_format(useOffset=False,style='plain')
    ax.legend()

    plt.show()

graphOldEx()
