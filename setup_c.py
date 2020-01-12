from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

examples_extension = Extension(
    "alignment",
    ["alignment.pyx", "clib/alignment.c"],
    include_dirs= ["clib"],
    depends=["alignment.h"]
)
setup(
    name="alignment",
    ext_modules=cythonize([examples_extension])
)
