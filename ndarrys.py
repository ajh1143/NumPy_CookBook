import numpy as np

def create_ndarray(values):
    """
    Generate and return and ndarray
    :param values: List of values to be added to ndarray
    :return: NumPy Multidimensional array
    """
    generated_ndarray = np.array(values)
    return generated_ndarray


def find_shape(arr):
    """
    Find and print the shape of given ndarray parameter
    :param arr: Multidimensional array object
    :return: None
    """
    show_shape = arr.shape
    print(f"This array is of shape: {show_shape}")
    return None

