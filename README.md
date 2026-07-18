# Protein-Structure-Visualization-using-Deep-Reinforcement-Learning


An AI-powered web application for predicting, visualizing, and analyzing protein structures from FASTA sequences. This project provides an interactive interface to generate protein structures, view predicted PDB files, and compare them with experimentally determined structures.



##  Features

- Upload and process protein FASTA sequences
- Protein sequence preprocessing and encoding
- AI-based protein structure prediction
- Generate Protein Data Bank (PDB) files
- Interactive 3D protein visualization
- Compare predicted structures with reference PDB structures
- JSON-based model output generation
- Simple and responsive web interface

---

##  Project Architecture

```
Protein Sequence
        │
        ▼
FASTA Reader
        │
        ▼
Preprocessing
        │
        ▼
Sequence Encoding
        │
        ▼
Structure Prediction
        │
        ▼
PDB Generation
        │
        ▼
3D Visualization
```

---

##  Project Structure

```
protein-visualizer/
│
├── app.py                    # Flask application
├── main.py                   # Main execution script
├── fasta_reader.py           # Reads FASTA files
├── preprocessing.py          # Cleans protein sequences
├── encoding.py               # Sequence encoding
├── structure_prediction.py   # Protein prediction logic
├── pdb_writer.py             # Generates PDB files
├── visualization.py          # Protein visualization
├── database_search.py        # Database search
├── feature_extraction.py     # Feature extraction
│
├── data/
│   └── sample.fasta
│
├── pdb_files/
├── predicted/
├── alphafold_outputs/
├── output/
│
├── templates/
├── index.html
├── page2.html
├── style.css
├── script.js
│
└── model_output.json
```

---

##  Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask

### Bioinformatics
- FASTA Sequence Processing
- Protein Data Bank (PDB)
- Protein Structure Prediction

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/bhagyasree327/protein-visualizer.git
```

```bash
cd protein-visualizer
```

### Install dependencies

```bash
pip install flask
```

(Install any additional required Python packages if needed.)

---

##  Running the Project

Start the Flask server:


python app.py


Open your browser:


http://127.0.0.1:5000/


##  Workflow

1. Read the input FASTA sequence.
2. Clean and preprocess the sequence.
3. Encode amino acid information.
4. Predict protein structure.
5. Generate a PDB file.
6. Visualize the predicted protein structure.
7. Export model information as JSON.

---

##  Output

The project generates:

- Predicted PDB structure
- Protein sequence information
- Model output JSON
- Interactive visualization

---

## Future Enhancements

- Support multiple protein sequences
- Deep learning-based structure prediction
- Protein-ligand interaction visualization
- RMSD comparison
- Mutation analysis
- Downloadable visualization reports
- Cloud deployment

---

##  Author

**Bhagyasri Divadari**

Bachelor of Technology (Computer Science & Engineering)

Interested in:
- Artificial Intelligence
- Bioinformatics
- Cloud Computing
- Full Stack Development

---

##  License

This project is developed for educational and research purposes.

