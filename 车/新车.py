# main.py -- put your code here!
from pyb import Pin
N1 = Pin('Y1', Pin.OUT_PP)
N2 = Pin('Y2', Pin.OUT_PP)
N3 = Pin('Y3', Pin.OUT_PP)
N4 = Pin('Y4', Pin.OUT_PP)
N5 = Pin('Y6', Pin.OUT_PP)
N6 = Pin('Y7', Pin.OUT_PP)
N7 = Pin('Y8', Pin.OUT_PP)
N8 = Pin('Y9', Pin.OUT_PP)

N1.value(0)
N2.value(1)

N3.value(0)
N4.value(1)

N6.value(1)
N5.value(0)

N8.value(0)
N7.value(1)