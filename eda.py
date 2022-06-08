#eda.py

import req_bos
import dbConstruct

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
n = 500
print("==== Requesting ", str(n), "entries from ", rid, " ====")
re = req_bos.eat_result(req_bos.n_recent(rid, n))
for x in range(0, len(re)):
    dbConstruct.addRowLog(table, re[x])

dumpedtable = dbConstruct.rowDump(table)
for x in range(0, len(dumpedtable)):
    print(dumpedtable[x])
    print('\n')
print("==== Closing table ====")
dbConstruct.closeLog(ofile, table)
