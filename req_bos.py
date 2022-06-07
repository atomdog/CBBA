#request wrapper for city of boston data
import requests

sources = {"CRIMEINCIDENTREPORTS": "313e56df-6d77-49d2-9c49-ee411f10cf58",
            "SHOOTINGS": "313e56df-6d77-49d2-9c49-ee411f10cf58",
            "SHOTSFIRED": "e16705ca-49ce-4803-84c1-c9848aa63024",
            "FIELDINTERROGATION_2020": "64dd32d9-26f9-4275-9265-97fa3de7e22b",
            "FIELDINTERROGATION_2019": "03f33240-47c1-46f2-87ae-bcdabec092ad",
            "FIELDINTERROGATION_2016": "35f3fb8f-4a01-4242-9758-f664e7ead125",
            "FIREARM_RECOVERY": "a3d2260f-8a41-4e95-9134-d14711b0f954",
            "EARNINGS_2021": "ec5aaf93-1509-4641-9310-28e62e028457",
            "EARNINGS_2020": "e2e2c23a-6fc7-4456-8751-5321d8aa869b",
            "EARNINGS_2019": "3bdfe6dc-3a81-49ce-accc-22161e2f7e74",
            "EARNINGS_2018": "31358fd1-849a-48e0-8285-e813f6efbdf1",
            "CHECKBOOK_2022": "0a261d4e-3eec-4bac-bf72-b9a7aa77b033",
            "CHECKBOOK_2021": "32897eeb-d9ca-494f-93b1-991c50bcd6a6"

            }

#request json -> list of fields w/ types and names
def return_fields(returnedjson):
    return(returnedjson['result']['fields'])


#resource id, int n -> json (results which are the first n)
def n_recent(rid, n):
    r = requests.get("https://data.boston.gov/api/3/action/datastore_search?resource_id="+rid+"&limit="+str(n))
    return(r.json())


#resource id, string n -> json (results which are those which contain n)
def n_contained(rid, n):
    r = requests.get("https://data.boston.gov/api/3/action/datastore_search?resource_id="+rid+"&q="+str(n))
    return(r.json())


#int r (the number of results to return), int n (the starting index) -> json (results which start at n, go to n+r)
def n_skip(rid, r, n):
    r = requests.get("https://data.boston.gov/api/3/action/datastore_search?resource_id="+rid+"$top=",r,"&$skip=",n)
    return(r.json())


rid = sources['EARNINGS_2021']
n = 5
#print(n_recent(rid, n))
print(return_fields(n_recent(rid, n)))



#<------------------------- UNDER CONSTRUCTION ------------------------>

def gen_queries(rid):
    fields = return_fields(n_recent(rid, 1))
    primary_operator = "WHERE"
    secondary_operator = "LIKE"
def request_builder():
    #combine recent, top
    pass
#resource id, query
def n_sql(rid, sel, qry):
    url = 'https://data.boston.gov/api/3/action/datastore_search_sql?sql=SELECT',sel,' from "'+rid+'"'+qry
    pass
