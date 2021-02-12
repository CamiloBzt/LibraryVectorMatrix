import unittest
import numpy as np
import library as cvm

# Vectors
a = np.array([5 + 1j, 3 + 10j, 2 + 2j])
b = np.array([1 + 1j, 1 + 1j, 1 + 1j])
c = np.array([[4 + 3j], [6 - 4j], [12 - 7j], [13j]])

# Matrix
a1 = np.array([[2 + 3j, 4 + 1j], [3 + 1j, 1 + 2j]])
b1 = np.array([[3 + 2j, 5 + 1j], [2 + 1j, 4 + 2j]])
c1 = np.array([[1 + 1j, 1 + 1j], [1 + 1j, 1 + 1j]])
matrix = np.array([[2 / 3, (-2 + 1j) / 3], [(2 + 1j) / 3, 2 / 3]])
matrix2 = np.array([[7, 6 + 5j], [6 - 5j, -3]])


class TestStringMethods(unittest.TestCase):

    def test_add(self):
        addP, addNP = cvm.addVect(a, b), np.add(a, b)
        self.assertEqual(addP.all(), addNP.all())
        addP, addNP = cvm.addMatrix(a1, b1), np.add(a1, b1)
        self.assertEqual(addP.all(), addNP.all())

    def test_sub(self):
        subsP, subsNP = cvm.inversVect(a, b), np.subtract(a, b)
        self.assertEqual(subsP.all(), subsNP.all())

    def test_escalar(self):
        escalarP, escalarNP = cvm.escalarVect(2, b), b * 2
        self.assertEqual(escalarP.all(), escalarNP.all())

    def test_transp(self):
        traspP, traspNP = cvm.transpV(a), np.transpose(a)
        self.assertEqual(traspP.all(), traspNP.all())
        traspP, traspNP = cvm.transpM(a1), np.transpose(a1)
        self.assertEqual(traspP.all(), traspNP.all())

    def test_dag(self):
        dagP, dagNP = cvm.dagV(a), np.array([[5. - 1.j], [3. - 10.j], [2. - 2.j]])
        self.assertEqual(dagP.all(), dagNP.all())
        dagP, dagNP = cvm.dagM(a1), np.array([[2. - 3.j, 3. - 1.j], [4. - 1.j, 1. - 2.j]])
        self.assertEqual(dagP.all(), dagNP.all())

    def test_mult(self):
        multP, multNP = cvm.multMatrix(a1, b1), a1 * b1
        self.assertEqual(multP.all(), multNP.all())

    def test_productInter(self):
        self.assertEqual(cvm.productoInterno(a, b), (-3 - 23j))

    def test_norm(self):
        self.assertEqual(cvm.normVect(c), np.linalg.norm(c))

    def test_unitary(self):
        self.assertTrue(cvm.unitary(matrix))

    def test_hermitian(self):
        self.assertTrue(cvm.hermitian(matrix2))

    def test_productTensor(self):
        tensorP, tensorNP = cvm.producTensorVect(b, a), np.array([[6. + 4.j, 13. - 7.j, 4. + 0.j],
                                                                  [6. + 4.j, 13. - 7.j, 4. + 0.j],
                                                                  [6. + 4.j, 13. - 7.j, 4. + 0.j]])
        self.assertTrue(np.testing.assert_almost_equal(tensorP, tensorNP) is None)
        tensorP, tensorNP = cvm.producTensorMatrix(c1, a1), np.array(
            [[5. - 1.j, 5. + 3.j, 4. + 2.j, 3. - 1.j, 5. - 1.j, 5. + 3.j, 4. + 2.j, 3. - 1.j]
                , [5. - 1.j, 5. + 3.j, 4. + 2.j, 3. - 1.j, 5. - 1.j, 5. + 3.j, 4. + 2.j, 3. - 1.j]])
        self.assertTrue(np.testing.assert_almost_equal(tensorP, tensorNP) is None)


if __name__ == '__main__':
    unittest.main()

"""print(a)
cvm.conjugV(a)
print(a)
print(a1)
cvm.conjugM(a1)
print(a1)"""
