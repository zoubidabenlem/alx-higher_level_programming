#### Object Caching

```
>>> print("I")
>>> print("Love")
>>> print("Python")
```

> At first look, this code line appears to generate no int objects. However, this is not entirely correct. When the Python interpreter starts, int objects are pre-allocated for integers ranging from -5 to 256. Python does this to increase program efficiency by reusing int objects rather than creating new ones every time an integer is used in the code. As a result, all integers in this range are pre-allocated and cached in memory. Now, because the pre-allocated integer range is between -5 and 256, a total of 262 integers are pre-allocated. As a result, the number of int objects created before executing line 2 is 262.

