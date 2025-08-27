
import threading as thr
import time

counter = 0
lock = thr.Lock()

def increment_counter(thread_id):
    global counter
    start_time = time.time()  
    with lock:
        counter += 1000
    end_time = time.time() 
    final_time = end_time - start_time  
    print(f"Поток {thread_id} увеличил счётчик на 1000. Время выполнения: {final_time:} сек")

threads = []  
 
for i in range(1, 11):
    thread = thr.Thread(target=increment_counter, args=(i,))
    threads.append(thread)
    thread.start()
    time.sleep(0.1) 


for thread in threads:
    thread.join()

print(f"Конечное значение счётчика: {counter}")


simple_counter = 0
start_time = time.time()
for _ in range(10):
    simple_counter += 1000
end_time = time.time()

simple_time = end_time - start_time
print(f"Обычный счётчик: Конечное значение: {simple_counter}, Время выполнения: {simple_time:} сек")
