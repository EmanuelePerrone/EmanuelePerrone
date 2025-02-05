import threading
import time

print_lock=threading.Lock()

def count_up():
    for i  in range(1, 11):
        with print_lock:
            print(f"Thread 1: {i}")
        time.sleep(1)
        
def count_down():
    for i in range(10, 0, -1):
        with print_lock:
            print(f"Thread 2: {i}")
        time.sleep(1)
    
thread1=threading.Thread(target=count_up)
thread2=threading.Thread(target=count_down)
    
thread1.start()
thread1.join()

thread2.start()
thread2.join()