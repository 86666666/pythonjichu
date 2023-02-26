from distutils.core import setup
from Cython.Build import cythonize
setup(
    name='ceshi Cython',
    ext_modules=cythonize(['examples_cy.pyx'])
)