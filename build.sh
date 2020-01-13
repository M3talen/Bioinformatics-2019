python -m pip install -r requirements.txt
cd clib
gcc -c -Ofast alignment.c
ar rcs alignment.lib alignment.o
cd ..
python setup_c.py build_ext --inplace