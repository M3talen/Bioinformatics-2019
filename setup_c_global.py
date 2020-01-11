from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

examples_extension = Extension(
    "globalAlg",
    ["globalAlg.pyx", "clib/globalAlg.c"],
    include_dirs= ["clib"],
    depends=["globalAlg.h"]
)
setup(
    name="globalAlg",
    ext_modules=cythonize([examples_extension])
)
