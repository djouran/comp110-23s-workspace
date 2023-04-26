"""EX10: Simpy"""
####################################################
## This file is for people who are having trouble ##
## getting Jupyter Notebooks to work!             ##
####################################################

"""You will implement a utility class that is helpful for 
working with sequences of numerical data, just like what 
you would expect to see in a column of a data table. 
Through cleverly designed methods and operator overloads, 
you will be able to work with numerical data 
at a higher level of abstraction that feels more natural 
and powerful, than up until now in the course.

The implementation of this class is heavily inspired by 
an immensely popular and valuable-to-know library called NumPy 
(numerical python library). 
Simpy is a *simp*ler, single dimension implementation 
of many of the same capabilities of NumPy. 
In a sense, Simpy simps for NumPy."""

__author__ = "YOUR PID HERE"

"""You will implement the methods of Simpy 
in the `Simpy.py` file found in the `exercises/ex10` 
directory. As you now know, when you import modules 
in a running Python program, the module is evaluated only once."""

# Import the class being implemented
from Simpy import Simpy
print(f"{Simpy} successfully imported.")

###############################
## Part 0. Simpy Constructor ##
###############################

"""Define a constructor on the `Simpy` class that takes 
a parameter of type `list[float]`. 
Its purpose is to initialize the `values` attribute 
of the newly constructed `Simpy` object to the argument passed in.

Once your constructor is properly implemented, 
you expect to see `[1.0, 1.0, 1.0, 1.0, 1.0]` 
printed when running the code below."""

#ones = Simpy([1., 1., 1., 1., 1.])
#print(ones.values)

###############################
## Part 1. `__str__` Method ##
###############################

"""Define a method in `Simpy` named `__str__` that 
takes no arguments and returns a `str`. 
As you know, this method will automagically be 
called when a `Simpy` object is converted 
to a `str` representation. 

For the `ones` variable constructed above 
(with a list of 5x `1.0` values) 
your expected output running the code below is:

`Simpy([1.0, 1.0, 1.0, 1.0, 1.0])`

More generally, the `str` returned by the method 
should be in a format of `"Simpy(...)"` where the 
elipses are replaced with the `str` representation 
of the `values` attribute `list[str]`."""

#print(ones)

###########################
## Part 2. `fill` Method ##
###########################

"""Define a method in `Simpy` named `fill`. 
Its purpose is to _fill_ a `Simpy`'s `values` 
with a specific number of repeating values. 
The `fill` method will have two parameters following `self`:

1. The `float` value you are filling the `values` list in with.
2. The `int` number of values to fill in.

The `fill` method is procedure-like in that it returns `None` 
and _mutates_ the object the method is called on. 
After calling `fill`, the length of the `Simpy` object's
values should be equal to the second argument given to `fill`.

For example, consider the following usage 
and expected printed output, given inline, below:"""

"""TIP: you can un-comment a line of code 
by pressing 'cmd + /' on a mac and 'ctrl + /' on windows!"""

# twos = Simpy([])
# twos.fill(2.0, 3)
# print("Actual: ", twos, " - Expected: Simpy([2.0, 2.0, 2.0])") 
# twos.fill(2.0, 5)
# print("Actual: ", twos, " - Expected: Simpy([2.0, 2.0, 2.0, 2.0, 2.0])")

# mixed = Simpy([])
# mixed.fill(3.0, 3)
# print("Actual: ", mixed, " - Expected: Simpy([3.0, 3.0, 3.0])")
# mixed.fill(2.0, 2)
# print("Actual: ", mixed, " - Expected: Simpy([2.0, 2.0])")

#############################
## Part 3. `arange` Method ##
#############################

"""Define a method in `Simpy` named `arange`. 
Its purpose is to fill in the `values` attribute 
with range of values, like the `range` built-in function, 
but in terms of `float`s. 
It has three parameters in addition to `self`, 
the last being optional:

1. `start` - a `float` indicating the first value in the range
2. `stop` - a `float` that is not included in the produced range values
3. `step` - a `float` whose default value is `1.0` that indicates how to increase (or decrease) each subsequent item in the generated range. Unlike the built-in `range` function, this can be a fractional, `float` value. Step cannot be `0.0`.

Think carefully about what the value of `step` 
tells you about how to design your loop(s) for this method. 
Before any looping, you should `assert step != 0.0` 
to be sure you avoid an infinite loop with an invalid argument."""

# positive = Simpy([])
# positive.arange(1.0, 5.0)
# print("Actual: ", positive, " - Expected: Simpy([1.0, 2.0, 3.0, 4.0])")

