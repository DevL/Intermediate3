# Exercise 02 - Working with API data

In these exercises we will be accessing and fetching data from the [JSON Placeholder API](https://jsonplaceholder.typicode.com). It is a collection of fake data with relations. In a later exercise, we will use the data we fetch from this API with `pandas`.

## Fetching data

Study the incomplete program `posts.py`. Using `requests`, either its functions or a `Session` object, fetch and output the following data to the console. Treat it as JSON. When outputting JSON data to the console, consider using [`pprint`](https://docs.python.org/3/library/pprint.html) to make it more readable.

1. If no post id is specified, all posts.
2. If a single post id is specified, just that post.
3. If any request fails, log a message at the error level and terminate the program.

# Fetching related data

4. If fetching a single post _and_ the command line flag `with-comments` is used, also fetch and output the comments belonging to the post.
5. Associate the comments with a post by adding them as a list to the post before outputting data. 

## Posting data and using the debugger

Since this is a fake API, no data will actually be written. However, you can still perform a few experiments using the debugger.

6. Add a post request to the `/posts` endpoint to create a new post. Capture the response in a variable and set a breakpoint. 
    * What status code do you get back? What does it mean?
    * What more does the response from creating a new post contain? In which format?
    * Can you access the newly created post? What response do you get and what does it mean?

## Outputting the post data to a JSON file (optional exercise)

7. Add a command line option to specify an output file. If it is given, output the fetched data as JSON to it.
    * Make sure that the data is valid JSON.

## Solution notes

A solution for exercises 1-5 has been provided in the _solutions/02_api_data_ directory.
