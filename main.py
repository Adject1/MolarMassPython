import re

MolarMasses = {
    #All elements (Verified)
    "H": 1.008,
    "He": 4.003,
    "Li": 6.941,
    "Be": 9.012,
    "B": 10.811,
    "C": 12.011,
    "N": 14.007,
    "O": 15.999,
    "F": 18.998,
    "Ne": 20.180,
    "Na": 22.990,
    "Mg": 24.305,
    "Al": 26.982,
    "Si": 28.085,
    "P": 30.974,
    "S": 32.066,
    "Cl": 35.453,
    "Ar": 39.948,
    "K": 39.098,
    "Ca": 40.078,
    "Sc": 44.956,
    "Ti": 47.867,
    "V": 50.942,
    "Cr": 51.996,
    "Mn": 54.938,
    "Fe": 55.845,
    "Co": 58.933,
    "Ni": 58.693,
    "Cu": 63.546,
    "Zn": 65.380,
    "Ga": 69.723,
    "Ge": 72.631,
    "As": 74.922,
    "Se": 78.971,
    "Br": 79.904,
    "Kr": 83.798,
    "Rb": 85.468,
    "Sr": 87.620,
    "Y": 88.906,
    "Zr": 91.224,
    "Nb": 92.906,
    "Mo": 95.950,
    "Tc": 98.907,
    "Ru": 101.070,
    "Rh": 102.906,
    "Pd": 106.420,
    "Ag": 107.868,
    "Cd": 112.414,
    "In": 114.818,
    "Sn": 118.711,
    "Sb": 121.760,
    "Te": 127.600,
    "I": 126.904,
    "Xe": 131.294,
    "Cs": 132.905,
    "Ba": 137.328,
    "La": 138.905,
    "Ce": 140.116,
    "Pr": 140.908,
    "Nd": 144.243,
    "Pm": 144.913,
    "Sm": 150.360,
    "Eu": 151.964,
    "Gd": 157.250,
    "Tb": 158.930,
    "Dy": 162.500,
    "Ho": 164.930,
    "Er": 167.259,
    "Tm": 168.934,
    "Yb": 173.055,
    "Lu": 174.967,
    "Hf": 178.490,
    "Ta": 180.948,
    "W": 183.840,
    "Re": 186.207,
    "Os": 190.230,
    "Ir": 192.217,
    "Pt": 195.085,
    "Au": 196.967,
    "Hg": 200.592,
    "Tl": 204.383,
    "Pb": 207.200,
    "Bi": 208.980,
    "Po": 208.982,
    "At": 209.987,
    "Rn": 222.018,
    "Fr": 233.020,
    "Ra": 226.025,
    "Ac": 227.028,
    "Th": 232.038,
    "Pa": 231.036,
    "U": 238.029,
    "Np": 237.048,
    "Pu": 244.064,
    "Am": 243.061,
    "Cm": 247.070,
    "Bk": 247.070,
    "Cf": 251.080,
    "Es": 254.000,
    "Fm": 257.095,
    "Md": 258.100,
    "No": 259.101,
    "Lr": 262.000,
    "Rf": 261.000,
    "Db": 262.000,
    "Sg": 266.000,
    "Bh": 264.000,
    "Hs": 269.000,
    "Mt": 278.000,
    "Ds": 281.000,
    "Rg": 280.000,
    "Cn": 285.000,
    "Nh": 286.000,
    "Fl": 289.000,
    "Mc": 289.000,
    "Lv": 293.000,
    "Ts": 294.000,
    "Og": 294.000,
}

CommonDict = {
    "Water": "H2O",
    "Hydrogen Peroxide": "H2O2",
    "Hydrochloric Acid": "HCl",
    "Hydrogen Chloride": "HCl",
    "Sulfuric Acid": "H2SO4",
    "Nitric Acid": "HNO3",
    "Acetic Acid": "CHCOO3",
    "Ammonia": "NH3",
    "Sulfur Dioxide": "SO2",
    "Sulfur Trioxide": "SO3",
    "Carbon Monoxide": "CO",
    "Carbon Dioxide": "CO2",
    "Methane": "CH4",
    "Ethane": "C2H6",
    "Propane": "C3H8",
    "Butane": "C4H10",
    "Pentane": "C5H12",
    "Hexane": "C6H14",
    "Heptane": "C7H16",
    "Octane": "C8H18",
    "Benzene": "C6H6",
    "Methanol": "CH3OH",
    "Ethanol": "C2H5OH",
    "Acetone": "CH3COCH3",
    "Diethyl Ether": "CH3CH2OCH2CH3",
    "Ether": "CH3CH2OCH2CH3",
    "Tetrafluoroethylene": "C2F4",
    "Butadiene": "C4H6",
    "Cyclohexane": "C6H12",
    "Ethylene": "C2H4",
    "Acetylene": "C2H2",
    "Isohexane": "C6H14",
    "Naphthalene": "C10H8",
    "Phenolphthalein": "C20H14O4",
    "Nitroglycerin": "C3H5N3O9",
    "Methylchloroisothiazolinone": "C4H4ClNOS",
    "Methylisothiazolinone": "C4H5NOS",
    "Benzisothiazolinone": "C7H5NOS",
    "Lilial": "C14H20O",
    "Formaldehyde": "CH2O",
    "Glucose": "C6H12O6",
    "Fructose": "C6H12O6",
    "Sucrose": "C12H22O11",
    "Lactose": "C12H22O11",
    "Galactose": "C6H12O6",
    "Cellulose": "C6H12O5",
    "Cocaine": "C17H21NO4",
    "Indole": "C8H7N",
    "Sodium Cyanide": "NaCN",
    "Hydrogen Cyanide": "HCN",
    "Codeine": "C18H21NO3",
    "Sodium Laureth Sulfate": "CH3C10H20CH2OSO3Na",
    "Lauric Acid": "C12H24O2",
    "Diethanolamine": "C4H11NO2",
    "Cocamidopropyl Betaine": "C19H38N2O3",
    "Nitroformic Acid": "CHNO4"
}

formula = input("Molecular formula: ")
if formula in CommonDict:
    formula = CommonDict[formula]
parser = re.findall("([A-Z][a-z]*)([0-9]*)", formula)

KeyList = []
TotalList = []

for x in range(0, len(parser)):
    pair = parser[x]
    if pair[0] in MolarMasses:
        if pair[1] == '':
            placeholder = pair[0]
            del parser[x]
            pair = (placeholder, '1')
            parser.insert(0, pair)
        count = int(pair[1])
        if pair[0] in KeyList:
            TotalList[KeyList.index(pair[0])] += (MolarMasses[pair[0]] * count)
        else:
            KeyList.append(pair[0])
            TotalList.append(MolarMasses[pair[0]] * count)
    else:
        print("One or more elements was invalid.")
        TotalList = []
        break

print("The molar mass of your molecule, " + formula + ", is " +
      str(round(sum(TotalList), 3)) + " g/mol\n")

total = round(sum(TotalList), 3)

for x in range(0, len(KeyList)):
    print("Mass" + KeyList[x] + " = " + str(TotalList[x]) + " g/mol")
    print("%" + KeyList[x] + " = " + str((TotalList[x] / total) * 100))

for key in CommonDict:
    if CommonDict[key] == formula:
        print("\n Your molecule is also known as " + key)
