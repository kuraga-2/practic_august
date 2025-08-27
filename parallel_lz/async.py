import threading as thr
import time

def timer(duration):
    time.sleep(duration) 
    print("Задача завершена")

def run(func, args=(), timeout=3): 
    thread = thr.Thread(target=func, args=args) 
    thread.start() 
    thread.join(timeout) 
    if thread.is_alive(): 
        print("Превышено время ожидания")
        thread.join() 

time = int(input("Введите количество секунд - ")) 
run(timer, args=(time,), timeout=3)