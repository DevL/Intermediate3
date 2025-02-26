# Exercise 03 - Working with data in pandas

Building on what we in the previous exercise learnt about fetching data from a [REST](https://en.wikipedia.org/wiki/REST) API, we will continue to use the [JSON Placeholder API](https://jsonplaceholder.typicode.com) to access different data and combine them using [Pandas](https://pandas.pydata.org).

_If you are already comfortable working with Pandas, have a look at the last optional challenge._

## Fetching and merging data

1. Given the incomplete program `ursa.py`, fetch the following data from the [JSON Placeholder API](https://jsonplaceholder.typicode.com).
    * All [posts](https://jsonplaceholder.typicode.com/posts).
    * All [users](https://jsonplaceholder.typicode.com/users).
2. Create [DataFrame] objects for each set of fetched data and study them. Make a note of what data are in each dataframe and how the data sets relate to each other.
    * Hint: It can be a good idea to set a [`breakpoint`](https://docs.python.org/3/library/functions.html#breakpoint) and interact with the dataframes in the [interactive debugger](https://docs.python.org/3/library/pdb.html).
3. [`Merge`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html) the dataframes based on suitable columns in each.
    * Ensure that any ID column is named in a manner that denotes what the ID represents, e.g. `'userId'`, `'postId'` etc.
    * Ensure that no duplicate columns are left in the final result.
4. Output the merged data as JSON.
    * Experiment with [various orientations](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html#pandas-dataframe-to-json) such as `records` and `table`.
    * The program accepts an optional argument for an outfile. If it is given, write the JSON to that file instead of printing it to the console.

## Challenges (optional)

5. In addition to fetching and combining the above data, also fetch all [`albums`](https://jsonplaceholder.typicode.com/albums) and merge them into datastructure on an appropriate per-user basis.
6. In exercise 3 above, you were instructed to merge users and posts. Could you have [joined](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.join.html) the two dataframes instead? If so, what would you have to do combine the two dataframes?
7. Now do all of the above exercises using [Polars](https://pola.rs) instead of Pandas.

## Solution notes

A solution for exercises 1-4 has been provided in the _solutions/03_pandas_ directory.
