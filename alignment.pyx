"""
    Author : Zvonimir Kucis
    Code wrapper for calling C functions from Python scripts.
"""

cdef extern from "alignment.h":
    int local_score(char genA[], char genB[])
    int global_score(char genA[], char genB[])

def py_local(genA, genB) -> int:
    return local_score(genA, genB)

def py_global(genA : bytes, genB : bytes) -> int:
    return global_score(genA, genB)