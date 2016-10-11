import numpy as np
from mendeleev import element
import glob


filename = 'Ti3SiC2.STRUCT_OUT'



def struct2xtl(filename):
    system = filename.split(sep='.')[0]
    latt_vectors = np.empty((3,3))
    with open(filename) as text_file:
        for i in range(3):
            latt_vect = text_file.readline().split()
            for j, x in enumerate(latt_vect):
                latt_vectors[i,j] = float(x)
        num_of_atoms = int(text_file.readline())
        atom_coords = np.empty((num_of_atoms, 3))
        atom_labels = []
        for i in range(num_of_atoms):
            atom = text_file.readline().split()
            atom_num = int(atom[1])
            atom_label = element(atom_num).symbol
            atom_labels.append(atom_label)
            for j, x in enumerate(atom[2:]):
                atom_coords[i, j] = float(x)

    ## Crystallographic Note
    # Convention for crystallographioc parameters is that
    # a unit cell (which must tesselate in 3D space) can be
    # defined by three scalar lengths and three angles
    # a, b, c and alpha, beta, gamma
    # alpha is the angle between the b and c vectors and so on. 
    # See Crystallography and Crystal Defects 
    # by Kelly and Knowles for further details

    a = np.linalg.norm(latt_vectors[0])
    b = np.linalg.norm(latt_vectors[1])
    c = np.linalg.norm(latt_vectors[2])

    alpha = np.arccos(np.dot(latt_vectors[1],latt_vectors[2])/(c*b))
    beta = np.arccos(np.dot(latt_vectors[0],latt_vectors[2])/(a*c))
    gamma = np.arccos(np.dot(latt_vectors[0],latt_vectors[1])/(a*b))

    latt_params = np.empty(6,)
    latt_params[0] = a
    latt_params[1] = b
    latt_params[2] = c
    latt_params[3] = np.degrees(alpha)
    latt_params[4] = np.degrees(beta)
    latt_params[5] = np.degrees(gamma)

    latt_params = tuple(latt_params)
    title = 'TITLE ' + system + '\n'
    unit_cell = ('CELL\n'
                 +'{:g} {:g} {:g} {:g} {:g} {:g}\n'.format(*latt_params)
                 +'SYMMETRY NUMBER 1 \n'
                 +'SYMETTRY LABEL P1 \n')
    atoms = 'ATOMS\nNAME         X          Y        Z\n'
    for i, label in enumerate(atom_labels):
        atom = label + ' {:g} {:g}  {:g}\n'.format(*atom_coords[i])
        atoms += atom

    text = title + unit_cell + atoms
    with open( system + '.xtl', 'wt') as file:
        file.write(text)
    print(text)
    print('\n #########################\n '
          +'Saved xtl to file.')
    
for filename in glob.iglob('*.STRUCT_OUT'):
    struct2xtl(filename)
