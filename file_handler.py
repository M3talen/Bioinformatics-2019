from Bio import SeqIO
import os.path

"""
    Simple helper function for getting file extension.
"""
def _get_file_extension(filename):
    _, extension = os.path.splitext(filename)
    return extension[1:]

"""
    Function for reading and parsing FASTA/FASTQ files.
    It returns a list where every element is a dictionary,
    with two keys: id and seq.
"""
def read(filename):
    extension = _get_file_extension(filename)
    records = []

    with open(filename, "rU") as handle:
        for record in SeqIO.parse(handle, extension):
            records.append({'id' : record.id, 'seq' : str(record.seq)})
    return records

# Testing the speed of read/write functions.
if __name__ == '__main__':
    import sys
    import time
    file = sys.argv[1]
    start = time.time()
    _ = read(file)
    end = time.time()
    print(f"reading time: {(end - start)*1000} ms")