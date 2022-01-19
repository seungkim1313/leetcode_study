# Introduction to String
**String** is an array of **characters**.

## Intro
- Basic Operations for **string**.
- Difference between **comparison** functions.
- Is string **immutable**?
- Solve string-related problems

## Compare Function
**Question**: Can we use '==' to compare two *strings*?  
**Answer**: It depends on the languages. If it supports *operator overloading*.  
- For example, Java, we may not use '==' to compare two strings. Because it will actually compare whether these two objects are the same object. However, C++, we may use '==' to compare. 

## Immutable or Mutable
**Immutable** means you cannot chnage the content of the string once it is initialized. So is **String** Immutable? For some language, yes. 
- For example, Java, string is **mutable**. So you may not modify string once it is initialized. However, C++, you can modify the string just like you did with *array*. 

## Extra Operations
```JAVA
public class Main{
    public static void main(String[] args) {
        String s1 = "Hello World";
        // concatenate
        s1 += "!";
        // search(find)
        temp = s1.indexOf('o');
        temp = s1.lastIndexOf('o');
        // substring
        temp = s1.substring(6, 11);
    }
}
```