from mongo.mongo import MongoInstance

test_collection = 'lessons'
db = MongoInstance().getDbInstance()

print '\neverything is working. you created the dblp db and the lessons collection.\nnow complete the 2 exercise in the file.\n'

doc = {
    'university': 'Roma Tre',
    'type': 'workshop',
    'topic': 'MongoDB',
    'partecipants':[
        {'name': 'Frank', 'age': 26, 'position': 'student'},
        {'name': 'Mike Bostock', 'age': 46, 'position': 'phD', 'skill': ['java', 'data mining', 'machine learning'] },
        {'name': 'Mina', 'age': 24, 'position': 'student', 'skill': {'java': 8, 'C': 6, 'SQL': 4}}
    ]
}

doc2 = {
    'university': 'TorVergata',
    'type': 'theory',
    'topic': 'Redis',
    'partecipants':[
        {'name': 'Mary Lopiccolo', 'age': 21, 'position': 'student'},
        {'name': 'Mike Bostock', 'age': 46, 'position': 'phD', 'skill': ['java', 'data mining', 'machine learning'] },
        {'name': 'Mina', 'age': 24, 'position': 'student', 'skill': {'java': 8, 'C': 6, 'SQL': 4}}
    ]
}

####insert / (implicit)create database and collection
# if you want to see how connect to the db see the db var on the top of the file and  mongo.py file

db[test_collection].insert(doc)
#write some a code line to insert the second document




####find
results = db[test_collection].find({})  ##find all docs in the collection
#write a code line to find only RomaTre lessons
#write a code line to find all the lesson Mike Bostock has joined as a partecipant

#print the results of your query; results is a mongocursor (similar to python iterator), so you cannot just print the results variable
#use list(results) to load all data in an array
####remove
#write a code line to remove all docs with type = theory