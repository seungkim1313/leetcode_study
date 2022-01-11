# Introduction to Array  
Understand Array and Dynamic Array

## Intro  
Followings are questions that need to be covered: 
- what's the difference? **array** and **dynamic array**
- what's the corresponding **built-in data structure** of array and dynamic array?
- **basic operations** of array and dynamic array. It convers: 
    - intialization 
    - data access 
    - modification
    - iteration
    - sort 
    - addition 
    - deletion
    - etc.  


## Note  
**Array**: It's a data structure to **sequentially store a collection of elements**. All elements can be **accessed randomly**. Why? Since each elemnet in the array can be identified by an array **index**.  
- **'accessed randomly'** -> **'random access'** means you can access any array element by its index in **O(1)** time. 
- An array has **a fixed capacity**. It requires user to specify the size during initialization.
- In JAVA,
```JAVA
public class Main {
    public static void main(String[] args) {
        // initialize
        int[] a0 = new int[5];
        int[] a1 = {1, 2, 3};
        // get length
        int length = a1.length;
        // access
        int temp = a1[0];
        // modification
        a1[0] = 4;
        // sort
        Arrays.sort(a1)
    }
}
```

**Dimensions for array**: An array can have one or more dimensions. 
- **one-dimensional array**, also known as **linear array**. 

**Dynamic Array**: It's a **random access** list data structure with **variable size**.  
- **variable size** means **size** is not known during compile time.
- In JAVA, **ArrayList**
```JAVA
public class Main {
    public static void main(String[] args) {
        // initialize
        List<Integer> v0 = new ArrayList<>();
        List<Integer> v1;
        // casting
        Integer[] a = {0, 1, 2, 3, 4};
        v1 = new ArrayList<>(Arrays.asList(a));
        // copy
        List<Integer> v2 = v1;
        List<Integer> v3 = new ArrayList<>(v1);
        // access
        int temp = v1.get(0)
        // iteration
        for (int 1=0; i<v1.size(); ++i) {
            // v1.size() -> get length
            System.out.print(v1.get(i));
        }
        for (int item:v1) {
            System.out.print(item);
        }
        // modification
        v2.set(0, 5);    // v2 is a reference of v1, so v1 will change
        v3.set(0, -1);   // v3 is not a reference of v1, so v1 will not change
        // sort
        Collections.sort(v1);
        // add
        v1.add(-1);
        v1.add(1, 6);
        // delete
        v1.remove(v1.size() - 1);   // this will remove the last element
    }
}
```
- In C++, **vector**




