# Context Managers

Context managers are objects that define the methods `__enter__` and `__exit__`. They are used to wrap the execution of some code in order to ensure that some things are done before (as defined by `__enter__`) and some things are done afterwards (as defined by `__exit__`).

You have seen context managers being used when opening files or in asserting that an error is raised using pytest.

A typical example use case is to avoid having to manually close an opened resource. Compare the following two examples of opening and reading the contents of a text file.

```python
f = open("some_file.txt", "r")
data = f.read()
f.close()
```

```python
with open("some_file.txt", "r") as f:
    data = f.read()
```

Notice the syntax for assiging the return value of the call to `open` to the variable `f`.

Also, notice how the latter example does not send the `close` message to the file handler `f`. This is because that behaviour is implemented in the `__exit__` method of the file handler `f`.

## Handling errors

In addition to cleaning up opened resources, a context manager can also be used to handle exceptions raised during the exection of the code block. If an exception is raised, it and additional information about it will be passed as arguments to `__exit__`. This is how `pytest.raises` is implemented and used to assert that an expected exception is raised by the code under test.

## Resources

* The term [context manager](https://docs.python.org/3/glossary.html#term-context-manager).
* The term [context managaer protocol](https://docs.python.org/3/glossary.html#term-context-management-protocol).
* The [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement.

## Exercises

See _exercises/01_files_and_errors/instructions.md_.
