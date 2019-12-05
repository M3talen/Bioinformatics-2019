#Needleman-Wunsch algorithm
import time
from enum import Enum

def get_time_of_execution(f):
    """ Decorator to get time of execution """

    def wrapped(*args, **kwargs):
        start_time = time.time()
        res = f(*args, **kwargs)
        print(f'Time elapsed to {f.__name__ } (s): { str(time.time() - start_time)}')
        return res

    return wrapped

class SampleScoring(Enum):
    MATCH = 5,
    MISMATCH = -3,
    GAP = -8
    

class NeedlemanWunsch():
    def __init__(self, seqA, seqB, scoring=SampleScoring):
        self.seqA = seqA
        self.seqB = seqB
        self.m_rows = len(seqA) + 1  # number of rows
        self.m_cols = len(seqB) + 1  # number of columns
        self.matrix = [[[[None] for i in range(2)] for i in range(self.m_cols)] for i in range(self.m_rows)] # Initiating Score Matrix
        self.scoring = scoring
        
    @get_time_of_execution
    def run(self,):
        for i in range(self.m_rows):
            self.matrix[i][0] = [self.scoring.GAP.value *i, []]
        for j in range(self.m_cols):
            self.matrix[0][j] = [self.scoring.GAP.value *j, []]    

nn = NeedlemanWunsch("CCTG", "TCTG")
nn.run()