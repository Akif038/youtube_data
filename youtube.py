# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 14:30:31 2022

@author: Mehmet Akif
"""

import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import dataframe_image as dfi

youtube = pd.DataFrame(pd.read_csv("C:/Users/Mehmet Akif/OneDrive/Masaüstü/Excel Files/top_200_youtubers.csv"))

youtube["Category"].fillna("Other",inplace = True)
youtube["Category"].replace(["None"],"Other",inplace=True)


def scatter_plot():
    #forming a joint plot showing the relationship betweeen number of likes and number of followers.
    sns.set_theme(style="darkgrid")
    sns.jointplot(x="followers",y="Likes",data=youtube,hue= "Category")
    plt.xlabel("Followers")
    plt.savefig("youtubescatter.pdf", format="pdf", bbox_inches="tight")
    plt.show()
def hist_plot():
    #forming a histogram based on the categories
    sns.set_theme(style="darkgrid")
    sns.histplot(youtube["Category"],kde=True,bins="15",color="purple")
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=45)
    plt.savefig("category_hist.pdf", format="pdf", bbox_inches="tight")

def get_data():
    #getting an outlook from the DataFrame
    data2 = youtube.iloc[:,0:10]
    smp = data2.sample(n=20)
    smp_t = smp.style.background_gradient() #adding a gradient based on values in cell
    dfi.export(smp_t,"mytable_youtube.png")


scatter_plot()
hist_plot()

