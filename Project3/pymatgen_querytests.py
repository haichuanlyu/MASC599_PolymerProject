from pymatgen import MPRester
import re
import pandas as pd

mpr = MPRester("w8omvyv2A531Mbub6Wt")

print(mpr.supported_properties)

prop = [
    'energy',  # Calculated vasp energy for structure
    # 'energy_per_atom',  # Calculated vasp energy normalized to per atom in the unit cell
    'volume',  # Final relaxed volume of the material
    'formation_energy_per_atom',  # Calculated formation energy from the elements normalized to per atom in the unit cell
    # 'nsites',  # Number of sites in the unit cell
    # 'unit_cell_formula',  # The full explicit formula for the unit cell
    'pretty_formula',  # A nice formula where the element amounts are normalized
    # 'is_hubbard',  # A boolean indicating whether the structure was calculated using the Hubbard U extension to DFT
    # 'elements',  # A array of the elements in the material
    # 'nelements',  # The number of elements in the material
    # 'e_above_hull',  # Calculated energy above convex hull for structure. Please see Phase Diagram Manual for the interpretation of this quantity.
    # 'hubbards',  # An array of Hubbard U values, where applicable
    # 'is_compatible',  # Whether this calculation is considered compatible under the GGA/GGA+U mixing scheme
    # 'spacegroup',  # An associative array containing basic space group information
    # 'task_ids',
    'band_gap',  # 待定
    'density',  # Final relaxed density of the material
    # 'icsd_id',  # The Inorganic Crystal Structure Database id for the initial structure, if any.
    # 'icsd_ids',
    # 'cif',  # A string containing the structure in the CIF format
    'total_magnetization',  # total magnetic moment of the unit cell
    # 'material_id',
    # 'oxide_type',  # 好像没什么用。。。 oxide/superoxide
    # 'tags',
    'elasticity'  # Mechanical properties in the elastic limit. Contains the full elastic tensor as well as derived properties, e.g. Poisson ratio and bulk (K) and shear (G) moduli.
]

# simple formula
# data = mpr.query("MoS2", properties=prop)

# by element
data = mpr.query("Fe-O", properties=prop)

# by element with condition
# data = mpr.query({ "elements":{"$all":["Si", "C"]}, "nelements":{"$eq":2} }, properties=prop)
# data = mpr.query({ "elements":{"$all":["Si", "C"]}, "nelements":{"$lte":2} }, properties=prop)

# wildcard 通配符
# data = mpr.query("**S3", properties=prop)

# semiconductors for band gap prediction.
# data = mpr.query({ "elements":{"$in":["Al", "N", "P", "As", "Sb"], "$all":["Al"]}, "nelements":{"$lte":2},"band_gap":{"$gt":0}}, properties=prop)
# data = mpr.query({ "elements":{"$in":["Ga", "N", "P", "As", "Sb"], "$all":["Ga"]}, "nelements":{"$lte":2},"band_gap":{"$gt":0}}, properties=prop)
# data += mpr.query({ "elements":{"$in":["In", "N", "P", "As", "Sb"], "$all":["In"]}, "nelements":{"$lte":2},"band_gap":{"$gt":0}}, properties=prop)

for d in data:
    print(d)
    # print(f"{d['pretty_formula']}   {d['spacegroup.symbol']}   {d['band_gap']:.2}")

print('total number of records: ', len(data))
