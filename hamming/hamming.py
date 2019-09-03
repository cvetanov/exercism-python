def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands have different length')
    zipped = zip(strand_a, strand_b)
    return sum(1 if a != b else 0 for (a, b) in zipped)
