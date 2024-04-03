# 0x05. Python - Exceptions
---
## 0-safe_print_list.py

#### Write a function that prints x elements of a list.

> Prototype: def safe_print_list(my_list=[], x=0):
- my_list can contain any type (integer, string, etc.)
- All elements must be printed on the same line followed by a new line.
- x represents the number of elements to print
- x can be bigger than the length of my_list
> Returns the real number of elements printed
1. You have to use try: / except:
2. You are not allowed to import any module
3. You are not allowed to use len()

---

## 1-safe_print_integer.py

#### Write a function that prints an integer with "{:d}".format().

> Prototype: def safe_print_integer(value):
- value can be any type (integer, string, etc.)
- The integer should be printed followed by a new line
> Returns True if value has been correctly printed (it means the value is an integer)Otherwise, returns False
1. You have to use try: / except:
2. You have to use "{:d}".format() to print as integer
3. You are not allowed to import any module
4. You are not allowed to use type()

---

## 2-safe_print_list_integers.py

#### Write a function that prints the first x elements of a list and only integers.

> Prototype: def safe_print_list_integers(my_list=[], x=0):
- my_list can contain any type (integer, string, etc.)
- All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
- x represents the number of elements to access in my_list
- x can be bigger than the length of my_list - if it's the case, an exception is expected to occur
> Returns the real number of integers printed
1. You have to use try: / except:
2. You have to use "{:d}".format() to print an integer
3. You are not allowed to import any module
4. You are not allowed to use len()

---

## 3-safe_print_division.py

#### Write a function that divides 2 integers and prints the result.

> Prototype: def safe_print_division(a, b):
- You can assume that a and b are integers
- The result of the division should print on the finally: section preceded by Inside result:
> Returns the value of the division, otherwise: None
1. You have to use try: / except: / finally:
2. You have to use "{}".format() to print the result
3. You are not allowed to import any module

---

## 4-list_division.py

#### Write a function that divides element by element 2 lists.

> Prototype: def list_division(my_list_1, my_list_2, list_length):
- my_list_1 and my_list_2 can contain any type (integer, string, etc.)
- list_length can be bigger than the length of both lists
> Returns a new list (length = list_length) with all divisions
- If 2 elements cant be divided, the division result should be equal to 0
- If an element is not an integer or float:
	-> print: wrong type
- If the division can't be done (/0):
	-> print: division by 0
- If my_list_1 or my_list_2 is too short
	-> print: out of range
1. You have to use try: / except: / finally:
2. You are not allowed to import any module

---

## 5-raise_exception.py

#### Write a function that raises a type exception.

> Prototype: def raise_exception():
- You are not allowed to import any module

---

## 6-raise_exception_msg.py

#### Write a function that raises a name exception with a message.

> Prototype: def raise_exception_msg(message=""):
- You are not allowed to import any module

---

## 100-safe_print_integer_err.py

### Write a function that prints an integer.

> Prototype: def safe_print_integer_err(value):
- value can be any type (integer, string, etc.)
- The integer should be printed followed by a new line
> Returns True if value has been correctly printed (it means the value is an integer) Otherwise, returns False and prints in stderr the error precede by Exception:
1. You have to use try: / except:
2. You have to use "{:d}".format() to print as integer
3. You are not allowed to use type()

---

## 101-safe_function.py

### Write a function that executes a function safely.

>Prototype: def safe_function(fct, *args):
- You can assume fct will be always a pointer to a function
> Returns the result of the function, Otherwise, returns None if something happens during the function and prints in stderr the error precede by Exception:
- You have to use try: / except:

---
