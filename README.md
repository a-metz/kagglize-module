# Kagglize Module

Use your Python modules (code split up over mutiple files) for Kaggle submissions.

## Why
When writing complex Python programs, it is practial to split up the code over several files and directories. The directory structure might look something like this:

```
my_module
├── __init__.py
├── some_file.py
├── some_directory
│   ├── __init__.py
│   └── another_file.py
...
```

Unfortunately, the online competition platform [Kaggle](https://www.kaggle.com/) uses [Jupyter notebooks](https://jupyter.org/) and single Python scripts edited in a web-based IDE. It does not support uploading a locally developed python module consisting of mutiple files. (Technically uploading single files works but is prohibitively time-intensive and error-prone to do for a whole module, especially when resubmitting on a regular basis.)

This tools helps you with that, by merging all your files into a single Python script. When executed this script regenerates all your original files, so you can import and run code from them.

## Usage

Install via pip:
```
$ pip install kagglize-module
```

Run:
```
$ kagglize-module
Usage: kagglize-module [OPTIONS] MODULE_ROOT_PATH

  Generate a single python script to recreate files of a python module.

Options:
  --output-file PATH      Location of generated script.  [default: output.py]
  --filename-regex TEXT   Filter filenames with regex.  [default: ^.*\.py$]
  --import / --no-import  Generate import statement.  [default: True]
  --help                  Show this message and exit.
```

Example:
```
$ kagglize-module my_module  # the module root path
```

Generates following python code to `output.py`:
```python
from pathlib import Path

Path('my_module').mkdir(parents=True, exist_ok=True)
Path('my_module/__init__.py').open('w').write('')
Path('my_module/some_file.py').open('w').write('<content of some_file.py as string>')
Path('my_module/some_directory').mkdir(parents=True, exist_ok=True)
Path('my_module/some_directory/__init__.py').open('w').write('')
Path('my_module/some_directory/another_file.py').open('w').write('<content of another_file.py as string>')
...

import my_module
```

You can copy and paste this code into a Jupyter notebook on Kaggle and run it to load your module.

## Disclaimer

This is intended only to upload your own code and not for uploading 3rd party modules.

Use at your own risk (see [LICENSE](LICENSE)). I cannot guarantee that Kaggle allows using this and will not disqualify your submission. When asking regarding its usage for the Abstraction and Reasoning Challenge I got [a positive answer](https://www.kaggle.com/c/abstraction-and-reasoning-challenge/discussion/141622#802477) from a Kaggle Team Member.

