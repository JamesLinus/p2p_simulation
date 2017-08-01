
import threading
import random
import Queue
import time
from collections import deque

class packet_sender(threading.Thread):
    def __init__(self, dest, delay_min = 40, delay_max = 300):
        threading.Thread.__init__(self)
        self.m_dest = dest
        self.m_queue = deque()
        self.m_stop = False
        self.m_delay_min = delay_min
        self.m_delay_max = delay_max
    
    def run(self):
        while not self.m_stop:
            delay = random.randint(self.m_delay_min, self.m_delay_max)
            self.send(delay*1000)
            time.sleep(0.001)

    def stop(self):
        self.m_stop = True
    
    def put(self, pkt):
        now = int((time.clock() * 1000000))
        item = {"puttime": now, "value": pkt}
        self.m_queue.append(item)

    def left_puttime(self):
        return self.m_queue[0]["puttime"]

    def send(self, delay):
        if len(self.m_queue) == 0:
            return
        puttime = self.left_puttime()
        now = int((time.clock() * 1000000))
        if puttime + delay < now:
            return
        p = self.m_queue.popleft()
        self.m_dest.put(p)

if __name__ == "__main__":
    q = Queue.Queue()
    sender = packet_sender(q)
    i = 0
    while i < 100:
        time.sleep(1/24)
        sender.put(i)
        i += 1
    # sender.daemon = True
    sender.start()

    i = 0
    while i < 100:
        p = q.get()
        print p
        q.task_done()
        i += 1

    sender.stop()
    sender.join()