# Needleman-Wunsch algorithm
import time
from enum import Enum

def get_time_of_execution(f):
    """ Decorator to get time of execution """

    def wrapped(*args, **kwargs):
        start_time = time.time()
        res = f(*args, **kwargs)
        print(
            f'Time elapsed to {f.__name__ } (s): { str(time.time() - start_time)}')
        return res

    return wrapped


class SampleScoring(Enum):
    MATCH = 5,
    MISMATCH = -3,
    GAP = -5

class NeedlemanWunsch():
    def __init__(self, seqA, seqB, scoring=SampleScoring):
        self.seqA = seqA
        self.seqB = seqB
        self.m_rows = len(seqA) + 1  # number of rows
        self.m_cols = len(seqB) + 1  # number of columns
        self.matrix = [[[[None] for i in range(2)] for i in range(
            self.m_cols)] for i in range(self.m_rows)]  # Initiating Score Matrix
        self.scoring = scoring
        self.aln_pathways = []

    def run(self,):
        for i in range(self.m_rows):
            self.matrix[i][0] = [self.scoring.GAP.value * i, []]
        for j in range(self.m_cols):
            self.matrix[0][j] = [self.scoring.GAP.value * j, []]

        [self.score(i, j) for i in range(1, self.m_rows)
         for j in range(1, self.m_cols)]

        o_score = self.matrix[i][j][0]
        #print(o_score)
        return o_score
      #  bk_i = i
      #  bk_j = j

      #  self.aligments = []
      #  self.find_each_path(bk_i, bk_j)
      #  
      #  score = self.matrix[bk_i][bk_j][0]
      #  print(score)
      #  return score

    def score(self, i, j):
        score = self.scoring.MATCH.value if (
            self.seqA[i-1] == self.seqB[j-1]) else self.scoring.MISMATCH.value
        h_val = self.matrix[i][j-1][0] + self.scoring.GAP.value
        v_val = self.matrix[i-1][j][0] + self.scoring.GAP.value
        d_val = self.matrix[i-1][j-1][0] + score[0]
        o_val = [h_val, d_val, v_val]  # h=1, d=2, v=3
        self.matrix[i][j] = [
            max(o_val), [i+1 for i, v in enumerate(o_val) if v == max(o_val)]]

    def find_each_path(self, c_i, c_j, path=''):
        i = c_i
        j = c_j
        if i == 0 and j == 0:
            self.aln_pathways.append(path)
            return 2
        t_dir = len(self.matrix[i][j][1])
        while t_dir <= 1:
            n_dir = self.matrix[i][j][1][0] if (i != 0 and j != 0) else (
                1 if i == 0 else (3 if j == 0 else 0))
            path = path + str(n_dir)

            j = j-1 if (n_dir == 1 or n_dir == 2) else j
            i = i-1 if (n_dir == 2 or n_dir == 3) else i

            t_dir = len(self.matrix[i][j][1])
            if i == 0 and j == 0:
                self.aln_pathways.append(path)
                return 3
        if t_dir > 1:
            for c_dir in range(t_dir):
                n_dir = self.matrix[i][j][1][c_dir] if (i != 0 and j != 0) else (
                    1 if i == 0 else (3 if j == 0 else 0))
                tmp_path = path + str(n_dir)

                n_i = i-1 if (n_dir == 2 or n_dir == 3) else i
                n_j = j-1 if (n_dir == 1 or n_dir == 2) else j

                self.find_each_path(n_i, n_j, tmp_path)

        return len(self.aln_pathways)

    def backtrace(bk_i, bk_j):
        for _e in self.aln_pathways:
            i = bk_i - 1
            j = bk_j - 1
            side_aln = ''
            top_aln = ''
            step = 0
            aln_info = []
            for n_dir_c in range(len(_e)):
                n_dir = _e[n_dir_c]
                score = self.matrix[i+1][j+1][0]
                step = step + 1
                aln_info.append([step, score, n_dir])
                if n_dir == '2':
                    side_aln = side_aln + self.seqA[i]
                    top_aln = top_aln + self.seqB[j]
                    i = i-1
                    j = j-1
                elif n_dir == '1':
                    side_aln = side_aln + '-'
                    top_aln = top_aln + self.seqB[j]
                    j = j-1
                elif n_dir == '3':
                    side_aln = side_aln + self.seqA[i]
                    top_aln = top_aln + '-'
                    i = i-1
            aln_count = aln_count + 1
            self.aligments.append(
                [top_aln[::-1], side_aln[::-1], _e, aln_info, aln_count])

@get_time_of_execution
def run():
    for i in range(0, 100):
        nn = NeedlemanWunsch("ACTGAGAGATAGAGTCAGCTACGTCGATCGACTAGCTACGATCGACTGAGAGATAGAGTCAGCTACGTCGATCGACTAGCTACGATCGACTGAGAGATAGAGTCAGCTACGTCGATCGACTAGCTACGATCGACTGAGAGATAGAGTCAGCTACGTCGATCGACTAGCTACGATCGACTGAGAGATAGAGTCAGCTACGTCGATCGACTAGCTACGATCGACTGAGAGATAGAGTCAGCTACGTCGATCGACTAGCTACGATCGACTGAGAGATAGAGTCAGCTACGTCGATCGACTAGCTACGATCG", "ACGCTAGCATCGATCGATCGATCGATCGATCAGTCAGCTACGATCGATCGATCGCTGCTAGCTACGATCGATCGATCGTCAGTCAACGCTAGCATCGATCGATCGATCGATCGATCAGTCAGCTACGATCGATCGATCGCTGCTAGCTACGATCGATCGATCGTCAGTCAACGCTAGCATCGATCGATCGATCGATCGATCAGTCAGCTACGATACGCTAGCATCGATCGATCGATCGATCGATCAGTCAGCTACGATCGATCGATCGCTGCTAGCTACGATCGATCGATCGTCAGTCACGATCGATCGCTGCTAGCTACGATCGATCGATCGTCAGTCA")
        nn.run()

if __name__ == "__main__":
    run()
