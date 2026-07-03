import numpy as np

def generate_coordinates(length):

    return np.random.rand(length,3)

def refine_structure(coords):

    for i in range(10):

        noise=np.random.normal(0,0.01,coords.shape)

        coords+=noise

    return coords