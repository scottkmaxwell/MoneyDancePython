Using make_pyi.py
=================

One of the difficulties in writing Python extensions for MoneyDance is that
your IDE knows nothing about the MoneyDance API. Python supports `pyi` files.
These files contain code that looks like Python, but actually just document
the API, including type information. Those PYI files give critical information
to IDEs such as PyCharm that allow them to understand the code you are writing.

# Using the PYI files

This folder already contains the site-packages that you need. To develop with
PyCharm, I do the following:

Step 1 - Create a virtual environment
-------------------------------------
On my Mac, I no longer have Python 2.7, so I just use Python 3.x. I do this in
my project folder.
```
python -m venv env
```

Step 2 - Update the site-packages
---------------------------------

Copy everything from the `site-packages` folder here into the site packages for
your new virtual environment. For me, that is:
```
cp -r ../MoneyDancePython/site-packages/* env/lib/python3.10/site-packages
```

Step 3 - Select that virtual environment in PyCharm
---------------------------------------------------

PyCharm should make this pretty easy so I won't document it here.

Step 4 - Update your script to see the new PYI files
----------------------------------------------------

Now you can conditionally import `moneydance`, which should only work from the
type checker in PyCharm. I also help PyCharm understand some obsolete Python2
types. Add this before your other imports

```python
try:
    from moneydance import *
    unicode = str
    basestring = str
except ImportError:
    pass
```

Your IDE (PyCharm, VSCode) will import `moneydance.pyi` for type analysis, but
MoneyDance will skip it.

Now your IDE should have all the information it needs to do autocomplete
and type analysis.

# Updating the PYI files

If you run `make_pyi.py` from the MoneyBot Console, it will output a file
called `moneydance.pyi`, as well as various folders with PYI files for the
MoneyDance API. These will be output to your `~/Downloads/MoneyDancePython`
folder. Run `move_modules.sh` to move the generated code into this folder.
We have to do this manual copy since security restrictions will not allow
the script to write directly to this folder.

If you do this, consider submitting a PR to update the main repo.

Enjoy!

-- Scott Maxwell
