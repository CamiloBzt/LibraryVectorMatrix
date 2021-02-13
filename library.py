import numpy as np


def addVect(a, b):
    """
    This function returns add operation between vectors
    :param a: vector
    :param b: vector
    :return: vector
    """
    if a.shape == b.shape:
        c = []
        for i in range(len(a)):
            c.append(a[i] + b[i])
        c = np.array(c)
        return c

    else:
        return None


def inversVect(a, b):
    """
    This function returns subtract operation between vectors
    :param a: vector
    :param b: vector
    :return: vector
    """
    if a.shape == b.shape:
        c = []
        for i in range(len(a)):
            c.append(a[i] - b[i])
        c = np.array(c)
        return c

    else:
        return None


def escalarVect(e, a):
    """
    This function returns scalar multiplication operation between scalar and vector
    :param e: scalar
    :param a: vector
    :return: vector
    """
    c = []
    for i in range(len(a)):
        c.append(e * a[i])
    c = np.array(c)
    return c


def addMatrix(a, b):
    """
    This function returns add operation between matrix
    :param a: matrix
    :param b: matrix
    :return: matrix
    """
    if a.shape == b.shape:
        c = [[] for k in range(len(a))]
        for i in range(len(a)):
            for j in range(len(a[i])):
                c[i].append(a[i][j] + b[i][j])
        c = np.array(c)
        return c

    else:
        return None


def inverseMatrix(a, b):
    """
    This function returns subtract operation between matrix
    :param a: matrix
    :param b: matrix
    :return: matrix
    """
    if a.shape == b.shape:
        c = [[] for k in range(len(a))]
        for i in range(len(a)):
            for j in range(len(a[i])):
                c[i].append(a[i][j] - b[i][j])
        c = np.array(c)
        return c

    else:
        return None


def escalarMatrix(e, a):
    """
    This function returnss scalar multiplication operation between scalar and matrix
    :param e: scalar
    :param a: matrix
    :return: matrix
    """
    c = []
    for i in range(len(a)):
        fila = []
        for j in range(len(a[i])):
            fila.append(e * a[i])
        c.append(fila)
    c = np.array(c)
    return c


def transpV(a):
    """
    This function returns transpose operation in a vector
    :param a: vector
    :return: vector
    """
    c = [[] for i in range(len(a))]
    for i in range(len(a)):
        c[i].append(a[i])
    c = np.array(c)
    return c


def transpM(a):
    """
    This function returns transpose operation in a matrix
    :param a: matrix
    :return: matrix
    """
    c = []
    for i in range(a.shape[1]):
        fila = []
        for j in range(len(a)):
            fila.append(a[j][i])
        c.append(fila)
    c = np.array(c)
    return c


def conjugV(a):
    """
    This function returns conjugate operation in a vector
    :param a:vector
    """
    for i in range(len(a)):
        a[i] = complex(a[i].real, a[i].imag * (-1))


def conjugM(a):
    """
    This function returns conjugate operation in a matrix
    :param a: matrix
    """
    for i in range(len(a)):
        conjugV(a[i])


def dagV(a):
    """
    This function returns adjoint operation in a vector
    :param a: vector
    :return: vector
    """
    conjugV(a)
    return transpV(a)


def dagM(a):
    """
    This function returns adjoint operation in a matrix
    :param a: matrix
    :return: matrix
    """
    conjugM(a)
    return transpM(a)


def multVect(a, b):
    """
    This function returns multiplicative operation between vectors
    :param a: vector
    :param b: vector
    :return: vector
    """
    total = 0
    for i in range(len(a)):
        num = a[i] * b[i]
        total = total + num
    return total


def multMatrix(a, b):
    """
    This function returns multiplicative operation between matrix
    :param a: matrix
    :param b: matrix
    :return: matrix
    """
    if a.shape[1] == b.shape[0]:
        matrix = []
        for i in range(len(a)):
            fila = []
            for j in range(len(a[i])):
                col = b[:, j]
                fila.append(multVect(a[i], col))
            matrix.append(fila)
        matrix = np.array(matrix)
        return matrix

    else:
        return None


def productoInterno(a, b):
    """
    This function returns inner product operation between vectors
    :param a: vector
    :param b: vector
    :return: vector
    """
    if a.shape == b.shape:
        total = 0
        for i in range(len(a)):
            total += a[i] * complex(b[i].real, b[i].imag * (-1))
        return total


def action(a, b):
    """
    This function returns the action of a matrix on a vector
    :param a: Vector
    :param b: Matrix
    :return: Array
    """
    return multVect(a, b)


def normVect(a):
    """
    This function returns norm operation of a vector
    :param a: vector
    :return: number
    """
    return np.math.sqrt(productoInterno(a, a).real)


def distanceVect(a, b):
    """
    This function returns the distance between vectors
    :param a: vector
    :param b: vector
    :return: number
    """
    c = inversVect(a, b)
    return normVect(c)


def unitary(a):
    """
    This function returns the boolean value of the verification of a unitary matrix
    :param a: Matrix
    :return: Boolean value
    """
    matrix = np.array(a)
    adj = dagM(a)
    mult = multMatrix(adj, matrix)
    mIdent = np.eye(mult.shape[0])
    val = True
    for i in range(len(mult)):
        for j in range(len(mult[i])):
            if mult[i][j] != mIdent[i][j]:
                val = False
    return val


def hermitian(a):
    """
    This function returns the boolean value of the verification of a hermitian matrix
    :param a: matrix
    :return: boolean value
    """
    matrix = np.array(a)
    adj = dagM(a)
    val = True
    for i in range(len(a)):
        for j in range(len(a[i])):
            if matrix[i][j] != adj[i][j]:
                val = False
    return val


def producTensorVect(a, b):
    """
    This function returns tensor product operation between vectors
    :param a: vector
    :param b: vector
    :return: vector
    """
    c = []
    for i in range(len(a)):
        c.append(escalarVect(a[i], b))
    c = np.array(c)
    return c


def producTensorMatrix(a, b):
    """
    This function returns tensor product operation between matrix
    :param a: matrix
    :param b: matrix
    :return: matrix
    """
    c = []
    for i in range(len(a)):
        fila = []
        for j in range(len(a[i])):
            productE = escalarVect(a[i][j], b)
            for k in range(len(productE)):
                for l in range(len(productE[k])):
                    fila.append(productE[k][l])
        c.append(fila)
    c = np.array(c)
    return c
