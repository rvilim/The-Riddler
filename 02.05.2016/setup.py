from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy as np                           # <---- New line

ext_modules = [Extension("matchup", ["matchup.pyx"])]

setup(
  name = 'castles',
  cmdclass = {'build_ext': build_ext},
  include_dirs = [np.get_include()],         # <---- New line
  ext_modules=ext_modules,
  extra_compile_args=["-O3", "-ffast-math", "-march=native", "-fopenmp"],
  extra_link_args=['-fopenmp']
)