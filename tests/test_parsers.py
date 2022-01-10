# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser
    class here. You should generate an instance of
    your FastaParser class and assert that it properly
    reads in the example Fasta File.
    """
    fasta_path = "/Users/sebastiancruzgonzales/Documents/UCSF/BMI_203/project1/data/test.fa"
    fasta_test_instance = FastaParser(fasta_path)

    fasta_line_count = 0
    for i in fasta_test_instance:
        fasta_line_count += 2 # Count the two lines per record that we parsed from the fasta file


    fasta_num_lines = sum(1 for line in open(fasta_path))

    assert fasta_line_count == fasta_num_lines # Number of lines in file must match the number of records we parsed * 2


def test_FastqParser():
    """
    Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    """
    fastq_path = "/Users/sebastiancruzgonzales/Documents/UCSF/BMI_203/project1/data/test.fq"
    fastq_test_instance = FastqParser(fastq_path)

    fastq_line_count = 0
    for i in fastq_test_instance:
        fastq_line_count += 4 # Count the for lines per record that we parsed from the fastq file

    fastq_num_lines = sum(1 for line in open(fastq_path))

    assert fastq_line_count == fastq_num_lines # Number of lines in file must match the number of records we parsed * 4

