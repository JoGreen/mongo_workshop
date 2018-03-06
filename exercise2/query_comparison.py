import time
from mysql import mysql
from mongo.mongo import MongoInstance


#query sql join
query_with_join = "SELECT p.paper_key, p.title, p.citations, c.conf_key, c.year, c.publisher, c.link, k.keyword FROM " \
        "papers p, keywords k, conferences c  " \
        "WHERE p.paper_key= k.paper_key and p.conf_key = c.conf_key"

t0 = time.time()
mysql_res = mysql.send_query(query_with_join)
print time.time() - t0, 'first query (sql)'

###same query with mongo
t0 = time.time()
mongo_res = MongoInstance().getDbInstance()['papers_workshop'].find({})
#list(mongo_res)
print time.time() - t0, 'first query (mongo)'

print

query_no_join = 'SELECT p.paper_key FROM papers p WHERE p.citations > 3'

t0 = time.time()
mysql_res = mysql.send_query(query_no_join)
list(mysql_res)
print time.time() - t0, 'second query (sql)'

#write the find condtion
t0 = time.time()
mongo_res = MongoInstance().getDbInstance()['papers_workshop'].find({} ) #add condition
#list(mongo_res)
print time.time() - t0, 'second query (mongo)'

print

#alternative query
t0 = time.time()
q1 = 'SELECT k.paper_key FROM keywords k WHERE k.keyword = "3g mobile communication" '
mysql_res = mysql.send_query(q1)
#list(mysql_res)
print time.time() - t0, 'third query (sql)'

t0 = time.time()
mongo_res = MongoInstance().getDbInstance()['papers_workshop'].find({
    'keywords':{'$in':['']}},{'paper_key':1, '_id':0} )  # modify condition
#list(mongo_res)
print time.time() - t0, 'third query (mongo)'


print

q2 = 'SELECT count(distinct(k.paper_key)) FROM dblp.keywords k '
t0 = time.time()
mysql_res = mysql.send_query(q2)
#list(mysql_res)
print time.time() - t0, 'fourth query (sql)'


t0 = time.time()
mongo_res = MongoInstance().getDbInstance()['papers_workshop'].distinct('paper_key')
#print len(mongo_res) # that's not a cursor
#list(mongo_res)
print time.time() - t0, 'fourth query (mongo)'
t0 = time.time()

print

q3 = 'SELECT count(distinct(k.conf_key)) FROM dblp.papers k '
t0 = time.time()
mysql_res = mysql.send_query(q3)
#list(mysql_res)
print time.time() - t0, 'fifth query (sql)'


t0 = time.time()
mongo_res = MongoInstance().getDbInstance()['papers_workshop'].distinct('') #modify condition
#print len(mongo_res) # that's not a cursor
#list(mongo_res)
print time.time() - t0, 'fifth query (mongo)'
t0 = time.time()