# fractional = Simpy([])
# fractional.arange(0.0, 1.0, 0.25)
# print("Actual: ", fractional, " - Expected: Simpy([0.0, 0.25, 0.5, 0.75])")

# negative = Simpy([])
# negative.arange(-1.0, -5.0, -1.0)
# print("Actual: ", negative, " - Expected: Simpy([-1.0, -2.0, -3.0, -4.0])")

##########################
## Part 4. `sum` Method ##
##########################

"""Define a method in `Simpy` named `sum`. 
Its purpose is to compute and return the sum 
of all items in the `values` attribute. 
You are encouraged to use Python's built-in 
`sum` function to assist in the implementation 
of your `sum` method. Doing so is illustrative 
of a pattern called delegation, where the implementation 
of some algorithm is delegated to existing algorithm. 
It should take no arguments and return a `float`."""

# ones = Simpy([1.0, 1.0, 1.0])
# print("Actual: ", ones.sum(), " - Expected: 3.0")

# one_to_nine = Simpy([])
# one_to_nine.arange(1.0, 10.0)
# print("Actual: ", one_to_nine.sum(), " - Expected: 45.0")

##########################################
## Part 5. Operator Overload: `__add__` ##
##########################################

"""Next, you will add the ability to use the _addition operator_ (`+`) 
in conjunction with `Simpy` objects and floats.

You will implement `__add__` such that the right-hand side 
operand of an addition expression can be _either_ a `Simpy` 
object _or_ a `float` value using a `Union` type. The `__add__` 
method should return a new `Simpy` object and _should not_ mutate 
the object the method is called on.

When the right-hand side of an addition expression 
is also a `Simpy` object, you should assert that 
both objects' `values` attributes have equal lengths. 
Then, you should produce a new `Simpy` object where 
each `item` in its `values` attribute corresponds to 
the items of the original `Simpy` objects at the 
same index added together. For example:

~~~python
a = Simpy([1.0, 1.0, 1.0])
b = Simpy([2.0, 3.0, 4.0])
c = a + b
print(c)  # Output: Simpy([3.0, 4.0, 5.0])
~~~

When the right-hand side of an addition expression is a `float` value, you should produce a new `Simpy` object where each item corresponds to the item at the same index in the left-hand side `Simpy` object added to the `float`. For example:

~~~python
a = Simpy([1.0, 2.0, 3.0])
b = a + 10.0
print(b)  # Output: Simpy([11.0, 12.0, 13.0])
~~~

The signature of the `__add__` function should be:

~~~python
def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
~~~"""

# # This code tests a Simpy + Simpy

# a = Simpy([1.0, 1.0, 1.0])
# b = Simpy([2.0, 3.0, 4.0])
# c = a + b
# print("Actual: ", c, " - Expected: Simpy([3.0, 4.0, 5.0])")
# print("Actual: ", a + a, " - Expected: Simpy([2.0, 2.0, 2.0])")
# print("Actual: ", b + b, " - Expected: Simpy([4.0, 6.0, 8.0])")

# # This code tests a Simpy + float
# a = Simpy([1.0, 2.0, 3.0])
# b = a + 10.0
# print("Actual: ", b, " - Expected: Simpy([11.0, 12.0, 13.0])")
# print("Actual: ", a + 1.0, " - Expected: Simpy([2.0, 3.0, 4.0])")

##########################################
## Part 6. Operator Overload: `__pow__` ##
##########################################

"""Next, you will add the ability to use the _power operator_ (`**`) 
in conjunction with `Simpy` objects and floats.

You will implement `__pow__` much the same as `__add__`, 
except that the operation performed item-wise is exponentiation 
rather than addition. For example, when raising one `Simpy` 
object by another `Simpy` object whose `values` attributes 
are the same length:

~~~python
a = Simpy([2.0, 2.0, 2.0])
b = Simpy([1.0, 2.0, 3.0])
c = a ** b
print(c)  # Output: Simpy([2.0, 4.0, 8.0])
~~~

Alternatively, exponentiation should also work with a `float` 
as the right-hand side operand:

~~~python
a = Simpy([1.0, 2.0, 3.0])
b = a ** 2.0
print(b)  # Output: Simpy([1.0, 4.0, 9.0])
~~~

Your implementations of `Simpy#__add__` 
and `Simpy#__pow__` 
should be _very_ similar!"""

# # This code tests a Simpy ** Simpy

