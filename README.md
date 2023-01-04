Using make_pyi.py
=================

One of the difficulties in writing Python extensions for MoneyDance is that
your IDE knows nothing about the MoneyDance API. Python supports `pyi` files.
These files contain code that looks like Python, but actually just documents
the API, including type information. Those PYI files give critical information
to IDEs such as PyCharm that allow them to understand the code you are writing.

# Using the PYI files

This folder already contains the `moneydance.pyi` and `com` folders for
MoneyDance 2022.3. To utilize these in your own script, copy both of those
into the same folder as your script and add this before your other imports:

```python
try:
    from moneydance import *
except ImportError:
    pass
```

Your IDE (PyCharm, VSCode) will import `moneydance.pyi` for type analysis, but
MoneyDance will skip it.

Now your IDE should have all of the information it needs to do autocomplete
and type analysis.

# Updating the PYI files

If you run `make_pyi.py` from the MoneyBot Console, it will output a file
called `moneydance.pyi`, as well as a folder called `com` with PYI files for
the MoneyDance API. These will be output to your `~/Downloads/MoneyDancePython`
folder.

If you do this, consider copying them back to this folder and submitting a PR
to update the main repo.

Enjoy!

-- Scott Maxwell
