# 0x0A. Python - Inheritance

One of the core concepts in object-oriented programming (OOP) languages is inheritance. It is a mechanism that allows you to create a hierarchy of classes that share a set of properties and methods by deriving a class from another class. Inheritance is the capability of one class to derive or inherit the properties from another class.

---

# Tasks

This repository contains Python scripts and classes focused on the concept of inheritance and object-oriented programming.

## Task <span style="color:blue">0: Lookup</span>

> File: <span style="color:green">0-lookup.py</span>

The task involves creating a function lookup that returns a list of available attributes and methods of an object. The function does not rely on importing any modules and provides insight into the structure of objects in Python.

## Task <span style="color:blue">1: My List</span>

> File: <span style="color:green">1-my_list.py</span>

In this task, a class MyList is created which inherits from the built-in list class. It introduces a public instance method print_sorted that prints the list in sorted order.

## Task <span style="color:blue">2: Exact Same Object</span>

> File: <span style="color:green">2-is_same_class.py</span>

The objective here is to implement a function is_same_class that determines if an object is exactly an instance of a specified class.

## Task <span style="color:blue">3: Same Class or Inherit From</span>

> File: <span style="color:green">3-is_kind_of_class.py</span>

This task involves writing a function is_kind_of_class that checks if an object is an instance of, or if it is derived from, a specified class.

## Task <span style="color:blue">4: Only Sub Class Of</span>

> File: <span style="color:green">4-inherits_from.py</span>

Here, a function inherits_from is developed to determine if an object is an instance of a class that inherits (directly or indirectly) from a specified class.

## Task <span style="color:blue">5: Geometry Module</span>

> File: <span style="color:green">5-base_geometry.py</span>

An empty class BaseGeometry is created as a foundation for geometric classes. This task lays the groundwork for subsequent tasks involving geometric shapes.

## Task <span style="color:blue">6: Improve Geometry</span>

> File: <span style="color:green">6-base_geometry.py</span>

Building upon Task 5, the BaseGeometry class is enhanced with a public instance method area that raises an Exception indicating that the method is not implemented. This sets the stage for subclasses to implement their own area calculation methods.

## Task <span style="color:blue">7: Integer Validator</span>

> File: <span style="color:green">7-base_geometry.py</span>

Extending the BaseGeometry class, a public instance method integer_validator is added to validate integer values, raising appropriate exceptions for invalid input.

## Task <span style="color:blue">8: Rectangle</span>

> File: <span style="color:green">8-rectangle.py</span>

A class Rectangle is implemented, inheriting from BaseGeometry. It introduces instantiation with width and height, along with validation of positive integer inputs.

## Task <span style="color:blue">9: Full Rectangle</span>

> File: <span style="color:green">9-rectangle.py</span>

In this task, the Rectangle class is further refined to include the implementation of the area method and customized print and str representations.

## Task <span style="color:blue">10: Square #1</span>

> File: <span style="color:green">10-square.py</span>

A class Square is developed, inheriting from Rectangle, to represent square geometries. It implements instantiation with size and the area calculation method.

## Task <span style="color:blue">11: Square #2</span>

> File: <span style="color:green">11-square.py</span>

Building upon Task 10, the Square class is enhanced with customized print and str representations, distinguishing it as a square geometry.

