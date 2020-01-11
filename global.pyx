cdef extern from "global.h":
    int run(char genA[],  char genB[])

def py_run(genA : bytes, genB : bytes) -> int:
    return run(genA, genB)