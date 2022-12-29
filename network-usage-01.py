import psutil
import time
UPDATE_DELAY = 1 # in seconds
def get_size(bytes):
    """
    Returns size of bytes in a nice format
    """
    for unit in ['','K','M','G','T','P']:
        if bytes<1024:
            return f"{bytes:.2f} {unit}B"
        bytes /=1024
        io=psutil.net_io_counters()
        bytes_sent, bytes_recv =io.bytes_sent,io.bytes_recv
while True:
    time.sleep(UPDATE_DELAY)
    io_2 = psutil.net_io_counters()
    # new - old stats gets us the speed
    us,ds, =io_2.bytes_sent, io_2.bytes_recv
    # print the total doenload/upload along with current speeds
    print(f"Upload: {get_size(io_2.bytes_sent)} "
    f",Download: {get_size(io_2.bytes_recv)} "
    f",Upload Speed: {get_size(us / UPDATE_DELAY)} /s"
    f",Download Speed: {get_size(ds / UPDATE_DELAY)} /s",end="\r")
    # update the bytes_sent and bytes_recv for next iteration
    bytes_sent, bytes_recv = io_2.bytes_sent,io_2.bytes_recv