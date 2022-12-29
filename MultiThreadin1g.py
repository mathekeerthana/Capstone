# Threading
'''
import time
start =time.perf_counter()
def calculateTime():
    print("sleep for 5 second")
    time.sleep(5)
    print("completed Sleep")

calculateTime()
calculateTime()
calculateTime()

finish =time.perf_counter()

print(f'Finished in {finish - start} seconds')'''

#
import threading
import time
start =time.perf_counter()
def calculateTime():
    print("sleep for 5 second \n")
    time.sleep(5)
    print("completed Sleep \n")

t1=threading.Thread(target=calculateTime)
t2=threading.Thread(target=calculateTime)
t3=threading.Thread(target=calculateTime)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

finish =time.perf_counter()
print(f'Finished in {finish - start} seconds')

# loops with threading

import threading
import time
start =time.perf_counter()
def calculateTime():
    print("sleep for 5 second")
    time.sleep(5)
    print("completed Sleep")
threads=[]

for _ in range(5):
    thread=threading.Thread(target=calculateTime)
    thread.start()
    threads.append(thread)
print(threads)

for t in threads:
    t.join()

finish =time.perf_counter()
print(f'Finished in {finish - start} seconds')

# loops,arguments with Threading

import threading
import time
start =time.perf_counter()
def calculateTime(seconds):
    print(f'sleep for {seconds} second')
    time.sleep(seconds)
    print(f'completed {seconds} Sleep')
threads=[]

for _ in range(5):
    thread=threading.Thread(target=calculateTime, args=[3])
    thread.start()
    threads.append(thread)
print(threads)

for t in threads:
    t.join()

finish =time.perf_counter()
print(f'Finished in {finish - start} seconds')

# context with Threading
import concurrent.futures
import time
start =time.perf_counter()
def calculateTime(seconds):
    print(f'sleep for {seconds} second')
    time.sleep(seconds)
    #print('completed {seconds} Sleep')
    return f"Completed {seconds} sleep"
with concurrent.futures.ThreadPoolExecutor() as executor:
    list_l=[2,3,4,5,6]
    results=[executor.submit(calculateTime,t) for t in list_l]

    for r in concurrent.futures.as_completed(results):
        print(r.result())
finish =time.perf_counter()
print(f'Finished in {finish - start} seconds')

