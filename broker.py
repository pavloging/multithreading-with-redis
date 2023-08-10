from multiprocessing import Process
from server_telegram import start

def execute_start(message):
    result = start(message)
    print(result)

if __name__ == '__main__':
    message = input('Введите сообщение: ')
    
    # Создаем экземпляр класса Process для каждого потока
    p1 = Process(target=execute_start, args=(message,))
    p2 = Process(target=execute_start, args=(message,))
    p3 = Process(target=execute_start, args=(message,))
    p4 = Process(target=execute_start, args=(message,))
    
    
    # Запускаем выполнение каждого потока
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    
    
    # Ждем, пока каждый поток завершится
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    