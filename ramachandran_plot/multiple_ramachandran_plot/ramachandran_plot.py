# Import Biopython, Matplotlib and NumPy libraries
import Bio.PDB
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import numpy as np

# Import the Hemoglobin coordinates file from the Protein Data Bank.
structure = Bio.PDB.PDBParser(QUIET=True).get_structure('Hemoglobin', 'data/1a3n.pdb')

# Define a function to build a model of the protein from the coordinates.
def build_model(structure, resid, offset):
    angles = list()
    for model in structure:
        for chain in model:
            polypeptides = Bio.PDB.CaPPBuilder().build_peptides(chain)
            for poly_index, poly in enumerate(polypeptides):
                phi_psi = poly.get_phi_psi_list()
                for res_index, residue in enumerate(poly):
                    phi, psi = phi_psi[res_index]
                    if (phi and psi) and poly[res_index + offset].resname == resid:
                        angles.append(['Hemoglobin', str(chain.id), residue.resname,
                                       residue.id[1], phi / np.pi, psi / np.pi])
    return np.array(angles)


# Run our function.
angles_gly = build_model(structure, 'GLY', 1)
angles_ala = build_model(structure, 'ALA', 1)
angles_pre_pro = build_model(structure, 'PRO', 1)


# Plot ramachandran plot
fig, axis = plt.subplots(3,1)
  
# Alanine
axis[0].scatter(angles_gly[:, 4].astype(float), angles_gly[:, 5].astype(float))
axis[0].set_title("Glycine")
axis[0].set_xlim([-1, +1 ])
axis[0].set_xlabel('$\phi$')
axis[0].set_ylabel('$\pi$')
  
# Glycine
axis[1].scatter(angles_ala[:, 4].astype(float), angles_ala[:, 5].astype(float))
axis[1].set_title("Alanine")
axis[1].set_xlim([-1, +1 ])
axis[1].set_xlabel('$\phi$')


# Pre proline
axis[2].scatter(angles_pre_pro[:, 4].astype(float), angles_pre_pro[:, 5].astype(float))
axis[2].set_title("pre-Proline")
axis[2].set_xlim([-1, +1 ]) 
axis[2].set_ylabel('$\pi$')
axis[2].set_xlabel('$\phi$')

plt.show()
