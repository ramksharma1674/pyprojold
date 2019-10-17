from elasticsearch import Elasticsearch

# Connect to the elastic cluster
es=Elasticsearch([{'host':'localhost','port':9200}])

e1={
    "first_name":"ram",
    "last_name":"sharma",
    "age": 27,
    "about": "Love to play cricket",
    "interests": ['sports','music'],
}

#print(es)
#print(e1)

#Now let's store this document in Elasticsearch 
#res = es.index(index='employee',id=1,body=e1)

e2={
    "first_name" :  "Jane",
    "last_name" :   "Smith",
    "age" :         32,
    "about" :       "I like to collect rock albums",
    "interests":  [ "music" ]
}
e3={
    "first_name" :  "Douglas",
    "last_name" :   "Fir",
    "age" :         35,
    "about":        "I like to build cabinets",
    "interests":  [ "forestry" ]
}

#res=es.index(index='employee',id=2,body=e2)
#print (res)

#res=es.index(index='employee',id=3,body=e3)
#print (res)


res=es.get(index='employee',id=1)
print (res)

print (res['_source'])

#res = es.delete(index='employee', id=2)

#print(res['result'])

res = es.search(index='employee', body={'query': {'match_all': {}}})

print('Took %d seconds to complete the search ' %res['took'])
print('Got %d hits...' %res['hits']['total']['value'])

res  = es.search(index='employee', body={'query': {'match': {'first_name': 'raam'}}})
print(res)


res  = es.search(index='employee', body=
                 {'query': 
                      {'bool' :
                       
                      {'match': {'first_name': 'raam'}}}})