# a = Simpy([2.0, 2.0, 2.0])
# b = Simpy([1.0, 2.0, 3.0])
# c = a ** b
# print("Actual: ", c, " - Expected: Simpy([2.0, 4.0, 8.0])")
# print("Actual: ", a ** a, " - Expected: Simpy([4.0, 4.0, 4.0])")
# print("Actual: ", b ** b, " - Expected: Simpy([1.0, 4.0, 27.0])")

# # This code tests a Simpy ** float

# a = Simpy([1.0, 2.0, 3.0])
# b = a ** 2.0
# print("Actual: ", b, " - Expected: Simpy([1.0, 4.0, 9.0])")
# print("Actual: ", a ** 3.0, " - Expected: Simpy([1.0, 8.0, 27.0])")

################################
## Check #1 for Understanding ##
#################################

"""In the code below, use the capabilities you've added 
to `Simpy` to ultimately produce a `Simpy` object 
whose `values` are the first 16 powers of 2, 
starting from 2 ** 0 ranging up to 2 ** 15. 
You can, and should, make use of intermediate variables 
holding `Simpy` objects. You should use the `arange`, 
`fill`, and `__pow__` methods. Ultimately, you should 
`print` your object and expect the output of:

~~~python
Simpy([1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0, 256.0, 512.0, 1024.0, 2048.0, 4096.0, 8192.0, 16384.0, 32768.0])
~~~

Your work should _not_ include any loops written in the code below."""

# TODO: Check #1 for Understanding

#################################################
## Part 7. `__eq__` operator overload for `==` ##
#################################################

"""Next, you will add the ability to produce a _mask_, 
or a `list[bool]`, based on the equality of each item 
in the `values` attribute with some other `Simpy` object 
or a `float` value. This operator overload will be similar
to those above, but will instead return a `list[bool]` 
that you will later use to filter a `Simpy` array 
as you did previously with the `mask` function. 
The `__eq__` special method is automatically called 
when you write expressions using the `==` operator, 
as demonstrated below.

Example use with two `Simpy` objects:

~~~python
a = Simpy([1.0, 2.0, 3.0, 4.0])
b = Simpy([1.0, 2.0, 1.0, 4.0])
c = a == b
print(c)  # Output: [True, True, False, True]
~~~

Example use with a `Simpy` object and a `float`:

~~~python
a = Simpy([1.0, 2.0, 1.0, 4.0])
b = a == 1.0
print(b)  # Output: [True, False, True, False]
~~~

Your expected method signature of `__eq__` is:

~~~python
def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
~~~"""

# # This code tests a Simpy == Simpy

# a = Simpy([1.0, 2.0, 3.0, 4.0])
# b = Simpy([1.0, 2.0, 1.0, 4.0])
# c = a == b
# print("Actual: ", c, " - Expected: [True, True, False, True]")
# print("Actual: ", a == a, " - Expected: [True, True, True, True]")

# # This code tests a Simpy == float

# a = Simpy([1.0, 2.0, 1.0, 4.0])
# b = a == 1.0
# print("Actual: ", b, " - Expected: [True, False, True, False]")
# print("Actual: ", a == 2.0, " - Expected: [False, True, False, False]")

################################################
## Part 8. `__gt__` operator overload for `>` ##
################################################


"""Next, you will add the ability to produce a _mask_, 
or a `list[bool]`, based on the greater than relationship 
between each item in the `values` attribute with some other 
`Simpy` object or a `float` value. 
This operator overload will be VERY similar to the equality overload, 
but will test for greater than rather than equality.

~~~python
a = Simpy([1.0, 2.0, 3.0, 4.0])
b = Simpy([2.0, 1.0, 1.0, 5.0])
c = a > b
print(c)  # Output: [False, True, True, False]
~~~

Example use with a `Simpy` object and a `float`:

~~~python
a = Simpy([1.0, 2.0, 3.0, 4.0])
b = a > 2.0
print(b)  # Output: [False, False, True, True]
~~~

Your expected method signature of `__gt__` is:

~~~python
def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
~~~"""

# # This code tests a Simpy > Simpy

# a = Simpy([1.0, 2.0, 3.0, 4.0])
# b = Simpy([2.0, 1.0, 1.0, 5.0])
# c = a > b
# print("Actual: ", c, " - Expected: [False, True, True, False]")
# print("Actual: ", b > a, " - Expected: [True, False, False, True]")

# # This code tests a Simpy > float

# a = Simpy([1.0, 2.0, 3.0, 4.0])
# b = a > 2.0
# print("Actual: ", b, " - Expected: [False, False, True, True]")
# print("Actual: ", a > 3.0, " - Expected: [False, False, False, True]")

