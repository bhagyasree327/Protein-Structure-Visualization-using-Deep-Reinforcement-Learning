import numpy as np

match=1
mismatch=-1
gap=-2

def create_matrix(seq1,seq2):

    rows=len(seq1)+1
    cols=len(seq2)+1

    matrix=np.zeros((rows,cols))

    for i in range(rows):
        matrix[i][0]=i*gap

    for j in range(cols):
        matrix[0][j]=j*gap

    return matrix


def fill_matrix(matrix,seq1,seq2):

    for i in range(1,len(seq1)+1):

        for j in range(1,len(seq2)+1):

            if seq1[i-1]==seq2[j-1]:
                score=match
            else:
                score=mismatch

            diag=matrix[i-1][j-1]+score
            up=matrix[i-1][j]+gap
            left=matrix[i][j-1]+gap

            matrix[i][j]=max(diag,up,left)

    return matrix