"""
    Adam Heitzman

    ISTA 131 Final Project

    Visualization code #1. Mode 1 plots number of view vs number of likes and dislikes on respective
    subplots, also showing regression lines. Mode 2 does the same but overlapping on one plot.Interesting 
    to note how the like/comment ratio follows a number of distinct trend lines, as opposed to points being 
    randomly scattered.
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
import seaborn as sns
from matplotlib import pyplot as plt

"""
    Open CSV and calls user input to select mode.
    Enter 1 to display views vs likes and views vs dislikes as two separate subplots.
    Enter 2 to display views vs likes and dislikes overlapping on one plot.
    Will call appropriate functions following input.
"""
def setup():
    csv = pd.read_csv('./datasets/USvideos.csv')
    mode = input("Mode? (1/2)\nEnter 1 for likes/dislikes on separate subplots and 2 for likes/dislikes overlapping.\n")
    if mode == "1":
        print("Processing your visualization...")
        make_subplots(csv)
    elif mode == "2":
        print("Processing your visualization...")
        make_plot(csv)
    else:
        print('Invalid input. Please enter either "1" or "2".')
        exit()

"""
    Makes subplots to compare view count vs likes and dislikes, showing a regression line for each.
    Initializes plots, sets custom axes and labels, saves the image, and shows the final output.
"""
def make_subplots(csv):
    x = csv.views
    y = csv.likes
    z = csv.dislikes

    f = plt.figure(figsize=(12, 8))
    gs = f.add_gridspec(2, 1)

    # Makes views vs likes subplot using Seaborn's darkgrid style.
    with sns.axes_style("darkgrid"):
        ax = f.add_subplot(gs[0, 0])
        plot = sns.regplot(x=x, y=y, data=csv, scatter_kws={'s':4}, line_kws={"color": "red"})
        plot.set_xlabel('Views (in millions)', fontsize=12)
        plot.set_ylabel('Likes (in millions)', fontsize=12)
        plot.set_title('Views vs Likes', fontsize=15, weight=600)
        plt.xticks([0, 25000000, 50000000, 75000000, 100000000, 125000000, 150000000, 175000000, 200000000, 225000000],\
            [0, 25, 50, 75, 100, 125, 150, 175, 200, 225])
        plt.yticks([0, 1000000, 2000000, 3000000, 4000000, 5000000, 6000000],\
            [0, 1, 2, 3, 4, 5, 6])

    # Makes views vs dislikes subplot using Seaborn's darkgrid style.
    with sns.axes_style("darkgrid"):
        ax = f.add_subplot(gs[1, 0])
        plot2 = sns.regplot(x=x, y=z, data=csv, scatter_kws={'s':4}, line_kws={"color": "red"})
        plot2.set_xlabel('Views (in millions)', fontsize=12)
        plot2.set_ylabel('Dislikes (in millions)', fontsize=12)
        plot2.set_title('Views vs Dislikes', fontsize=15, weight=600)
        plt.xticks([0, 25000000, 50000000, 75000000, 100000000, 125000000, 150000000, 175000000, 200000000, 225000000],\
            [0, 25, 50, 75, 100, 125, 150, 175, 200, 225])
        plt.yticks([0, 200000, 400000, 600000, 800000, 1000000, 1200000, 1400000, 1600000, 1800000],\
            [0, .2, .4, .6 , .8, 1, 1.2, 1.4, 1.6, 1.8])
    f.tight_layout()

    plt.savefig('ADAM_VIS1.png', bbox_inches="tight", dpi=600)
    print('-----')
    print('Figure has been saved as ADAM_VIS1.png')
    print('-----')
    plt.show()

"""
    Plots views vs likes AND dislikes on one plot where the latter overlap.
    Initializes plot, sets custom axes and labels, saves the image, and shows the final output.
"""
def make_plot(csv):
    x = csv.views
    y = csv.likes
    z = csv.dislikes

    # Makes views vs likes and dislikes regplot using Seaborn's darkgrid style.
    with sns.axes_style("darkgrid"):
        plot = sns.regplot(x=x, y=y, data=csv, scatter_kws={'s':2})
        plot2 = sns.regplot(x=x, y=z, data=csv, scatter_kws={'s':2})
        plot.set_xlabel('Views (in millions)', fontsize=12)
        plot.set_ylabel('Likes / Dislikes (in millions)', fontsize=12)
        plot.set_title('Views vs Likes / Dislikes', fontsize=15, weight=600)
        plt.xticks([0, 25000000, 50000000, 75000000, 100000000, 125000000, 150000000, 175000000, 200000000, 225000000],\
            [0, 25, 50, 75, 100, 125, 150, 175, 200, 225])
        plt.yticks([0, 1000000, 2000000, 3000000, 4000000, 5000000, 6000000],\
            [0, 1, 2, 3, 4, 5, 6])
        plt.legend(labels=["Likes","Dislikes"])

    plt.savefig('ADAM_VIS1-ALT.png', bbox_inches="tight", dpi=600)
    print('-----')
    print('Figure has been saved as ADAM_VIS1-ALT.png')
    print('-----')
    plt.show()

"""
    Automatically calls setup when program starts
"""
def main():
    setup()

if __name__ == "__main__":
    main()

# OLD XTICK SETTINGS
# plt.xticks([0, 20000000, 40000000, 60000000, 80000000, 100000000, 120000000, 140000000, 160000000, 180000000, 200000000, 220000000, 240000000],\
#             [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240])