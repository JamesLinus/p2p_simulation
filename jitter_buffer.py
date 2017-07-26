
from fake_frame import *
from fake_packet import *

class jitter_buffer:
    def __init__(self, size):
        self.m_size = size
        self.m_ts = 0
        self.m_pkt_buf = []
        self.m_frame_buf = []

    def put_pkt(self, pkt):
        pass