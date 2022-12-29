import os
import time
import win32api
start =time.perf_counter()
def find_files(filename,search_path):
    result=[]
    # walking top-down from root
    for root,dir,files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root,filename))
    return result
for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
    print(find_files("sample.txt",drive))
finish=time.perf_counter()
print(f"time{finish-start} seconds")