############################################################################
## Part 9. Subscription Notation with the `__getitem__` operator overload ##
############################################################################

"""Next, you will add the ability to use the _subscription_ 
operator with `Simpy` objects. To add _subscription notation_ 
support to objects of classes you design, you must implement 
the special method named `__getitem__`.

The `Simpy` object will use the subscription operator 
in two distinct ways. First, the most familiar behavior, 
you will be able to read specific items from the Simpy array.

For example:

~~~python
a = Simpy([10.0, 20.0, 30.0])
print(a[0])  # Output: 10.0
print(a[1])  # Output: 20.0
~~~

For now, it is worth focusing on getting this first, 
simpler usage working. 
Then, in the next and final part of this exercise, 
you will get the second usage of subscription notation working.

The expected signature of `__getitem__`  for this part is:

~~~python
def __getitem__(self, rhs: int) -> float:
~~~"""

# a = Simpy([10.0, 20.0, 30.0])
# print("Actual: ", a[0], " - Expected: 10.0")
# print("Actual: ", a[1], " - Expected: 20.0")
# print("Actual: ", a[2], " - Expected: 30.0")

##########################################################################
## Part 10. Overloading the Subscription Notation to Filter with a Mask ##
##########################################################################

"""The acclaimed _NumPy_ library, that `Simpy` is inspired by, 
allows you to use the subscription operator not just to select
individual items, but also to filter with a mask. 
It adds a second usage to the operator, just like you have had 
two uses of many of the operators above, such as adding two `Simpy`s 
or a `Simpy` and a `float`.

The big idea of the second usage of subscription notation is that if 
instead of giving an `int` inside the subscription brackets 
you give a `list[bool]`, the expression will return a new `Simpy` 
object containing only the _masked_, or filtered, `values`. For example:

~~~python
a = Simpy([1.0, 2.0, 3.0, 4.0, 2.0, 1.0])
mask = a > 2.0
print(mask)  # Output: [False, False, True, True, False, False]
b = a[mask]
print(b) # Output: Simpy([3.0, 4.0])  
~~~

The above example did not need to establish a separate variable 
named `mask`, it only did so to make it obvious 
what the `mask` values were. 
More conventionally, the above example would be written 
in a shorter-form notation such as:

~~~python
a = Simpy([1.0, 2.0, 3.0, 4.0, 2.0, 1.0])
b = a[a > 2.0]
print(b) # Output: Simpy([3.0, 4.0])
~~~

Take a moment to reflect on how _expressive_ that second line is! 
For this expression to evaluate, first the `__gt__` method call 
must evaluate and finally a `__getitem__` method call whose behavior
you will need to extend. 
Notice how natural this expression feels in English: 
from the `Simpy` object `a`, select the values that greater than `2.0`.

Because of these two distinct use cases, 
notice not only the parameter given to `__getitem__` 
can either be an `int` in the first usage and a `list[bool]` 
in the second usage, 
but the return type will also be two different types: 
either a single `float` value or a new `Simpy` object.

Thus, you will need to modify the signature of your
`__getitem__` method and implement logic to test for whether
`rhs` is an instance of an `int` or not.

~~~python
def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
~~~"""

# a = Simpy([1.0, 2.0, 3.0, 4.0, 2.0, 1.0])
# b = a[a > 2.0]
# print("Actual: ", b, " - Expected: Simpy([3.0, 4.0])")
# print("Actual: ", a[a + 1.0 == 2.0], " - Expected: Simpy([1.0, 1.0])")

################################
## Check #2 for Understanding ##
################################

"""Consider two `Simpy` objects that are "columns" 
of the same table. 
The `max_temps` object contains the maximum temperature 
for a given day, the `precip` object contains the amount of 
precipitation for the corresponding days.

In terms of the functionalities implemented above, 
compute and print the sum of precipitation on days where the maximum
temperature is greater than 32.0. 
You should not need to write any loops in the code below 
in order to calculate this. 
Feel free to establish additional, 
intermediate variables as needed. 
Then try to simplify your solution as much as you possibly can. 
The expressions you write will ultimately need to call 
upon the operator overloads of `__gt__` and `__getitem__`. 
You will also need to use call your `sum` method."""

# max_temps = Simpy([21.0, 30.0, 41.0, 31.0, 45.0, 31.5])
# precip = Simpy([0.0, 1.5, 0.1, 0.3, 0.2, 0.8])

# TODO: Your solution goes here.

