#!/bin/sh
# Compiles all UI files into python classes.

DIR="$(dirname $(realpath $0))/src/UI";

cd ${DIR}
mkdir -p ./build
rm ${DIR}/build/*

echo "Start compiling UI files."

for file in `ls ./*.ui`;
    do
        echo "Compiling ${file}"
        pyuic5 ${file} -o ./build/${file%.*}.py;
done;

echo "Done."