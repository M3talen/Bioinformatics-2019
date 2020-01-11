from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

examples_extension = Extension(
    "local",
    ["local.pyx", "clib/local.c"],
    include_dirs= ["clib"],
    depends=["local.h"]
)
setup(
    name="local",
    ext_modules=cythonize([examples_extension])
)
