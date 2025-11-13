import numpy as np
from scipy import integrate

def calculate_double_integral():
    def f1(y, x):
        return x**2 + y**2
    
    result1, error1 = integrate.dblquad(f1, 0, 1, lambda x: 0, lambda x: 1)
    
    def f2(y, x):
        return np.sin(x) * np.cos(y)
    
    result2, error2 = integrate.dblquad(f2, 0, np.pi/2, lambda x: 0, lambda x: np.pi/2)
    
    print(f"∫∫(x² + y²) dx dy = {result1:.4f}")
    print(f"∫∫sin(x)cos(y) dx dy = {result2:.4f}")

if __name__ == "__main__":
    calculate_double_integral()