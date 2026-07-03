valid_amino_acids=set("ACDEFGHIKLMNPQRSTVWY")

def clean_sequence(seq):

    seq=seq.upper()

    cleaned=""
    removed=[]

    for aa in seq:
        if aa in valid_amino_acids:
            cleaned+=aa
        else:
            removed.append(aa)

    return cleaned,removed