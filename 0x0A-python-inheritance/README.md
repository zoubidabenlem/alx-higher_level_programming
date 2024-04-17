# 0x0A. Python - Inheritance

One of the core concepts in object-oriented programming (OOP) languages is inheritance. It is a mechanism that allows you to create a hierarchy of classes that share a set of properties and methods by deriving a class from another class. Inheritance is the capability of one class to derive or inherit the properties from another class.
---

# Tasks

This repository contains Python scripts and classes focused on the concept of inheritance and object-oriented programming.

## Task `0`: Lookup

> File: [Â0-l](./0-lookup.py)

The task involves creating a function lookup that returns a list of available attributes and methods of an object. The function does not rely on importing any modules and provides insight into the structure of objects in Python.

## Task `1`: My List

> File: [1-my_list.py](./1-my_list.py)

In this task, a class MyList is created which inherits from the built-in list class. It introduces a public instance method print_sorted that prints the list in sorted order.

## Task `2`: Exact Same Object

> File: [2-is_same_class.py](./2-is_same_class.py)

The objective here is to implement a function is_same_class that determines if an object is exactly an instance of a specified class.

## Task `3`: Same Class or Inherit From

> File: [3-is_kind_of_class.py](./3-is_kind_of_class.py)

This task involves writing a function is_kind_of_class that checks if an object is an instance of, or if it is derived from, a specified class.

## Task `4`: Only Sub Class Of

> File: [4-inherits_from.py](./4-inherits_from.py)

Here, a function inherits_from is developed to determine if an object is an instance of a class that inherits (directly or indirectly) from a specified class.

## Task `5`: Geometry Module

> File: [5-base_geometry.py](./5-base_geometry.py)

An empty class BaseGeometry is created as a foundation for geometric classes. This task lays the groundwork for subsequent tasks involving geometric shapes.

## Task `6`: Improve Geometry

> File: [6-base_geometry.py](./6-base_geometry.py)

Building upon Task 5, the BaseGeometry class is enhanced with a public instance method area that raises an Exception indicating that the method is not implemented. This sets the stage for subclasses to implement their own area calculation methods.

## Task `7`: Integer Validator

> File: [7-base_geometry.py](./7-base_geometry.py)

Extending the BaseGeometry class, a public instance method integer_validator is added to validate integer values, raising appropriate exceptions for invalid input.

## Task `8`: Rectangle

> File: [8-rectangle.py](./8-rectangle.py)

A class Rectangle is implemented, inheriting from BaseGeometry. It introduces instantiation with width and height, along with validation of positive integer inputs.

## Task `9`: Full Rectangle

> File: [9-rectangle.py](./9-rectangle.py)

In this task, the Rectangle class is further refined to include the implementation of the area method and customized print and str representations.

## Task `10`: Square #1

> File: [10-square.py](./10-square.py)

A class Square is developed, inheriting from Rectangle, to represent square geometries. It implements instantiation with size and the area calculation method.

## Task `11`: Square #2

> File: [11-square.py](./11-square.py)

Building upon Task 10, the Square class is enhanced with customized print and str representations, distinguishing it as a square geometry.

## Task `12`:  My integer

> File: [`100-my_int.py`](./100-my_int.py)

class named ÂMyIntÂ that inherits from the built-in int class. However, there's a twist: MyInt behaves differently from a regular integer. Specifically, the == and != operators are inverted. That is, == returns False when the values are equal, and != returns True when the values are equal.

## Task `13`: Can I?

> File: [`101-add_attribute.py`](./101-add_attribute.py)

function called Âadd_attributeÂ that adds a new attribute to an object if it's possible. If the object cannot have a new attribute, the function should raise a TypeError exception with the message "can't add new attribute".
