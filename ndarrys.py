import numpy as np


def create_ndarray(values):
    """ Generate and return and ndarray
    :param values: List of values to be added to ndarray
    :return: NumPy Multidimensional array
    """
    generated_ndarray = np.array(values)
    return generated_ndarray


def find_shape(arr):
    """ Find and print the shape of given ndarray parameter
    :param arr: Multidimensional array object
    :return: None
    """
    show_shape = arr.shape
    print(f"This array is of shape: {show_shape}")
    return None


def vectorize_add(arr1, arr2):
    """ Vectorized addition of two arrays, return the result
    :param arr1: NumPy Array 1
    :param arr2: NumPy Array 2
    :return: Vectorized ndarray comprised of the addition of Array 1 and Array 2
    """
    result = arr1+arr2
    return result


def vectorize_subtract(arr1, arr2):
    """ Subtract an array from another, return result
    :param arr1: NumPy Array 1
    :param arr2: NumPy Array 2
    :return: Vectorized ndarray comprised of the addition of Array 1 and Array 2
    """
    result = arr1-arr2
    return result


def vectorize_multiply(arr1, arr2):
    """ Multiple two arrays
    :param arr1: NumPy Array 1
    :param arr2: NumPy Array 2
    :return: Vectorized ndarray comprised of the multiplaction of Array 1 and Array 2
    """
    result = arr1*arr2
    return result


def vectorize_exponential(arr1, value):
    """ Return a vectorized array of exponential results
    :param arr1: NumPy Array 1
    :param value: integer or float
    :return: Vectorized ndarray comprised of the exponentiation of Array 1 and parameter value
    """
    result = arr1**value
    return result


def array_slice(array, start, stop):
    """ Given an array, a start and stop point, return a sliced array
    :param array: NumPy ndarray
    :param start: Integer value defining start position to slice array
    :param stop: Integer value defining the end position to slice array
    :return sliced: The sliced ndarray
    """
    sliced = array[start:stop]
    return sliced
