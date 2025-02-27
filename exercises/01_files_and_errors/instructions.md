# Exercise 01 - File and Error Handling

Study the incomplete program `liner.py` and modify it to accomplish the following tasks. The text file `data.txt` has been provided as example data.

## Enumerating the lines of a text file.

1. Read the contents of the given input file as text file.
    * Make sure that the file is closed one way or the other.
    * Hint: everything you need is in the [Python tutorial](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files).
2. Prepend a line number to each of the lines read.
    * The numbering should start at 1.
    * The line number should be right-justified and allow up to six digits.
        * Hint: There are several ways to do this. An elegant way is to use [f-strings](https://docs.python.org/3/reference/lexical_analysis.html#f-strings) with [format specification](https://docs.python.org/3/library/string.html#formatspec).
    * Separate the line number and the line of text with a colon and a space.
        * Example: `   123: Some text`
    * Hint: Have a look at the built-in [`enumerate`](https://docs.python.org/3/library/functions.html#enumerate) function.
3. Output the enumerated lines to the console.
    * There should be no empty lines output between enumerated lines.
        * Hint: Did you know that [`print`](https://docs.python.org/3/library/functions.html#print) accepts some extra arguments?

## Writing a file

The program accepts an optional flag to specify an output file.

4. If an output file has been given, write the enumerated lines to that file rather than to the console.

## Handle a missing input file

5. If the input file cannot be opened, a certain error will be raised and a stack trace will be output. Handle this error by instead outputting a friendly message to the program's user that the file is missing.
    * Hint: Once again, the [tutorial](https://docs.python.org/3/tutorial/errors.html#handling-exceptions) holds the key to the solution.

## Handle an output file that you cannot write to

6. If the input file cannot be written to, a certain error will be raised and a stack trace will be output. Handle this error by instead logging that the output file is missing and fall back to outputting the enumerated lines to the console.
    * Hint: The easiest way of causing a write error is to set an existing output file to be read-only. This will raise a `PermissionError` when opening the file in write mode.

## Outputting the enumarated lines as JSON (optional exercise)

The program accepts an optional flag to specify that the output should be in JSON.

7. If the flag is set, create a dictionary where the keys are the line numbers and the values are the lines. Output this dictionary as JSON to either the console or a given output file as before.
    * You can varify that the output is proper JSON by using the program `verify_json.py` found in this directory. 
    * Hint: Have a look at the ['json'](https://docs.python.org/3/library/json.html) module and [the tutorial section](https://docs.python.org/3/tutorial/inputoutput.html#saving-structured-data-with-json) on reading and writing JSON files.

## Solution notes

A solution for exercises 1-6 has been provided in the _solutions/01_files_and_errors_ directory. Its doctests can be run by entering into that directory in the terminal and running `pytest`.
