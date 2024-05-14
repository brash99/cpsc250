print("Environment:")
print("-----------------")

sys_values = True
if (sys_values):
    import sys
    print("sys.executable: ", sys.executable)
    print("-----------------")
    from pprint import pprint as p
    p(sys.path)

print("-----------------")
print("Imports:")
from mpl_toolkits.mplot3d import Axes3D
from pprint import pprint
from sympy.vector import CoordSys3D
import sys  
import os   
from array import array 
from functools import lru_cache 
from matplotlib import cm as cm
from mpl_toolkits.axes_grid1 import make_axes_locatable 
from mpl_toolkits.mplot3d import Axes3D 
from scipy import integrate 
from scipy import signal 
from scipy.fftpack import fft 
from scipy.integrate import dblquad 
from scipy.integrate import tplquad 
from scipy.optimize import fsolve 
from scipy.special import gamma 
from scipy.special import gamma, factorial
from sympy.vector import CoordSys3D 
from timer import Timer 
import decimal as dec 
import librosa   
import librosa.display   
import math   
import matplotlib.animation as animation 
import matplotlib.pyplot as plt 
import numpy as np 
import numpy.random as random 
import pandas as pd 
import platform   
import random   
import rk_functions as rk 
import sympy as sp 
import time
print("-----------------")
print("Done.")

