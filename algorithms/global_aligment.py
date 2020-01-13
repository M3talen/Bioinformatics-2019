""" 
    Author : Alen Štruklec
"""

"""
    Needleman-Wunsch algorithm
    Scoring follows this indexes :
    [0] MATCH = 5,
    [1] MISMATCH = -3,
    [2] GAP = -5    
"""
class NeedlemanWunsch():
    def __init__(self, scoring=[5,-3,-5]):
        self.scoring = scoring
    """
        Run Needleman-Wunsch algorithm on seqA and seqB
    """
    def run(self, seqA, seqB,):
        self.seqA = seqA
        self.seqB = seqB
        self.m_rows = len(seqA) + 1
        self.m_cols = len(seqB) + 1
        
        self.matrix = [[None for i in range(self.m_cols)] for i in range(self.m_rows)] # Initiating Score Matrix
        
        # Populate matrix 
        for i in range(self.m_rows):
            self.matrix[i][0] = self.scoring[2] * i
        for j in range(self.m_cols):
            self.matrix[0][j] = self.scoring[2] * j

        # Calculate similarity 
        [self.score(i, j) for i in range(1, self.m_rows) for j in range(1, self.m_cols)]

        o_score = self.matrix[i][j]
        return o_score
    
    """ 
            Calculate similarity with the maximum value from the following :
            D_(i-1)_(j-1) + MATCH     if seqA_i == seqB_i 
            D_(i-1)_(j-1) + MISSMATCH if seqA_i != seqB_i 
            D_(i-1)_(j)   + GAP       if seqB_i == - 
            D_(i)_(j-1)   + GAP       if seqA_i == - 
    """
    def score(self, i, j):
        score = self.scoring[0] if (self.seqA[i-1] == self.seqB[j-1]) else self.scoring[1]
        h_val = self.matrix[i][j-1] + self.scoring[2]
        v_val = self.matrix[i-1][j] + self.scoring[2]
        d_val = self.matrix[i-1][j-1] + score
        o_val = [h_val, d_val, v_val]  # h=1, d=2, v=3
        
        self.matrix[i][j] = max(o_val)
        