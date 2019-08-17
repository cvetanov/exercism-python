codon_to_protein = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP"
}

def proteins(strand):
    proteins = []
    num_codons = len(strand) / 3
    for i in range(num_codons):
        codon = strand[i * 3 : (i + 1) * 3]
        protein = codon_to_protein[codon]
        if protein != "STOP":
            proteins.append(protein)
        else:
            break
    return proteins