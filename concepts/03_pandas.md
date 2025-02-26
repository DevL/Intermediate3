# Pandas

[Pandas](https://pandas.pydata.org) is a Python package providing data structures and data analysis functionality that is built upon the [NumPy](https://numpy.org) library.

## Data structures

The two primary data structures pandas provide are [`Series`](https://pandas.pydata.org/pandas-docs/stable/reference/series.html) and [`DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html). Series are one-dimensional similar to indexed arrays while dataframes are two-dimensional similar to tables. We will primarily examine dataframes, but be aware that series exist.

## Creating a DataFrame

A `DataFrame` can be created from several other kinds of data structure, but a common one – especially when working with JSON API:s – is having the raw data as a `list` of `dicts`.   

```python
import pandas

raw_data = [
    {"name": "Amadeus", "born": 2005, "breed": "KWPN"}, 
    {"name": "Nemah", "born": 2004, "breed": "arabian"},
    {"name": "BR Pan Demi", "born": 2020, "breed": "arabian"}
]

horses = pandas.DataFrame(raw_data)
```

Printing our dataframe `horses` will output the following.

```
          name  born    breed
0      Amadeus  2005     KWPN
1        Nemah  2004  arabian
2  BR Pan Demi  2020  arabian
```

## Accessing data selectively

We can use Python's [slicing](https://docs.python.org/3/reference/expressions.html#slicings) to access selected rows of data.

To select only the first row of data we could use `horses[:1]`.

```
      name  born breed
0  Amadeus  2005  KWPN
```

To select all but the first row of data, we could use `horses[1:]`.
Given our data, this happens to return the same result as asking for the last two rows using `horses[-2:]`.

```
          name  born    breed
1        Nemah  2004  arabian
2  BR Pan Demi  2020  arabian
```

We can also use slicing to select one or more columns.

To select a single column, slice on the column name, like `horses["name"]`. This will return a `Series` representing the column's values.

```
0        Amadeus
1          Nemah
2    BR Pan Demi
```

To select multiple columns, slice on a list containing the desired column names, like `horses[["name", "born"]]`. This will return a `DataFrame`.

```
          name  born
0      Amadeus  2005
1        Nemah  2004
2  BR Pan Demi  2020
```

## Merging dataframes

Let us say that we have another piece of data that we would like to join to our existing tabular data of horses.

```python
breed_names = [
    {"short": "arabian", "long": "Arabian horse"},
    {"short": "KWPN", "long": "Dutch Warmblood"}
]

breeds = pandas.DataFrame(breed_names)
```

```
     short             long
0  arabian    Arabian horse
1     KWPN  Dutch Warmblood
```

If we want to combine our two dataframes `horses` and `breeds`, we need to find a way to do this. There are two primary methods; [`join`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.join.html) and [`merge`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html). The former is great when we want to combine two dataframes using indicies, but in this case we want to combine the data based on keys. Moreover, we do not have columns with the same name, but rather `breed` in `horses` and `short` in `breeds`.

We can use [`merge`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html) to solve this by specifying what keys to use.

```python
merged = horses.merge(breeds, left_on="breed", right_on="short")
```

```
          name  born    breed    short             long
0      Amadeus  2005     KWPN     KWPN  Dutch Warmblood
1        Nemah  2004  arabian  arabian    Arabian horse
2  BR Pan Demi  2020  arabian  arabian    Arabian horse
```

## Removing and renaming columns

Notice that after the merge, we have two columns for the short breed name? We only need one of them so let us drop the one called `short`. We can do this by using the [`drop`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html) method, indicating that we want to drop data along the Y-axis (or column axis). We also indicate that we want to mutate the existing dataframe rather than creating a new one without the `short` column.

```python
merged.drop("short", axis=1, inplace=True)
```
```
          name  born    breed             long
0      Amadeus  2005     KWPN  Dutch Warmblood
1        Nemah  2004  arabian    Arabian horse
2  BR Pan Demi  2020  arabian    Arabian horse
```

One last change we might want to make is to [`rename`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html) the column `long` to `full breed name` instead. This time we will use a `dict` to map from the old name to the new name.

```python
merged.rename(columns={"long": "full breed name"}, inplace=True)
```
```
          name  born    breed  full breed name
0      Amadeus  2005     KWPN  Dutch Warmblood
1        Nemah  2004  arabian    Arabian horse
2  BR Pan Demi  2020  arabian    Arabian horse
```

## Exporting data from a dataframe

A `DataFrame` has a vast number of export methods built-in, of which common ones are `to_json` and `to_csv`.

```python
import json
from pprint import pprint

pprint(json.loads(merged.to_json()))
```

```python
{'born': {'0': 2005, '1': 2004, '2': 2020},
 'breed': {'0': 'KWPN', '1': 'arabian', '2': 'arabian'},
 'full breed name': {'0': 'Dutch Warmblood',
                     '1': 'Arabian horse',
                     '2': 'Arabian horse'},
 'name': {'0': 'Amadeus', '1': 'Nemah', '2': 'BR Pan Demi'}}
```

When exporting a `DataFrame`, we can see its underlying way of structuring the data it contains. Notice how the columns have been turned into keys at the root level and the rows are represented by nested dictionaries with the row index as the key in the nested dictionaries.

Of course, this can be changed by specifying a different orientation for the data when exporting it.

```python
pprint(json.loads(merged.to_json(orient="table")))
```

```python
{'data': [{'born': 2005,
           'breed': 'KWPN',
           'full breed name': 'Dutch Warmblood',
           'index': 0,
           'name': 'Amadeus'},
          {'born': 2004,
           'breed': 'arabian',
           'full breed name': 'Arabian horse',
           'index': 1,
           'name': 'Nemah'},
          {'born': 2020,
           'breed': 'arabian',
           'full breed name': 'Arabian horse',
           'index': 2,
           'name': 'BR Pan Demi'}],
 'schema': {'fields': [{'name': 'index', 'type': 'integer'},
                       {'name': 'name', 'type': 'string'},
                       {'name': 'born', 'type': 'integer'},
                       {'name': 'breed', 'type': 'string'},
                       {'name': 'full breed name', 'type': 'string'}],
            'pandas_version': '1.4.0',
            'primaryKey': ['index']}}
```

## Disabling output truncation

When working with larger datasets, it is common to see the columns and rows truncated when printing them to a console. While this is usually not a problem, sometimes we do want to see all the data being printed, e.g. when developing or troubleshooting. 

To configure pandas to _not_ truncate columns and rows when printing a dataframe, you can use the following settings. Be aware that with large dataframes this can result in _a lot_ of output to the console.

```python
pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)
pandas.set_option('display.width', None)
pandas.set_option('display.max_colwidth', None)
```

## Resources

* A [short video](https://www.youtube.com/watch?v=KHoEbRH46Zk) by IBM Technology on how NumPy and Pandas relate to each other.
* Pandas' [getting started guide](https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html#getting-started).
* Pandas' [user guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html#user-guide).
* Pandas' [reference documentation](https://pandas.pydata.org/pandas-docs/stable/reference/index.html#api). 
* [Polars](https://pola.rs) is an alternative to Pandas built in Rust. 

## Exercises

See _exercises/03_pandas/instructions.md_.
