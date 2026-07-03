def write_pdb(coords):

    with open("output/predicted_structure.pdb","w") as f:

        for i,(x,y,z) in enumerate(coords):

            line=f"ATOM {i:5d} CA ALA A {i:4d} {x:8.3f}{y:8.3f}{z:8.3f}"

            f.write(line+"\n")