# Testing project
A python package that installs bonmin.

How to build: checkout the project on the platform you want to build the wheels for, then:

```
$ python setup.py bdist_wheel
```

This will create a wheel in the `dist` directory, for instance `bonmin-1.0.0-py3-none-win_amd64.whl`

Installation of this wheel, for instance with:
```
pip install bonmin-1.0.0-py3-none-win_amd64.whl
```

Should install bonmin in the python scripts directory and make it available when the python environment is activated.

There is also an example travis that builds the wheels for linux64, win64 and osx.
The wheels are deployed as binaries in corresponding tagged releases.