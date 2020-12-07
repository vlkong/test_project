

from distutils.core import setup
import os
import platform
import tokenize
from sys import version_info



try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel

    class bdist_wheel(_bdist_wheel):
        def finalize_options(self):
            _bdist_wheel.finalize_options(self)
            # Mark us as not a pure python package
            self.root_is_pure = False

        def get_tag(self):
            # we want to create a wheel for current python major, per platform
            # On linux, we want to return manylinux tag
            python, abi, plat = super().get_tag()
            if plat == "linux_x86_64":
                plat = "manylinux1_x86_64"
            return "py%s" % version_info[0], "none", plat

except ImportError:
    bdist_wheel = None


def is_windows():
    return platform.system() in ('Windows', 'Microsoft')

scripts = ["bin/bonmin.exe", "bin/libipoptfort.dll"] if is_windows() else ["bin/bonmin"] 

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


setup(name='bonmin',
      version='1.0.0',
      author='Viu-Long Kong',
      description='A Python packaging for the bonmin solver.',
      long_description='%s\n' % readme,
      packages=[],
      url='http://github.com/vlkong/test_package',
      license='Apache 2.0',
      cmdclass={'bdist_wheel': bdist_wheel},
      scripts=scripts
      )
