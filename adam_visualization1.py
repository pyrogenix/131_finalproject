"""
    Adam Heitzman

    ISTA 131 Final Project

    Visualization code #1. Plots number of likes vs number of comments on a chart
    and shows regression line. Interesting to note how the like/comment ratio follows
    a number of distinct lines, as opposed to being randomly scattered.
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
import seaborn as sns
from matplotlib import pyplot as plt

def setup():
    csv = pd.read_csv('./datasets/USvideos.csv')
    makeplot(csv)

def makeplot(csv):
    x = csv.comment_count
    y = csv.likes
    sns.set(rc={"figure.figsize":(8, 4)})
    plot = sns.regplot(x, y, data=csv)
    plot.set_xlabel('Number of Comments (in millions)', fontsize=12)
    plot.set_ylabel('Number of Likes (in millions)', fontsize=12)
    plot.set_title('Likes vs Comments', fontsize=15, weight=600)
    plt.xticks([0, 200000, 400000, 600000, 800000, 1000000, 1200000, 1400000],[0, .2, .4, .6, .8, 1, 1.2, 1.4])
    plt.yticks([0, 1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000],[0, 1, 2, 3, 4, 5, 6, 7])
    plt.savefig('ADAM_VIS1.png', bbox_inches="tight")
    print('-----')
    print('Figure has been saved as ADAM_VIS1.png')
    print('-----')
    plt.show()


def main():
    setup()


if __name__ == "__main__":
    main()
