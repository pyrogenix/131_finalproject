"""
    Adam Heitzman

    ISTA 131 Final Project

    Visualization code #1. ...
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def setup():
    csv = pd.read_csv('./datasets/USvideos.csv')

def makeplot():
    plt.plot(csv.views, csv.likes)

def show():
    plt.show()

def main():
    setup()


if __name__ == "__main__":
    main()
