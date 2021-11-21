import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

csv = pd.read_csv('./datasets/USvideos.csv')

def makeplot():
    plt.plot(csv.views, csv.likes)

def show():
    plt.show()