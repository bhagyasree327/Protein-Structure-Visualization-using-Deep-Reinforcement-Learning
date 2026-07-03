def generate_kmers(seq,k):

    kmers=[]

    for i in range(len(seq)-k+1):
        kmers.append(seq[i:i+k])

    return set(kmers)

def kmer_search(query,database,k=3):

    query_kmers=generate_kmers(query,k)

    results=[]

    for protein in database:

        db_kmers=generate_kmers(protein,k)

        matches=query_kmers.intersection(db_kmers)

        score=len(matches)

        results.append((protein,score,matches))

    return results