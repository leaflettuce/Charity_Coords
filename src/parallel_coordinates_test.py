# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 18:26:48 2018

@author: andyj
"""
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

df = pd.read_csv('./data/test.csv')

data = [
    go.Parcoords(
        line = dict(color = df['Annual Contributions'],
                   colorscale = [[0, '#CAD11A'],
                                [0.25,'#6EBE18'],
                                [0.5,'#B71752'],
                                [0.75, '#69178C'],
                                [1, '#DE9733']]),  
        dimensions = list([
            dict(range = [70,100],
                constraintrange = [85,100],
                label = 'Rating', values = df['Rating']),
            dict(range = [55,90],
                label = ' Program Expenses', values = df['Program Expenses']),
            dict(range = [0,0.5],
                label = 'Efficiency', values = df['Efficiency']),
            dict(range = [75, 100],
                label = 'Transparency', values = df['Accountability and Transparency'])
        ])
    )
]

layout = go.Layout(
    plot_bgcolor = '#E5E5E5',
    paper_bgcolor = '#E5E5E5'
)

fig = go.Figure(data = data, layout = layout)
py.iplot(fig, filename = 'parcoords-basic')