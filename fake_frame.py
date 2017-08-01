
class fake_frame:
    def __init__(self, seq, type, len):
        self.m_seq = seq
        self.m_len = len
        # 0 for key
        # 1 for delta
        self.m_type = type

class frame_generator:
    def __init__(self):
        self.m_next_seq = 0

    def new_frame(self, type, len):
        frame = fake_frame(self.m_next_seq, type, len)
        self.m_next_seq += 1
        return frame
