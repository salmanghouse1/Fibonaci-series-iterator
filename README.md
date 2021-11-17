# Assignment: A Fibonacci series iterable


Write an iterable which produces an iterator of the Fibonacci series for a
given value.

Example:

```python
>>> [number for number in Fibonacci(10)]
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

### What this software includes:

-  a test module called `test_fibonacci.py`
-  a module called `fibonacci.py`
-  iterable class called `Fibonacci` which requires a single
  positional argument. , an iterable class has to:
    - Have an `__iter__`
    - Have a `__next__`
    - Raise a `StopIteration` exception when there are no more items


### TDD
TDD methodology, developed an algorithm to assert the following test
cases.

Note: iterables return iterators and not lists, 

```python
assert list(Fibonacci(2)) == [0, 1, 1]
```
## Tests

1. If constructed with a value other than an integer, the Fibonacci constructor
  should raise a ValueError.
1. Given a constructor value of 0, the iterator should produce the values `[0]`
   if cast as a list.
1. Given a constructor value of 1, the iterator should produce the values
`[0, 1]` if cast as a list.
1. Given a constructor value of 2, the iterator should produce the values
`[0, 1, 1]`.
1. Given a value of 4, the iterator should produce `[0, 1, 1, 2, 3]`
1. Given a value of 10, the iterator should produce
`[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]`
1. Given a negative value, the iterator should produce an empty list.

**Note:** Any integer must be accepted and calculate a correct Fibonacci
sequence. Building a function which only handles the above cases is
insufficient and will not be accepted.

