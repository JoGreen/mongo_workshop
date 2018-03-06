from mongo.mongo import MongoInstance

test_collection = 'lessons'
db = MongoInstance().getDbInstance()

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

####insert / (implicit)create

db[test_collection].insert(doc)
#write some a code line to insert the second document




####find
db[test_collection].find({})  ##find all docs in the collection
#write a code line to find only RomaTre lessons
#write a code line to find all the lesson Mike Bostock has joined as a partecipant

####remove
#write a code line to remove all docs with type = theory