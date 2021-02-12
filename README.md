# LibraryVectorMatrix


This project has some different functions to perform some operations between complex numbers, vectors and matrix.

### Complex Vectors
- Additions.
- Additive inverse.
- Multiplication of a scalar.
- Norm.
- Inner product.
- Distance.

```
a = np.array([complex_number, complex_number]) (Vector)
b = np.array([complex_number, complex_number]) (Vector)
e = scalar
function(a, b) (Operations between vectors)
function(e,a) (Operations between vectors and scalars)
```

### Complex Matrix
- Addition.
- Additive inverse.
- Multiplication of a scalar.
- Product.
- Verify that a matrix is unitary.
- Verify that a matrix is hermitian.

```
a = np.array([[complex_number, complex_number], [complex_number, complex_number]]) (Matrix)
b = np.array([[complex_number, complex_number], [complex_number, complex_number]]) (Matrix)
e = scalar
function(a, b) (Operations between matrix)
function(e, a) (Operations between matrix and scalars)
```

### Functions for complex Matrix Vectors and Matrix
- Transpose.
- Conjugated.
- Adjoint.
- Action.
- Tensor product.


##Here are some examples:
####Vectors
```
a = np.array([5 + 1j, 3 + 10j, 2 + 2j])
b = np.array([1 + 1j, 1 + 1j, 1 + 1j])
c = addVect(a, b)
transpose_a = transpV(a)
```
###Matrix
```
a = np.array([[2 + 3j, 4 + 1j], [3 + 1j, 1 + 2j]])
b = np.array([[3 + 2j, 5 + 1j], [2 + 1j, 4 + 2j]])
c = addMatrix(a, b)
transpose_a = transpM(a)
```

## Getting Started

- You have to clone this library for using it in your PC.
- Then you have to move it to the folder you want.
- Cloning the library

You have to write this in your Git cmd (If you do not have Git on your computer you can install it [Here](https://git-scm.com/))
```git bash
$ git clone https://github.com/CamiloBzt/LibraryVectorMatrix.git
```

In this moment you will have the repository in your PC

### Prerequisites

- You will need to have instaled Python 3.8 in your computer

Here is a link where you can download and install it:

[Python Official Page](https://python.org/)

- Be sure you have the library is in the same folder of the project you want to implement it.


## Running the tests

For running the predetermined test you have to open the file **unitTest.py** and then just run it, then it will show you the results from the tests.


## Built With

* [Python 3.8](https://python.org/) - Python


## Authors

* **Juan Camilo Bazurto Arias** - *Systems Engineering Student* - [Linkedin](https://www.linkedin.com/in/juan-camilo-b-b65379105/) - [GitHub](https://github.com/CamiloBzt)