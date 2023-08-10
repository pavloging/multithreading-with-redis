import redis
import json
import uuid

def start(message_args):
    # init
    # Подключение r_send для отправки сообщения
    # В другой сервис
    r_send = redis.Redis()

    # Подключение r_res для принятия ответа
    # С другого сервиса
    r_res = redis.Redis()

    server = 'serverTelegram'
    arr = []

    # Осуществляем метод публикации и подписки
    mobile = r_send.pubsub()

    # Делаем себя видемым для других серверов
    # И создаем себе имя serverTelegram
    mobile.subscribe(server)

    while True:
        # message = input("Enter the message you want to send to soilders: ")
        message = message_args
        
        id = str(uuid.uuid4())
        data = {
            'message': message,
            'id': id,
            'target': server,
        }
        r_send.publish("serverUsers", json.dumps(data))
        arr.append(data['id'])
        
        for data in mobile.listen():
            data = data['data'] 
            if not isinstance(data, bytes): continue 
            data = json.loads(data.decode('utf-8')) 
            if 'target' not in data: continue 

            print('data', data)
            
            if data['id'] in arr:
                print(data['message'])
                arr.remove(data['id'])
                
                return data['message']
            else:
                data['message'] = 'Егор Павлов'
                r_send.publish(data['target'], json.dumps(data))
        
