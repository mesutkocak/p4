import itertools
import socket
import threading
import time
from queue import Queue
from urllib.request import urlopen


q = Queue()
file2 = open("domain_name_2.txt", "w")

def get_host_name():

    file = open("domain_name.txt", "w")
    url = urlopen("https://www.usom.gov.tr/url-list.txt ")

    for line in itertools.islice (url, 1, 1000):
        if (line.rstrip().decode("utf-8").replace(".", "").isdigit()):
            print("satır yazılmadı")
        else:
            file.write(line.rstrip().decode("utf-8") + '\n')

get_host_name()

def get_ip(host):

    try:
        host_ip = socket.gethostbyname(host.strip())
        time.sleep(0.2)
        file2.write(host_ip.rstrip() + '\n')
    except:
        print("IP alınamadı")


def threader(q):
    while True:
        worker = q.get()
        get_ip(worker)
        q.task_done()


for x in range(20):
    t = threading.Thread(target=threader, args=(q,))
    t.daemon = True
    t.start()


file1 = open('domain_name.txt', 'r')
Lines = file1.readlines()
for worker in Lines:
    q.put(worker.strip())

q.join()
file2.close()

lines = open('domain_name_2.txt', 'r').readlines()
lines_set = set(lines)
out = open('domain_name_3.txt', 'w')
for line in lines_set:
    out.write(line)


out.close()
