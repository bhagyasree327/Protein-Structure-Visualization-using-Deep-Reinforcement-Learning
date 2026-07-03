def read_fasta(filepath):
    header = ""
    sequence = ""

    with open(filepath,"r") as file:
        for line in file:
            line=line.strip()
            if line.startswith(">"):
                header=line
            else:
                sequence+=line

    return header,sequence