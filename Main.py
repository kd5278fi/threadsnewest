import threading
from time import ctime, sleep


def sleepFunction(i):
    print("Thread " + str(i) + " sleeping for 1 second.")
    sleep(1)
    print("Thread " + str(i) + " waking up!\n")

def main():
    threads = []
    for i in range(15):
        t = threading.Thread(target=sleepFunction, args=(i,))
        threads.append(t)

    for i in range(15):
        threads[i].start()

    for i in range(15):
        threads[i].join()

main()