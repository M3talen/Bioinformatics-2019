cd clib
gcc -c -Os -mtune=native alignment.c
ar rcs alignment.lib alignment.o
cd ..
python setup_c.py build_ext --inplace