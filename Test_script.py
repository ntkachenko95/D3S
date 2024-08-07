from D3S import D3S
import os

S6,S8,ALPHA1,ALPHA2 = D3S.DFT_D3BJ_parameters["BLYP"]
COORDS = D3S.read_XYZ(os.path.join("./Test_geometries", "H2_NiKur_BLYP_1D_scan.xyz"))

#compute D3S(BJ) energies for the scan geometries
D3S_BJ_energy_list = []
for COORD in COORDS:
    D3S_BJ_energy_list.append(D3S.D3SBJ(COORD, S6,S8,ALPHA1,ALPHA2))

#compute D3(BJ) energies for the scan geometries
D3_BJ_energy_list = []
k3 = 4
for COORD in COORDS:
    D3_BJ_energy_list.append(D3S.D3BJ(COORD, S6,S8,ALPHA1,ALPHA2,k3))

with open("D3S_BJ.txt", 'w') as f:
    for line in D3S_BJ_energy_list:
        f.write(f"{line}\n")

with open("D3_BJ.txt", 'w') as f:
    for line in D3_BJ_energy_list:
        f.write(f"{line}\n")