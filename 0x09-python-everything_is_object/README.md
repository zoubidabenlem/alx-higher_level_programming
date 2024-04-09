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


