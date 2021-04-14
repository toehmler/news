import datanews

datanews.api_key = '0fraab4bvhzj7f59n3z6hds0f'
test = datanews.headlines(source='dailywire.com', sortBy='date')
hits = test['hits']

print(test)
print(len(hits))
#response = datanews.headlines(q='SpaceX', language=['en'])
#articles = response['hits']
