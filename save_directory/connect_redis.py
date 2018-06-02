from redis import StrictRedis


redis = StrictRedis(host='localhost', port=6379, db=0, password='000000')
redis.set('name', 'Lockin')
print(redis.get('name'))
