#from mysql import load some tables and save dat on mongodb
from mongo.mongo import MongoInstance
from mysql import mysql
import time
from tqdm import tqdm


def make_unicode(input):
    input = "%r"%input
    input2 =  input.replace('\\','').replace('\'', '')
    return input2





migration_collection = 'papers_workshop'
db = MongoInstance().getDbInstance()
#hint -> use insert_many instead of insert
sql_query = "SELECT p.paper_key, p.title, p.citations, c.conf_key, c.year, c.publisher, c.link, k.keyword FROM papers p, keywords k, conferences c  WHERE p.paper_key= k.paper_key and p.conf_key = c.conf_key ORDER BY p.paper_key"
res = mysql.send_query(sql_query)
doc = {'paper_key': 'test'}
docs = []
t_start = time.time()
for row in tqdm(res):
    if doc != None and doc["paper_key"] != row[0]:
        if(doc['paper_key'] != 'test'):
            docs.append(doc)
        doc = {'keywords': [] }
        doc["paper_key"] = row[0]
        doc['title'] = make_unicode(row[1])
        doc['citations'] = int(row[2])
        doc['conference'] = {}
        doc['conference']['conf_key'] = row[3]
        doc['conference']['year'] = int(row[4])
        doc['conference']['publisher'] = row[5]
        doc['conference']['link'] = row[6]


    doc['keywords'].append(make_unicode(row[7] ) )



##change step value to see different time logs in your console -> max value 5000 for this example
    step  = 5
############################
    if len(docs) > step:
        t0 = time.time()
        print db[migration_collection].insert_many(docs)
        print 'step time:', time.time() - t0
        docs = []

t0 = time.time()
##insert
print db[migration_collection].insert_many(docs)
#########
print 'step time:', time.time() - t0
print 'end in ', time.time() - t_start


