[Discord Server](https://discord.gg/tb4XFNA9xK)

# About
---

Pyutils is a package that contains many different utilities ranging from getting source codes, to dumping output logs. This package simplifies things down the one line of code to be executed.

**[Pypi Page](https://pypi.org/project/pyutils-cr/)**

**[Github Page](https://github.com/GoodMusic8596/pythonutilities)**

# Examples
---

Return complete system information
```py
import pyutilscr
overview = pyutilities.ov()
print(overview.complete())
```
Get source code
```py
import pyutilscr as pyutil
print(pyutil.method_source(pyutil.method_source()))
#Use file_source instead of method_source for files
```

Dump output of python script
```py
import pyutilscr as pyutil
pyutil.log("foo.py","dump.txt")
```

Check to see if a string is in a file
```py
import pyutilscr as pyutil
print(pyutil.search("/home/runner/foo/",["Yessir","pyutilscr"],".py"))
```