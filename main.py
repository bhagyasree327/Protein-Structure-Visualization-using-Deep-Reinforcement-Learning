import webbrowser

from fasta_reader import read_fasta
from preprocessing import clean_sequence
from encoding import encode_sequence
from structure_prediction import generate_coordinates, refine_structure
from pdb_writer import write_pdb
from visualization import visualize
import json   # ✅ ADDED

# -------------------------
# READ FASTA
# -------------------------
header, sequence = read_fasta("data/sample.fasta")

# -------------------------
# CLEAN SEQUENCE
# -------------------------
sequence, _ = clean_sequence(sequence)

# -------------------------
# ENCODE
# -------------------------
encoded = encode_sequence(sequence)

# -------------------------
# GENERATE STRUCTURE
# -------------------------
coords = generate_coordinates(len(sequence))
coords = refine_structure(coords)

# -------------------------
# SAVE PDB
# -------------------------
write_pdb(coords)

# -------------------------
# ✅ SAVE OUTPUT JSON (ADDED)
# -------------------------
data = {
    "sequence": sequence,
    "length": len(sequence)
}

with open("model_output.json", "w") as f:
    json.dump(data, f, indent=4)

colab_url = "https://colab.research.google.com/drive/1sKSfvfbErmPrjl_9KmaHGWJ7GWUEgBvA?usp=sharing"
webbrowser.open(colab_url)


