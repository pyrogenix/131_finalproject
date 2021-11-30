"""
    Adam Heitzman

    ISTA 131 Final Project

    Visualization code #2. Takes a CSV of data on trending YouTube videos in the
    US and displays the number of videos in each categorey as a bar graph. It is
    clear that certain "genres" of videos are vastly more popular, with some categories
    having close to no videos that ever reach the trending page.
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
import seaborn as sns
from matplotlib import pyplot as plt

"""
    Imports the dataset into Pandas and calls 'categorize' function.
"""
def setup():
    csv = pd.read_csv('./datasets/USvideos.csv')
    categorize(csv)

"""
    Creates a new column with the corresponding names of each category_id.
    Calls the 'makeplot' function to display the visualization.
"""
def categorize(csv):
    csv['cat_name'] = np.nan
    csv.loc[(csv["category_id"] == 1),"cat_name"] = 'Film and Animation'
    csv.loc[(csv["category_id"] == 2),"cat_name"] = 'Cars and Vehicles'
    csv.loc[(csv["category_id"] == 10),"cat_name"] = 'Music'
    csv.loc[(csv["category_id"] == 15),"cat_name"] = 'Pets and Animals'
    csv.loc[(csv["category_id"] == 17),"cat_name"] = 'Sport'
    csv.loc[(csv["category_id"] == 19),"cat_name"] = 'Travel and Events'
    csv.loc[(csv["category_id"] == 20),"cat_name"] = 'Gaming'
    csv.loc[(csv["category_id"] == 22),"cat_name"] = 'People and Blogs'
    csv.loc[(csv["category_id"] == 23),"cat_name"] = 'Comedy'
    csv.loc[(csv["category_id"] == 24),"cat_name"] = 'Entertainment'
    csv.loc[(csv["category_id"] == 25),"cat_name"] = 'News and Politics'
    csv.loc[(csv["category_id"] == 26),"cat_name"] = 'How to and Style'
    csv.loc[(csv["category_id"] == 27),"cat_name"] = 'Education'
    csv.loc[(csv["category_id"] == 28),"cat_name"] = 'Science and Technology'
    csv.loc[(csv["category_id"] == 29),"cat_name"] = 'Non Profits and Activism'
    csv.loc[(csv["category_id"] == 25),"cat_name"] = 'News & Politics'
    makeplot(csv)

"""
    Uses Seaborn to make a lineplot showing the number videos in each category.
    Saves image and calls plt.show() to display the plot.
"""
def makeplot(csv):
    sns.set_style("darkgrid")
    sns.set(rc={"figure.figsize":(8, 4)})

    x = csv.cat_name
    y = csv.views

    fig, ax1 = plt.subplots()

    ax2 = ax1.twinx()

    sns.countplot(x = x, data=csv, ax = ax1, palette="muted")
    sns.lineplot(x = x, y = y, ax = ax2, marker='o', palette="muted", data=csv)

    ax1.set_title("Metrics by Category", fontsize=15, weight=600)
    ax1.set_ylabel('Number of Videos')
    ax2.set_ylabel('Average View Count (in millions)')
    ax1.set_xlabel("Category", fontsize=12)

    ax1.set_xticklabels(ax1.get_xticklabels(),rotation = 90)
    ax2.yaxis.set_ticks([0, 1300000, 2600000, 3900000, 5200000, 6500000])
    ax2.grid(None)

    plt.savefig('ADAM_VIS2.png', bbox_inches="tight")
    print('-----')
    print('Figure has been saved as ADAM_VIS2.png')
    print('-----')
    plt.show()

"""
    Calls setup to start the script.
"""
def main():
    setup()


if __name__ == "__main__":
    main()