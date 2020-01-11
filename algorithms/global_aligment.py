# Needleman-Wunsch algorithm
import time
from enum import Enum
from pandas import *

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
    GAP = -5

class NeedlemanWunsch():
    def __init__(self, scoring=[5,-3,-5]):
        self.scoring = scoring


    def run(self, seqA, seqB,):
        self.seqA = seqA
        self.seqB = seqB
        self.m_rows = len(seqA) + 1
        self.m_cols = len(seqB) + 1
        
        self.matrix = [[None for i in range(self.m_cols)] for i in range(self.m_rows)] # Initiating Score Matrix
        
        self.aln_pathways = []
        
        for i in range(self.m_rows):
            self.matrix[i][0] = self.scoring[2] * i
        for j in range(self.m_cols):
            self.matrix[0][j] = self.scoring[2] * j

        [self.score(i, j) for i in range(1, self.m_rows)
         for j in range(1, self.m_cols)]

        o_score = self.matrix[i][j]
        return o_score
    
    def score(self, i, j):
        score = self.scoring[0] if (self.seqA[i-1] == self.seqB[j-1]) else self.scoring[1]
        h_val = self.matrix[i][j-1] + self.scoring[2]
        v_val = self.matrix[i-1][j] + self.scoring[2]
        d_val = self.matrix[i-1][j-1] + score
        o_val = [h_val, d_val, v_val]  # h=1, d=2, v=3
        
        self.matrix[i][j] = max(o_val)
        

@get_time_of_execution
def run():
    for i in range(0, 1):
        nn = NeedlemanWunsch()
        x = nn.run( "ACGA", 
                    "ACGC")
        print(x)

if __name__ == "__main__":
    run()
