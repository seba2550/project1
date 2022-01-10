# write tests for transcribes

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the
    transcribe function here.
    """
    sample_dna = "GATGGAACTTGACTACGTAAATT" # Sample DNA string from the Rosalind "rna" problem
    sample_rna = "GAUGGAACUUGACUACGUAAAUU" # Corresponding transcribed string from the Rosalind website
    rna = transcribe(sample_dna)

    assert sample_rna == rna # Result of my transcribe function should be the same as the sequence from Rosalind
    assert "T" not in rna    # Transcribed result should only have Uracils in place of Thymines
    assert len(sample_dna) == len(rna) # Length of sequence should remain constant


def test_reverse_transcribe():
    """
    Write your unit test for the
    reverse transcribe function here.
    """
    sample_dna = "GATGGAACTTGACTACGTAAATT" # Same string we used for test_transcribe
    sample_rna = "GAUGGAACUUGACUACGUAAAUU" 
    rev_rna = reverse_transcribe(sample_dna)

    assert rev_rna == sample_rna[::-1] # Sequences should be identical 
    assert len(rev_rna) == len(sample_dna) # Length of sequence should remain constant



