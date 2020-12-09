#!/bin/bash

# As we are not actually compiling anything, we can just package the wheels
# in the same build
for target in universal linux64 win64 osx
do
	echo "Building wheel $target"
	# clean up
	rm -rf bin build
	# set python wheel platform
	case $target in
	   linux64) spec=manylinux1_x86_64;;
	   win64) spec=win_amd64;;
	   osx) spec=macosx_10_14_x86_64;;
	   *) spec=$target
	esac
	# uncompress binaries if appropriate
	[ ! -d bin ] && mkdir bin
	[ ! $spec = "universal" ] && (unzip distribs/bonmin-${target}.zip -d bin && chmod -f a+x bin/*)
    TARGET_WHEEL=$spec python3 setup.py bdist_wheel
done