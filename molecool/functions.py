import numpy as np

"""Provide the primary functions."""

def open_pdb(file_location):
    with open(file_location) as f:
        data = f.readlines()
    coordinates = []
    symbols = []
    for line in data:
        if 'ATOM' in line[0:6] or 'HETATM' in line[0:6]:
            symbols.append(line[76:79].strip())
            atom_coords = [float(x) for x in line[30:55].split()]
            coordinates.append(atom_coords)
    coords = np.array(coordinates)
    return symbols, coords


def write_xyz(file_location, symbols, coordinates):
    
    ## Write an xyz file given a file location, symbols, and coordinates.
    num_atoms = len(symbols)
    
    if num_atoms != len(coordinates):
        raise ValueError(f"write_xyz : the number of symbols ({num_atoms}) and number of coordinates ({len(coordinates)}) must be the same to write xyz file!")
    
    with open(file_location, 'w+') as f:
        f.write('{}\n'.format(num_atoms))
        f.write('XYZ file\n')
        
        for i in range(num_atoms):
            f.write('{}\t{}\t{}\t{}\n'.format(symbols[i], 
                                              coordinates[i,0], coordinates[i,1], coordinates[i,2]))
            

def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format).

    Replace this function and doc string for your own project.

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from.

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution.
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
