# File Handling
 
Use the [`open`](https://docs.python.org/3/library/functions.html#open) function to open a file. When opening a file, a number of options can be set, such as the way the file can be accessed, any specific encoding to use, and whether the file should be treated as a text file or as a binary file. `open` returns a [file object](https://docs.python.org/3/glossary.html#term-file-object) that can be used to access and modify the contents of the file. There are a plenty of different file operations that can be performed, but the most common ones will be reading files, either in one go or line by line, and writing files.

Below follows an example of opening a text file, reading all its contents as a single string, and closing the file. 

```python
f = open("some_file_to_read.txt", "r")
data = f.read()
f.close()
```

Writing a file is similar, but requires another file mode to be used.

```python
f = open("some_file_to_write.txt", "w")
f.write("Some data to write")
f.close()
```

For an alternative way of ensuring that the file has been closed once you are finished with it, see _concepts/01c_context_managers.md_.

## Resources

* Python's tutorial on [reading and writing files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files).

* The built-in [`open`](https://docs.python.org/3/library/functions.html#open) function.

* Python's [`glossary`](https://docs.python.org/3/glossary.html).
    * The definition of a [`file` or `file-like object`](https://docs.python.org/3/glossary.html#term-file-object).
    * The definition of a [`text file`](https://docs.python.org/3/glossary.html#term-text-file).

## Exercises

First read _concepts/01b_error_handling.md_.
