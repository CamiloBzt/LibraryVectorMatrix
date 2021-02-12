import numpy as np


def addVect(a, b):
    if a.shape == b.shape:
        c = []
        for i in range(len(a)):
            c.append(a[i] + b[i])
        c = np.array(c)
        return c

    else:
        return None


def inversVect(a, b):
    if a.shape == b.shape:
        c = []
        for i in range(len(a)):
            c.append(a[i] - b[i])
        c = np.array(c)
        return c

    else:
        return None


def escalarVect(e, a):
    c = []
    for i in range(len(a)):
        c.append(e * a[i])
    c = np.array(c)
    return c


def addMatrix(a, b):
    if a.shape == b.shape:
        c = [[] for k in range(len(a))]
        for i in range(len(a)):
            for j in range(len(a[i])):
                c[i].append(a[i][j] + b[i][j])
        c = np.array(c)
        return c

    else:
        return None


def transpV(a):
    c = [[] for i in range(len(a))]
    for i in range(len(a)):
        c[i].append(a[i])
    c = np.array(c)
    return c


def transpM(a):
    c = []
    for i in range(a.shape[1]):
        fila = []
        for j in range(len(a)):
            fila.append(a[j][i])
        c.append(fila)
    c = np.array(c)
    return c


def conjugV(a):
    for i in range(len(a)):
        a[i] = complex(a[i].real, a[i].imag * (-1))


def conjugM(a):
    for i in range(len(a)):
        conjugV(a[i])


def dagV(a):
    conjugV(a)
    return transpV(a)


def dagM(a):
    conjugM(a)
    return transpM(a)


def multVect(a, b):
    total = 0
    for i in range(len(a)):
        num = a[i] * b[i]
        total = total + num
    return total


def multMatrix(a, b):
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
    if a.shape == b.shape:
        total = 0
        for i in range(len(a)):
            total += a[i] * complex(b[i].real, b[i].imag * (-1))
        return total


def normVect(a):
    return np.math.sqrt(productoInterno(a, a).real)


def distanceVect(a, b):
    c = inversVect(a, b)
    return normVect(c)


def unitary(a):
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
    matrix = np.array(a)
    adj = dagM(a)
    val = True
    for i in range(len(a)):
        for j in range(len(a[i])):
            if matrix[i][j] != adj[i][j]:
                val = False
    return val


def producTensorVect(a, b):
    c = []
    for i in range(len(a)):
        c.append(escalarVect(a[i], b))
    c = np.array(c)
    return c


def producTensorMatrix(a, b):
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