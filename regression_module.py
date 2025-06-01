import numpy as np
import numpy.polynomial.polynomial as poly

def polynomial_regression(x, y, degree):
    if len(x) != len(y):
        print("x and y must have the same length")
        return None
    if len(x) == 0:
        print("x and y must not be empty")
        return None
    if degree < 0:
        print("degree must be non-negative")
        return None
    if len(x) < degree + 1:
        print("x must have at least degree + 1 elements")
        return None
    
    X_matrix = np.vander(x, degree + 1, increasing=True)
    try:
        coef = np.linalg.lstsq(X_matrix, y, rcond=None)[0]
    except np.linalg.LinAlgError as e:
        print(f"Error: {e}")
        return None
    return coef

def polynomial_regression_value(x, coef):
    if coef is None:
        return None
    return poly.polyval(x, coef)