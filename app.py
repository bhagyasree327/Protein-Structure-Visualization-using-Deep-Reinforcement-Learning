from flask import Flask, jsonify, send_from_directory, send_file
import json
import os

app = Flask(__name__)

# ---------------- HOME ----------------
@app.route("/")
def home():
    return send_from_directory(".", "index.html")


# ---------------- PAGE 2 ----------------
@app.route("/page2.html")
def page2():
    return send_from_directory(".", "page2.html")


# ---------------- PER-PROTEIN JSON ----------------
@app.route("/alphafold_outputs/<path:filename>")
def serve_json(filename):
    return send_from_directory("alphafold_outputs", filename)


# ---------------- PREDICTED PDB ----------------
@app.route("/predicted/<path:filename>")
def serve_predicted(filename):
    return send_from_directory("predicted", filename)


# ---------------- REAL PDB ----------------
@app.route("/pdb_files/<path:filename>")
def serve_real(filename):
    return send_from_directory("pdb_files", filename)


# ---------------- MODEL OUTPUT ----------------
@app.route("/model_output.json")
def model_output():
    if os.path.exists("model_output.json"):
        return send_file("model_output.json")
    else:
        return jsonify({"error": "model_output.json not found"})


# ---------------- OLD SINGLE JSON (OPTIONAL) ----------------
@app.route("/alphafold")
def alphafold():
    if os.path.exists("final_result.json"):
        with open("final_result.json") as f:
            data = json.load(f)
        return jsonify(data)
    else:
        return jsonify({"error": "final_result.json not found"})


# ---------------- RUN MODEL ----------------
@app.route("/run_model")
def run_model():
    try:
        from fasta_reader import read_fasta
        from preprocessing import clean_sequence
        from encoding import encode_sequence
        from structure_prediction import generate_coordinates, refine_structure
        from pdb_writer import write_pdb

        header, sequence = read_fasta("data/sample.fasta")
        sequence, _ = clean_sequence(sequence)
        encoded = encode_sequence(sequence)

        coords = generate_coordinates(len(sequence))
        coords = refine_structure(coords)

        write_pdb(coords)

        data = {
            "sequence": sequence,
            "length": len(sequence)
        }

        with open("model_output.json", "w") as f:
            json.dump(data, f, indent=4)

        return jsonify({"message": "Model run complete"})

    except Exception as e:
        return jsonify({"error": str(e)})


# ---------------- STATIC FILES ----------------
@app.route("/script.js")
def script():
    return send_from_directory(".", "script.js")


@app.route("/style.css")
def style():
    return send_from_directory(".", "style.css")


# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    app.run(debug=True)