

from distutils.core import setup
import os
import platform
import tokenize
from sys import version_info

target_wheel = os.environ.get("TARGET_WHEEL", None)
universal_wheel = True if target_wheel == "universal" else False
is_windows = (target_wheel == "win_amd64")

try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel

    class bdist_wheel(_bdist_wheel):
        def finalize_options(self):
            _bdist_wheel.finalize_options(self)
            # Mark us as not a pure python package
            self.root_is_pure = universal_wheel

        def get_tag(self):
            # we want to create a wheel for current python major, per platform
            # On linux, we want to return manylinux tag
            python, abi, plat = super().get_tag()
            if not universal_wheel:
                if target_wheel is not None and target_wheel != "universal":
                    plat = target_wheel
                else:
                    if plat == "linux_x86_64":
                        plat = "manylinux1_x86_64"
            return "py%s" % version_info[0], "none", plat

except ImportError:
    bdist_wheel = None


if hasattr(tokenize, 'detect_encoding'):
    try:
        _detect_encoding = tokenize.detect_encoding
    except AttributeError:
        pass
    else:
        def detect_encoding(readline):
            try:
                return _detect_encoding(readline)
            except SyntaxError:
                return 'latin-1', []

        tokenize.detect_encoding = detect_encoding

if universal_wheel:
    scripts = None
else:
    scripts = ['bin/bonmin.exe', 'bin/libipoptfort.dll'] if is_windows else ['bin/bonmin'] 

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    try:
        with open(os.path.join(HERE, *parts)) as f:
            return f.read()
    except:
        return None


readme = read('README.md')
if readme is None:
    readme = 'A Python packaging for bonmin.'


setup(name='bonmin_runtime_test',
      packages=['bonmin_runtime_test'],
      version='1.0.0',
      author='Viu-Long Kong',
      description='A Python packaging for the bonmin solver.',
      long_description='%s\n' % readme,
      url='http://github.com/vlkong/test_package',
      license='Apache 2.0',
      cmdclass={'bdist_wheel': bdist_wheel},
      scripts=scripts
      )
