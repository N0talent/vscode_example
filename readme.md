# Setup env (Linux)
```
python -m venv v
source v/bin/activate
pip install .
```

# Usage

1. set breakpoint in 2 files:
-   `Packagename/module1/f1.py, line 2`
-   `v/lib/<your python version>/site-packages/Packagename/module1/f1.py, line 2`

2. open file `Packagename/module3/f2.py`and run debugger with setting 'Python: Current File'

# out come

Breakpoint will stop in file `v/lib/<your python version>/site-packages/Packagename/module1/f1.py, line 2` and not `Packagename/module1/f1.py, line 2`
