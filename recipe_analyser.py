# Please use Python version 2.7

# This script displays recipe information from cookpad

# author: Richard Kunert (rikunert@gmail.com) August 2017

import pickle # for saving
import numpy as np # for standard fast analyses
import plotly
import plotly.offline as po
import plotly.plotly as py
import plotly.graph_objs as go
# plotly.tools.set_credentials_file(username='rikunert', api_key='EG35XFgrKKxfb8t1up7K')
from collections import Counter
import operator  # for sorting
import networkx as nx
import matplotlib.pyplot as plt

# source translation
execfile("C:\Users\Richard\Desktop\python\\recipe_ingredients\ingredient_dictionary.py")

#dictionary updated for
# Dinner
# American
# Italian
# Mediterranean
# Latin American
# Mexican
# Asian
# Chinese

#read in recipes of all nations
# recipe_info = [0]*10
# nations = ['American','Chinese', 'Indian', 'Italian', 'Mexican', 'Thai', 'Asian', 'Latin_American', 'Mediterranean']
# for i, nation in enumerate(nations):
#
#     with open ('cookpad_recipe_info_'+nation+'.pickled', 'rb') as fp:
#         recipe_info[i] = pickle.load(fp)

with open ('cookpad_recipe_info_Chinese.pickled', 'rb') as fp:
         recipe_info = pickle.load(fp)
#exactly 2000 recipes because cookpad does not list more than 100 pages with each 20 recipes in each category

recipe_info = ingredient_translator(recipe_info)  # function can be found in ingredient_dictionary.py

#let's first get an idea of the recipe size
ingredients_count = [len(r['ingredients']) for r in recipe_info]
np.mean(ingredients_count)
np.median(ingredients_count)

data = [go.Histogram(x=ingredients_count)]
layout = layout = go.Layout(
    title='How many ingredients make up a dinner recipe?',
    xaxis=dict(
        title='Number of ingredients in each recipe'
    ),
    yaxis=dict(
        title='Number of recipes with x number of ingredients'
    ),
    bargap=0.1,
    bargroupgap=0.1,
    annotations=go.Annotations([
        go.Annotation(
            x=0,
            y=0,
            showarrow=False,
            text='<a href="https://twitter.com/rikunert">@rikunert</a>',
            xanchor = 'left',
            xref='paper',
            yref='paper'),
        go.Annotation(
            x=1,
            y=0,
            showarrow=False,
            text='source: <a href="https://cookpad.com">cookpad</a>',
            xanchor = 'right',
            xref='paper',
            yref='paper')
    ])
)
fig = go.Figure(data = data, layout = layout)
po.plot(fig, filename='file.html')
#py.iplot(data, filename='basic histogram')

# let's get an idea of how many times different ingredients actually occur
ingredients_recipe = [r['ingredients'] for r in recipe_info]
ingredients = [item.lower() for sublist in ingredients_recipe for item in sublist]
ingredients = Counter(ingredients)

# delete ingredients with low count
for k in list(ingredients):
        if ingredients[k] < 5:
            del ingredients[k]

#plotly bar chart

# turn ingredients into nodes (vertices) and recipes into edges (links) of a graph
G = nx.Graph()

for origin in ingredients:  # for each ingredient
    print origin
    for neighbour in ingredients:  # for each other ingredient
        if G.has_edge(origin, neighbour) is False:
            weight_counter = 0
            for recipe in recipe_info:  # for each recipe
                if origin != neighbour and origin in recipe['ingredients'] and neighbour in recipe['ingredients']:
                    weight_counter += 1
            if weight_counter > 0:  # if ingredients are connected through recipe
                G.add_edge(origin, neighbour, weight=weight_counter)

#save graph
# nx.write_gexf(G, 'Dinner_network.gexf')
# open gephi and analyse network there

nx.info(G)  # basic graph info
nx.draw_networkx(G, pos = nx.spring_layout(G), with_labels=True, node_size=10)

# degree centrality for nodes (how many nodes this node is connected to, divided by total number of nodes)
degr = nx.degree_centrality(G)
sorted_degr = sorted(degr.items(), key=operator.itemgetter(1))
sorted_degr.reverse()
sorted_degr
# What percentage of other ingredients this ingredient matches with

# closeness centrality
close = nx.closeness_centrality(G)
sorted_close = sorted(close.items(), key=operator.itemgetter(1))
sorted_close.reverse()
sorted_close
# the shortest distance of this ingredient to all the other ingredients
# What you should buy if you cook many different kind of dishes

# shortest-path betweenness centrality for nodes.
betw = nx.betweenness_centrality(G)
sorted_betw = sorted(betw.items(), key=operator.itemgetter(1))
sorted_betw.reverse()
sorted_betw
# High betweenness centrality means acting often as a bridge nodes for shortest paths of other nodes
# The ingredient you should buy if you want to cook wildly different kinds of dishes which are not connected by other ingredients





