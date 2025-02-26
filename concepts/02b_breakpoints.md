# Breakpoints

Sometimes it is useful to halt the execution of a program at a certain position and interactively examine what values variables hold. Python comes with a built-in debugger that can be entered by calling the [`breakpoint`](https://docs.python.org/3/library/functions.html#breakpoint) function from your Python code. Doing so and executing the code will drop you into an interactive Python REPL at the point you added the call to `breakpoint`.

```python
def my_function(a, b):
    result = a + b
    breakpoint()
    return result


if __name__ == "__main__":
    my_function(1, 2)
```

```
> ...exercises/02_api_data/debugger.py(4)my_function()
-> return result
(Pdb)
```

Now we can enter various debugger commands. `list` or its abbreviation `l` will show us the code around the breakpoint. This is a short example so we happen to see the entire python script, but the output would be narrower in a real-life example.

```
(Pdb) list
  1  	def my_function(a, b):
  2  	    result = a + b
  3  	    breakpoint()
  4  ->	    return result
  5
  6
  7  	if __name__ == "__main__":
  8  	    my_function(1, 2)
[EOF]
```

We can also check the values of the arguments passed to the function we currently are in by using `args` or the abbreviation `a`.

```
(Pdb) args
a = 1
b = 2
```

But what if we want to access the value of the variable called `a`? We can use a leading exclamation mark to escape the debugger commands and have our commanded interpreted as python code.

```
(Pdb) !a
1
```

Note that when there is no overlap between the debugger commands and our Python code, we can enter it without escaping it using a exclamation mark. To access our function `my_function`, we can type the following.

```
(Pdb) my_function
<function my_function at 0x100fc3f70>
```

For a list of debugger commands, enter `help` or `h`.

```
(Pdb) h

Documented commands (type help <topic>):
========================================
EOF    c          d        h         list      q        rv       undisplay
a      cl         debug    help      ll        quit     s        unt
alias  clear      disable  ignore    longlist  r        source   until
args   commands   display  interact  n         restart  step     up
b      condition  down     j         next      return   tbreak   w
break  cont       enable   jump      p         retval   u        whatis
bt     continue   exit     l         pp        run      unalias  where

Miscellaneous help topics:
==========================
exec  pdb
```

**NB:** _Configuring and working with other debuggers that Python's own is outside of the scope of this course. See the resources section below for a tutorial if you are using VS Code._

## Resources

* The documentation for the [`breakpoint`](https://docs.python.org/3/library/functions.html#breakpoint) function.
* The documentation for [the Python debugger](https://docs.python.org/3/library/pdb.html).
* [Working with breakpoints in VS Code](https://code.visualstudio.com/docs/python/debugging)

## Exercises

See _exercises/02_api_data/instructions.md_.
