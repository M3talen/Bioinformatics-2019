"""
    Author : Zlako Verk
"""
import itertools
import numpy as np 

"""
    Smith-Waterman algorithm
"""
class SmithWaterman():
    def __init__(self, match, mismatch, gap):
        self.match = match
        self.mismatch = mismatch
        self.gap = gap

    """
        Calculate simiraity of seqA and seqB
        Aligment 'local' or 'glocal'
    """
    def score(self, seqA, seqB, alignment='local'):
        
        H = np.zeros((len(seqA) + 1, len(seqB) + 1), np.int) #Initialize matrix

        """ 
            Calculate score with the maximum value from the following :
            D_(i-1)_(j-1) + MATCH     if seqA_i == seqB_i 
            D_(i-1)_(j-1) + MISSMATCH if seqA_i != seqB_i 
            D_(i-1)_(j)   + GAP       if seqB_i == - 
            D_(i)_(j-1)   + GAP       if seqA_i == - 
            0 (zero)
        """
        for i, j in itertools.product(range(1, H.shape[0]), range(1, H.shape[1])):
            match = H[i - 1, j - 1] + (self.match if seqA[i - 1] == seqB[j - 1] else + self.mismatch)
            gap = H[i - 1, j] + self.gap
            mismatch = H[i, j - 1] + self.gap
            H[i, j] = max(match, gap, mismatch, 0) if alignment == 'local' else max(match, gap, mismatch) #Calculate glocal without zero or local with zero

        return H.max() if alignment == 'local' else H[len(seqA), ].max()