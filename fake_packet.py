
class fake_packet:
    def __init__(self):
        self.m_seq = 0
        self.m_len = 0

class packet_generator:
    def __init__(self):
        self.m_next_seq = 0
    
    def new_packet(self, len):
        pkt = fake_packet()
        pkt.m_len = len
        pkt.m_seq = self.m_next_seq
        self.m_next_seq += 1
        return pkt
