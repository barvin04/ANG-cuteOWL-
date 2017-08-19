import numpy as np
import matplotlib.pyplot as plt

inp = open('ex1data1.txt', 'r')
data = inp.readlines()
data[:] = (value for value in data if value != '\n')

