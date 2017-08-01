
class fake_packet:
    def __init__(self, frame, seq, len, end = 0):
        self.m_frame = frame
        self.m_end_mark = end
        self.m_seq = seq
        self.m_len = len

class packet_generator:
    def __init__(self):
        self.m_next_seq = 0
    
    def new_packet(self, frame_seq, len, end = 0):
        pkt = fake_packet(frame_seq, self.m_next_seq, len, end)
        self.m_next_seq += 1
        return pkt
