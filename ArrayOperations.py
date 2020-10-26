import numpy as np
#create 1-D numpy array
a = np.array([1,2,3])
a
#create 2-D numpy array
b = np.array([[1,2,3],[4,5,6]])
b

#get the number of elements in array
a.size
b.size

# get the shape of the array in rows,cols format
a.shape
b.shape

# get dimension of array
a.ndim
b.ndim

# get number of bytes (space) occupied by each element of array
b.itemsize

# get datatype of array
b.dtype

#create array with float datatype
f = np.array([[1,2,3],[4,5,6]], dtype=np.float64)
f

#create array with zeros initialized
x = np.zeros([2,2])
x
#create array with ones initialized
x = np.ones([2,3])
x
#create empty array
x = np.empty(5)
x
#create array using arange
x = np.arange(5)
x
#specify intervals in arange
x = np.arange(1,10,2)
x
# re-shape the array
b= b.reshape(3,2)
b
#flatten the array
c = b.ravel()
c
# get the largest number in the array
b.max()
# get the smallest number in the array
b.min()
#sum up all the elements of array
b.sum()
# sum along columns
b.sum(axis=0)
# sum along rows
b.sum(axis=1)

# find square root of each elements
np.sqrt(b)
#find standard deviation of array elements
np.std(b)

# add, subtract, multiply, divide and dot for two arrays
x = np.array([[1,1],[2,2]])
x
y = np.array([[1,1],[2,2]])
y
x+y
x-y
x*y
x/y
x.dot(y)













































