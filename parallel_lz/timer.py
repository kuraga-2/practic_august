
import multiprocessing as mult

def update_counter(counter, lock, result_list):
    for _ in range(1000):
        with lock:
            counter.value += 1 
            result_list.append(counter.value) 

def main():
    lock = mult.Lock() 
    counter = mult.Value('i', 0) 
    manager = mult.Manager() 
    result_list = manager.list() 


    processes = [mult.Process(target=update_counter, args=(counter, lock, result_list)) for _ in range(10)] #список с 10-ю процессами

    for proc in processes:
        proc.start()
    for proc in processes:
        proc.join() 

    print(result_list)

if __name__ == '__main__':
    main()
