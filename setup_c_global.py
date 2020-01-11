from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

examples_extension = Extension(
    "global",
    ["global.pyx", "clib/global.c"],
    include_dirs= ["clib"],
    depends=["global.h"]
)
setup(
    name="global",
    ext_modules=cythonize([examples_extension])
)
