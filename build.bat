cd clib
gcc -c alignment.c
ar rcs alignment.lib alignment.o
cd ..
python setup_c.py build_ext --inplace