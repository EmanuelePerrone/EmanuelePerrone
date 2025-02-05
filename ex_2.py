import threading
import time

def complex_calculation():
    total_sum=sum(range(1, 1000000))
    print (f"Sum= {total_sum}")
    
def show_status():
    while thread_calculation.is_alive():
        print("Calculation in progress...")
        time.sleep(0.5)
            
thread_calculation=threading.Thread(target=complex_calculation)
thread_calculation.start()

thread_status=threading.Thread(target=show_status)
thread_status.start()

thread_calculation.join()
thread_status.join()
