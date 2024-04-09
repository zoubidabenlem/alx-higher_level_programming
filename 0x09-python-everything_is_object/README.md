# 0x09-python-everything_is_object

> This project is a little bit different than the usual projects. The first part is only questions about Python's specificity like *"What would be the result of ..."*. You should read all documentation first (as usual :)), then take the time to think and brainstorm with your peers about what you think and why. Try to do this without coding anything for a few hours.
> First read, then think, then brainstorm together. Only then you can test in the interpreter.
> It's important that you truly understand the reasons behind the answers of all those tasks so that you can apply the same logic to other variables and other variable types.
> Note that during interviews for Python positions, you will most likely have to answer to these type of questions.
> All your answers should be only one line in a file. No space before or after the answer.

---

### 0. Who am I?

What function would you use to get the type of an object?

Write the name of the function in the file, without ().

---

### 1. Where are you?

How do you get the variable identifier (which is the memory address in the CPython implementation)?

Write the name of the function in the file, without ().

---

### 2. Right count

In the following code, do a and b point to the same object? Answer with Yes or No.

	>>> a = 89
	>>> b = 100

---

### 3. Right count =

In the following code, do a and b point to the same object? Answer with Yes or No.

	>>> a = 89
	>>> b = 89

---

### 4. Right count =
	
In the following code, do a and b point to the same object? Answer with Yes or No.

	>>> a = 89
	>>> b = a

---

### 5. Right count =+

In the following code, do a and b point to the same object? Answer with Yes or No.

	>>> a = 89
	>>> b = a + 1

---

### 6. Is equal

What do these 3 lines print?

	>>> s1 = "Best School"
	>>> s2 = s1
	>>> print(s1 == s2)

---

### 7. Is the same

What do these 3 lines print?

	>>> s1 = "Best"
	>>> s2 = s1
	>>> print(s1 is s2)

---

### 8. Is really equal

What do these 3 lines print?

	>>> s1 = "Best School"
	>>> s2 = "Best School"
	>>> print(s1 == s2)

---

### 9. Is really the same

What do these 3 lines print?

	>>> s1 = "Best School"
	>>> s2 = "Best School"
	>>> print(s1 is s2)

---

### 10. And with a list, is it equal

What do these 3 lines print?

	>>> l1 = [1, 2, 3]
	>>> l2 = [1, 2, 3] 
	>>> print(l1 == l2)

---

### 11. And with a list, is it the same

What do these 3 lines print?

	>>> l1 = [1, 2, 3]
	>>> l2 = [1, 2, 3] 
	>>> print(l1 is l2)

---

### 12. And with a list, is it really equal

What do these 3 lines print?

	>>> l1 = [1, 2, 3]
	>>> l2 = l1
	>>> print(l1 == l2)

### 13. And with a list, is it really the same

What do these 3 lines print?

	>>> l1 = [1, 2, 3]
	>>> l2 = l1
	>>> print(l1 is l2)

---

### 14. List append

What does this script print?

	>>> l1 = [1, 2, 3]
	>>> l2 = l1
	>>> l1.append(4)
	>>> print(l2)

---

### 15. List add

What does this script print?

	>>> l1 = [1, 2, 3]
	>>> l2 = l1
	>>> l1 = l1 + [4]
	>>> print(l2)

---

### 16. Integer incrementation

What does this script print?

	def increment(n):
    	    n += 1

	a = 1
	increment(a)
	print(a)

---

### 17. List incrementation

What does this script print?

	def increment(n):
	    n.append(4)

	l = [1, 2, 3]
	increment(l)
	print(l)

---

### 18. List assignation

What does this script print?

	def assign_value(n, v):
	    n = v

	l1 = [1, 2, 3]
	l2 = [4, 5, 6]
	assign_value(l1, l2)
	print(l1)

---

### 19. Copy a list object

Write a function def copy_list(l): that returns a copy of a list.

- The input list can contain any type of objects
- Your file should be maximum 3-line long (no documentation needed)
- You are not allowed to import any module

---

### 20. Tuple or not?

	a = ()

Is a a tuple? Answer with Yes or No.

---

### 21. Tuple or not?

	a = (1, 2)

Is a a tuple? Answer with Yes or No.

---

### 22. Tuple or not?

	a = (1)

Is a a tuple? Answer with Yes or No.

---

### 23. Tuple or not?

	a = (1, )

Is a a tuple? Answer with Yes or No.

---

### 24. Who I am?

What does this script print?

	a = (1)
	b = (1)
	a is b

---

### 25. Tuple or not

What does this script print?

	a = (1, 2)
	b = (1, 2)
	a is b

---

### 26. Empty is not empty

What does this script print?

	a = ()
	b = ()
	a is b

---

### 27. Still the same?

	>>> id(a)
	139926795932424
	>>> a
	[1, 2, 3, 4]
	>>> a = a + [5]
	>>> id(a)

Will the last line of this script print `139926795932424` ? Answer with Yes or No.

---

### 28. Same or not?

	>>> a
	[1, 2, 3]
	>>> id (a)
	139926795932424
	>>> a += [4]
	>>> id(a)

Will the last line of this script print `139926795932424` ? Answer with Yes or No.

---

### 29. #pythonic
#advanced

Write a function magic_string() that returns a string “BestSchool” n times the number of the iteration (see code):

- Format: see example
- Your file should be maximum 4-line long (no documentation needed)
- You are not allowed to import any module
```
guillaume@ubuntu:~/0x09$ cat 100-main.py
#!/usr/bin/python3
magic_string = __import__('100-magic_string').magic_string
for i in range(10):
	print(magic_string())
guillaume@ubuntu:~/0x09$ ./100-main.py | cat -e
BestSchool$
BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
guillaume@ubuntu:~/0x09$ wc -l 100-magic_string.py
4 100-magic_string.py
```

---

