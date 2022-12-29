import psutil
result01 =psutil.cpu_times()
result02 =psutil.cpu_stats()
result03 =psutil.cpu_freq()
result04 =psutil.disk_partitions()
result05 =psutil.net_io_counters(pernic=True)
#pernic=True :false ::collect the snetio info from all the NIC's together and display the overall result

print(result01)
print("================")
print(result02)
print("================")
print(result03)
print("================")
print(result04)
print("================")
print(result05)
