# Introduction to 2D Array
Two-dimensional array: It is an array also consists of a sequence of elements. However, the elements are laid out in a **retangula grid** rather than a line. 

## Example of 2D Array
``` Python
def printArray(arr):
    for a in arr:
        print(a)

if __name__ == "__main__":
    a = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
    printArray(a)
```
```bash
[1, 1, 1]
[2, 2, 2]
[3, 3, 3]
```

## Principle
For some languages, the multi-dimensional array is **implemented internally as one-dimensional array** while for some languages, there is **no multidimensional array** at all.  
1. C++, stores the 2d-array as 1d-array
    * **A[i][j]** is equal to **A[i*N+j]**
2. Java, 2D-array is actually a 1D-array which contains M elements, where each M contains an array of N integers.

## Dynamic 2D Array
Dynamic 2D Array is a **nested dynamic array**.