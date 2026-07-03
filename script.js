let viewer1 = null;
let viewer2 = null;

// ================= FILE LIST =================

const predictedFiles = [
"crambin_predicted.pdb","myoglobin_predicted.pdb",
"ubiquitin_predicted.pdb","cytochrome_c_predicted.pdb","lysozyme_predicted.pdb",
"ferredoxin_predicted.pdb","rubredoxin_predicted.pdb","thioredoxin_predicted.pdb",
"protein_l_predicted.pdb","villin_headpiece_predicted.pdb","trypsin_inhibitor_predicted.pdb",
"trp-cage_mini_protein_predicted.pdb","melittin_predicted.pdb","insulin_chain_b_predicted.pdb",
"glucagon_predicted.pdb","cold_shock_protein_predicted.pdb"
];

const realFiles = [
"crambin.pdb","myoglobin.pdb","ubiquitin.pdb","cytochrome_c.pdb",
"lysozyme.pdb","ferredoxin.pdb","rubredoxin.pdb","thioredoxin.pdb","protein_l.pdb",
"villin_headpiece.pdb","trypsin_inhibitor.pdb","trp-cage_mini_protein.pdb",
"melittin.pdb","insulin_chain_b.pdb","glucagon.pdb","cold_shock_protein.pdb"
];

// ================= DROPDOWNS =================

const predictedDropdown = document.getElementById("predictedSelect");
const realDropdown = document.getElementById("proteinSelect");

// populate predicted
if (predictedDropdown) {
    predictedFiles.forEach(file => {
        const option = document.createElement("option");
        option.value = file;
        option.textContent = file.replace(".pdb", "");
        predictedDropdown.appendChild(option);
    });
}

// populate real
if (realDropdown) {
    realFiles.forEach(file => {
        const option = document.createElement("option");
        option.value = file;
        option.textContent = file.replace(".pdb", "");
        realDropdown.appendChild(option);
    });
}

// ================= HELPER (WHITE VIEWER) =================

function createViewer(elementId){
    return $3Dmol.createViewer(elementId, {
        backgroundColor: "white"   // ✅ FIXED HERE
    });
}

// ================= PREDICTED HANDLER =================

if (predictedDropdown) {
predictedDropdown.addEventListener("change", async function () {

const fileName = this.value;
if (!fileName) return;

const viewerElement = document.getElementById("viewer1");
const isPage1 = document.getElementById("seq") !== null;

try {

    // ===== PAGE 1 DATA =====
    if (isPage1) {

        document.getElementById("seq").innerText = "-";
        document.getElementById("len").innerText = "-";
        document.getElementById("plddt").innerText = "-";
        document.getElementById("pdbText").innerText = "";

        const protein = fileName.replace(".pdb", "");

        const jsonRes = await fetch(`/alphafold_outputs/${protein}.json`);
        const data = await jsonRes.json();

        document.getElementById("seq").innerText = data.sequence || "-";
        document.getElementById("len").innerText = data.length || "-";

        if (Array.isArray(data.pLDDT)) {
            let avg = data.pLDDT.reduce((a,b)=>a+b,0)/data.pLDDT.length;
            document.getElementById("plddt").innerText = avg.toFixed(2);
        } else {
            document.getElementById("plddt").innerText = data.pLDDT || "-";
        }

        document.getElementById("logs").innerText = data.full_output || "No logs";
    }

    // ===== LOAD PDB =====
    const pdbRes = await fetch(`/predicted/${fileName}`);
    const pdbData = await pdbRes.text();

    if (document.getElementById("pdbText")) {
        document.getElementById("pdbText").innerText = pdbData;
    }

    // ===== VIEWER =====
    if (!viewer1) {
        viewer1 = createViewer(viewerElement);  // ✅ WHITE
    }

    viewer1.clear();
    viewer1.addModel(pdbData, "pdb");
    viewer1.setStyle({}, {cartoon:{color:"spectrum"}});
    viewer1.zoomTo();
    viewer1.render();

} catch (err) {
    console.error("Predicted error:", err);
}

});
}

// ================= ORIGINAL PROTEIN =================

if (realDropdown) {
realDropdown.addEventListener("change", async function () {

const fileName = this.value;
if (!fileName) return;

try {
    const res = await fetch(`/pdb_files/${fileName}`);
    const pdbData = await res.text();

    if (!viewer2) {
        viewer2 = createViewer("viewer2"); // ✅ WHITE
    }

    viewer2.clear();
    viewer2.addModel(pdbData, "pdb");
    viewer2.setStyle({}, {cartoon:{color:"spectrum"}});
    viewer2.zoomTo();
    viewer2.render();

} catch (err) {
    console.error("Original error:", err);
}

});
}

// ================= FILE UPLOAD =================

const uploadInput = document.getElementById("uploadPDB");
const isPage2 = document.getElementById("seq") === null;

if (uploadInput && isPage2) {
uploadInput.addEventListener("change", function(event) {

    const file = event.target.files[0];
    if (!file) return;

    const reader = new FileReader();

    reader.onload = function(e) {

        const pdbData = e.target.result;

        if (!viewer1) {
            viewer1 = createViewer("viewer1"); // ✅ WHITE
        }

        const dropdown = document.getElementById("predictedSelect");
        if (dropdown) dropdown.value = "";

        viewer1.clear();
        viewer1.addModel(pdbData, "pdb");
        viewer1.setStyle({}, {cartoon:{color:"spectrum"}});
        viewer1.zoomTo();
        viewer1.render();
    };

    reader.readAsText(file);
});
}

// ================= BUTTON ACTIVE =================

function setActiveButton(btn){
let buttons = btn.parentElement.querySelectorAll("button");
buttons.forEach(b => b.classList.remove("active"));
btn.classList.add("active");
}

// ================= CONTROLS =================

function cartoonView1(){ if(viewer1){ viewer1.setStyle({}, {cartoon:{color:"spectrum"}}); viewer1.render(); } }
function stickView1(){ if(viewer1){ viewer1.setStyle({}, {stick:{radius:0.2}}); viewer1.render(); } }
function sphereView1(){ if(viewer1){ viewer1.setStyle({}, {sphere:{scale:0.3}}); viewer1.render(); } }
function resetView1(){ location.reload(); }

function cartoonView2(){ if(viewer2){ viewer2.setStyle({}, {cartoon:{color:"spectrum"}}); viewer2.render(); } }
function stickView2(){ if(viewer2){ viewer2.setStyle({}, {stick:{radius:0.2}}); viewer2.render(); } }
function sphereView2(){ if(viewer2){ viewer2.setStyle({}, {sphere:{scale:0.3}}); viewer2.render(); } }
function resetView2(){ location.reload(); }