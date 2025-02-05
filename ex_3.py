import threading

counter = 0
counter_lock = threading.Lock()  

def increment_counter():
    global counter
    for _ in range(1000):
        with counter_lock:  #
            counter += 1

num_threads = 10  
threads = []

for i in range(num_threads):
    thread = threading.Thread(target=increment_counter)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Final value of the counter: {counter}")
