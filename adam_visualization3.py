"""
    Adam Heitzman

    ISTA 131 Final Project

    Visualization code #3. Takes a CSV of data on trending YouTube videos in the
    US and ranks the top 20 channels by how many of their videos reached the trending
    page. Y-axis is limited to values between 150 and 210. It seems most channels to reach
    trending are massive corporations and TV personalities, although some independent youtubers
    such as Tom Scott made it to the top 20.
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
import seaborn as sns
from matplotlib import pyplot as plt
from textblob import TextBlob


"""
    Imports the dataset into Pandas and calls 'makeplot' function.
"""
def setup():
    csv = pd.read_csv('./datasets/USvideos.csv')
    makeplot(csv)

"""
    Uses Seaborn to make a bar plot ranking the top 20 channels by number of
    videos to hit the trending page.
    Saves image and calls plt.show() to display the plot.
"""
def makeplot(csv):
    a = csv.channel_title.value_counts().index.tolist()
    b = csv.channel_title.value_counts()

    sns.set_style("darkgrid")
    sns.set(rc={"figure.figsize":(8, 4)})

    f = sns.barplot(x=a[0:20], y=b[0:20], data=csv, palette="muted")
    f.set_xticklabels(f.get_xticklabels(),rotation = 90, fontsize=10)
    f.set_title("Top 20 Channels by Number of Trending Videos", fontsize=15, weight=600)
    f.set_xlabel("Channel Name", fontsize=12)
    f.set_ylabel("Number of Trending Videos", fontsize=12)
    plt.ylim([150,210])

    plt.savefig('ADAM_VIS3.png', bbox_inches="tight", dpi=600)
    print('-----')
    print('Figure has been saved as ADAM_VIS3.png')
    print('-----')
    plt.show()

"""
    Calls setup to start the script.
"""
def main():
    setup()


if __name__ == "__main__":
    main()