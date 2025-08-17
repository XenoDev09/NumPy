# Installing numpy as pip install numpy

"""
ndarray:

N-Dimentional Array allows to store and manipulate large amount of data efficiently.
All the elements in an ndarray must be of same type making it homogeneous array.
This structure supports multiple dimentions which makes it ideal for handling complex
datasets like those used in scientific computing or data analysis.
With that we can perform fast and memory efficient operations on data.

"""


import numpy as np

x = np.array([1,2,3]) # 1D array

y = np.array([[1,2],
              [3,4]]) # 2D array

z = np.array([[[1,2],[3,4]],
              [[5,6],[7,8]]]) # 3D array

print("Printing 1D array:",x)
print("Printing 2D array:",y)
print("Printing 3D array:",z)

"""
ATTRIBUTES OF NDarray:
1. ndarray.shape : Returns a tuple representing shape of the array 
2. ndarray.ndim : Returns the number of dimentions(axes) of the array
3. ndarray.size : Returns the total number of elements in the array
4. ndarray.dtype : Returns the data type of the array elements
5. ndarray.itemsize : Returns the size in bytes of each element
"""

arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

print(arr)
print("shape:",arr.shape) # Row and Column
print("Dimentions:",arr.ndim)
print("Size:",arr.size)
print("Data Type:",arr.dtype)
print("Item Size:",arr.itemsize)

"""
SHAPE ATTRIBUTE : Syntax: numpy.shape(array_name) 
                  Parameters: Array is passed as a Parameter. 
                  Return: A tuple whose elements give the lengths of the corresponding array dimensions.
1. Normal Shape like above example:
2. Shape of Array Using ndim
3. Shape of Array of Tuples
"""
# 2. Shape of Array using ndim

a = np.array([2,4,6,8,10],ndmin=6)
print(a)
print("Shape:",a.shape)

# 3. Shape of Array of Tuples

b = np.array([(1,2),(3,4),(5,6),(7,8)])
print(b)
print("shape:",b.shape)

"""
NDIM ATTRIBUTE: 

Syntax  :  numpy.ndarray.ndim(arr)
Parameters : 
arr   : [array_like] Input array. If it is not already an ndarray, a conversion is attempted.
Return  : [int] Return the number of dimensions in arr.
"""


"""
SIZE ATTRIBUTE:
Syntax:
numpy.size(arr, axis=None)
Where: 
arr is input data in the form of an array.
axis represent along which the elements (rows or columns) are counted.
The function returns an integer as an output representing the number of elements. 
"""
#1. To Find Total Number of Elements

#2. To Count the Elements Along a Specific Axis
c = np.array([[1,2,3,4],
              [5,6,7,8]])
print(np.size(c,0)) # 0 represents axis as rows
print(np.size(c,1)) # 1 represents axis as columns

#   3. To Count Elements in a 3D Array
d = np.array([[[1,2],[3,4]],
              [[5,6],[7,8]]]) #shape (2,2,2)
print(np.size(d))
print(np.size(d,0)) # axis=0 refers to the number of blocks(first level of depth)
print(np.size(d,1)) # axis=1 refers to the number of rows in each block
print(np.size(d,2)) # axis=2 refers to the number of columns in each row


"""
dtype Attribute:
This attribute is read-only and cannot be modified directly.
Syntax: numpy.ndarray.dtype 
Parameters : None 
Return : [numpy dtype object] Return the data-type of the array’s elements.
"""

"""
itemsize Attribute:
Syntax :  numpy.ndarray.itemsize(arr)
Parameters : 
arr   : [array_like] Input array. 
Return  : [int] The length of one array element in bytes
"""

e = np.array([1, 2, 3, 4], dtype = np.float64)
print (e.itemsize)

f = np.array([1, 2, 3, 4],  dtype = np.complex128)
print (f.itemsize)