import redis
import json

print('\nStarting...')

# init
r_send = redis.Redis()
r_res = redis.Redis()
arr = []

mobile = r_send.pubsub()
mobile.subscribe('serverUsers')

for data in mobile.listen():
    data = data['data'] 
    if not isinstance(data, bytes): continue 
    data = json.loads(data.decode('utf-8')) 
    if 'target' not in data: continue 
     
    print('server_users', data)
    
    if not(data['id'] in arr):
        data['message'] = 'Егор Павлов'
        r_send.publish(data['target'], json.dumps(data))