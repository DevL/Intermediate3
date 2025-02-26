# Error Handling

Some operations in Python can result in an error or [`exception`](https://docs.python.org/3/reference/executionmodel.html#exceptions). An exception break the normal flow of code execution and if not handled, will terminate the execution of the program. However, it is possible to enclose a piece of code that might cause an exception that you want to handle in a `try...except` statement.

```python
def division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("You tried to divide by zero!")
    except TypeError:
        print("You need to use two numbers!")
    else:
        print("No exception was raised!")
    finally:
        print("Always output this line!")
    
    return result
```

Notice that we can specify what specific exceptions we want to handle in an `except` clause. We can also specify an `else` clause that will be executed if no exception was raised and a `finally` clause that will be executed just before leaving the `try` block regardless of whether an exception was raised or not. 

To raise an exception, you use the `raise` statement.

```python
def my_unfinished_function():
    raise NotImplementedError
```

You can also create your own exceptions. A good built-in exception to base your own on is `RuntimeError`.

```python
class MyError(RuntimeError):
    pass


raise MyError("some error message")
```

There is more to exceptions and error handling, but this is enough to wet your appetite. See the below resources for more in-depth information.

## Resources

* More on [exceptions](https://docs.python.org/3/reference/executionmodel.html#exceptions) in Python's execution model.
* The [`try`](https://docs.python.org/3/reference/compound_stmts.html#try) statement.
    * The [`except`](https://docs.python.org/3/reference/compound_stmts.html#except-clause) clause.
* [Built-in exceptions](https://docs.python.org/3/library/exceptions.html).

## Exercises

First read _concepts/01c_context_managers.md_.
