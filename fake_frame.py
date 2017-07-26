
class fake_frame:
    def __init__(self):
        self.m_seq = 0
        self.m_len = 0
        # 0 for key
        # 1 for delta
        self.m_type = 0

class frame_generator:
    def __init__(self):
        self.m_next_seq = 0

    def new_frame(self, type, len):
        frame = fake_frame()
        frame.m_len = len
        frame.m_type = type
        frame.m_seq = self.m_next_seq
        self.m_next_seq += 1
        return frame
