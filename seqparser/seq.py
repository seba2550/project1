# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by replacing
    all `T` to `U`
    """
    rna = seq.replace('T','U')

    return rna

def reverse_transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by replacing
    all `T` to `U` then reverses the sequence
    """
    rna = transcribe(seq)
    reverse_rna = rna[::-1]

    return reverse_rna
