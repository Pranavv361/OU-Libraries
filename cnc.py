import requests,csv, json
from requests import Session
import secretkey
from pprint import pprint as pp

class CNC:
    def __init__(self,token):
        self.apiurl = 'https://api.clarivate.com/apis/wos-starter/v1'
        self.headers = headers = {
                                    'Accepts' :'application/json',
                                    'X-Apikey':token
                                    }
        self.session = Session()
        self.session.headers.update(self.headers)

    def getDocument(self):
        url = self.apiurl+ '/documents'
        query = "PY=2022"  # Web of Science advanced search query
        database = "WOS"  # Web of Science Database abbreviation
        limit = 5  # Limit of records on the page (1-50)
        page = 1  # Result page
        sort_field = "LD+A"  # Order by field(s)
    
        params = {
        "q": query,
        "db": database,
        "limit": limit,
        "page": page,
        "sortField": sort_field
        }
        r = self.session.get(url, params=params)
        print(r.status_code)
        data = r.json()
        return data

cnc = CNC(secretkey.AKEY)
document = cnc.getDocument()
data = pp(document)

# Flatten the JSON structure
def flatten_data(entry):
    flat = {
        "doi": entry["identifiers"].get("doi", ""),
        "issn": entry["identifiers"].get("issn", ""),
        "pmid": entry["identifiers"].get("pmid", ""),
        "title": entry.get("title", ""),
        "authors": "; ".join([author["displayName"] for author in entry["names"]["authors"]]),
        "authorKeywords": "; ".join(entry["keywords"].get("authorKeywords", [])),
        "sourceTitle": entry["source"].get("sourceTitle", ""),
        "volume": entry["source"].get("volume", ""),
        "issue": entry["source"].get("issue", ""),
        "pages": entry["source"]["pages"].get("range", ""),
        "publishMonth": entry["source"].get("publishMonth", ""),
        "publishYear": entry["source"].get("publishYear", ""),
        "recordLink": entry["links"].get("record", ""),
        "referencesLink": entry["links"].get("references", ""),
        "relatedLink": entry["links"].get("related", ""),
        "uid": entry.get("uid", "")
    }
    return flat

# Prepare the CSV file
with open('output.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ["doi", "issn", "pmid", "title", "authors", "authorKeywords", "sourceTitle", "volume", "issue", "pages", "publishMonth", "publishYear", "recordLink", "referencesLink", "relatedLink", "uid"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for entry in document["hits"]:
        writer.writerow(flatten_data(entry))

