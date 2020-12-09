# Testing project
A python package that installs bonmin.

The idea is that we can deploy a `bonmin_runtime_test` package on pypi,
and that we can install `bonmin` using:
```
$ pip install bonmin
```

On platforms where there is an official binary distribution of `bonmin` (win, osx, linux64),
`bonmin` is installed as a script and will be available. On platforms where there is no
official binary of `bonmin` (like ppc64le), user will have to install `bonmin` by other means.


# Building 

How to build: As we don't actually compile anything but just repackage, we can create the wheels for
any platform. Just specify the target platform with the `TARGET_WHEEL` environment variable.

For instance to build wheel for linux64, run:
```
$ TARGET_WHEEL=manylinux1_x86_64 python setup.py bdist_wheel
```

This will create a wheel in the `dist` directory, for instance `bonmin-1.0.0-py3-none-manylinux1_x86_64.whl`

`TARGET_WHEEL` should have the following values:
```
   - manylinux1_x86_64
   - win_amd64
   - macosx_10_14_x86_64
   - universal
```
Each value is self explanatory. `universal` should be used to generate the wheel for unsupported platforms.

# Automation

The `.travis` and `build.sh` scripts are starting point to configure automation.

`build.sh` will build all the wheels.

`.travis` setups the environment, then call `build.sh` to create wheels, then wheels are deployed with
the github release deployer. This just upload the wheels in the release section of github. If the build
is untagged (regular dev/master branches), wheels are uploaded in a release called package-BRANCH-latest
(example: https://github.com/vlkong/test_project/releases/tag/monobuild-latest)

If the build is tagged (like from a release, wheels are uploaded as package-TAG (example: TBD)





