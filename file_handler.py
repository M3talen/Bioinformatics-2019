"""
    Author : Zlatko Verk
"""
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqIO import FastaIO
import os.path

"""
    Simple helper function for getting file extension.
"""
def _get_file_extension(filename):
    _, extension = os.path.splitext(filename)
    return extension[1:]

"""
    Function for reading and parsing FASTA/FASTQ files.
    Input argument is filename.
    It returns a list where every element is a dictionary,
    with three keys: id, seq and description.
"""
def read(filename):
    extension = _get_file_extension(filename)
    records = []

    with open(filename, "rU") as handle:
        for record in SeqIO.parse(handle, extension):
            records.append({'id' : record.id, 
                            'seq' : str(record.seq), 
                            'description' : record.description})
    return records

"""
    Function for writing FASTA files.
    Input argumnets are data that needs to be writen
    and filename where to save data.
    It returns nothing.
"""
def write(data, filename):
    records = []
    with open(filename, "w") as handle:
        fasta_out = FastaIO.FastaWriter(handle, wrap=None)
        for element in data:
            sequence = SeqRecord(Seq(element['seq']), 
                                    id=element['id'], 
                                    description=element['description'])
            records.append(sequence)
        fasta_out.write_file(records)
