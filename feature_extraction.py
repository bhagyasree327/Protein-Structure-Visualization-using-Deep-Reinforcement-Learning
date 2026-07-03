import pandas as pd

def msa_features(msa):

    msa_matrix=pd.DataFrame([list(seq) for seq in msa])

    features={}

    for col in msa_matrix.columns:

        freq=msa_matrix[col].value_counts(normalize=True)

        features[col]=freq.to_dict()

    return features