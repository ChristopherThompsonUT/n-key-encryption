message = 100
n = 5

import numpy as np
from fractions import Fraction



def inverse_matrix(A):
    """
    Computes the inverse of a matrix A using row reduction
    and ndarrays with object type Fractions.
    """
    n = A.shape[0]
    
    # Create an identity matrix with the same dimensions as A
    I = np.array([[Fraction(1, 1) if i == j else Fraction(0, 1) for j in range(n)] for i in range(n)])

    
    # Concatenate A and I to create an augmented matrix
    M = np.concatenate((A, I), axis=1, dtype=Fraction)

    
    
    # Perform row reduction on M
    for i in range(n):
        # Divide the ith row by the diagonal element
        div = M[i][i]
        M[i] = M[i] / div

        # Subtract the ith row from all other rows to eliminate the ith column
        for j in range(n):
            if i != j:
                sub = M[j][i]
                M[j] = M[j] - sub * M[i]

    # The inverse of A is the right half of the augmented matrix M
    A_inv = M[:, n:]

    return A_inv


x_invertable = False
while not x_invertable:
    x_values = [Fraction(ii) for ii in (-1)**np.random.randint(0, 2, n)*np.random.rand(n)*8]
    index = np.random.randint(n); 
    x_values[index]=Fraction(0,1)
    
    X = np.vander(x_values, increasing=True)
    for i in range(n):
        X[i][0]=Fraction(1,1)
    try:
        X_inverse = inverse_matrix(np.copy(X))
        x_invertable=True
    except:
        x_invertable=False
    
    

Y = np.array([Fraction(ii) for ii in np.random.rand(n)*8])

Y[index] = Fraction(message)

A = np.dot(X_inverse, Y)

for i in A:
    print(float(i))
    
random_value = Fraction((-1)**np.random.randint(0, 2)*np.random.rand()*8)
x_values[index] = random_value

Y[index] = sum([A[ii]*random_value**ii for ii in range(n)])


