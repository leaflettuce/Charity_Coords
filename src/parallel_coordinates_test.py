# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 18:26:48 2018

@author: andyj
"""
import pandas as pd
import plotly 
import plotly.plotly as py
import plotly.graph_objs as go
import os

#Plotly credentials
plotly.tools.set_credentials_file(username='Andyjtrick', api_key= os.environ.get("PLOTLY_KEY"))


df = pd.read_csv('./data/test.csv')


data = [
    go.Parcoords(
        line = dict(color = df['cat_num'],
                   colorscale = [[0, '#6C9E12'], ## social services
                                [0.25,'#0D5F67'], ## humanitarian
                                [0.5,'#AA1B13'], ## health
                                [0.75, '#69178C'], ## environmentla
                                [1, '#DE9733']]),  ## animal rights
        dimensions = list([
            dict(range = [70,100],
                 constraintrange = [93,100],
                label = 'Charity Navigator Rating', values = df['Rating']),
            dict(range = [10000000, 800000000],
                label = 'Annual Contribution', values = df['Annual Contributions']),
            dict(range = [55,90],
                label = 'Revenue Percent to Programs', values = df['Program Expenses']),
            dict(range = [0,0.4],
                label = 'Fundraising Efficiency', values = df['Efficiency']),
            dict(range = [75, 100],
                label = 'Transparency', values = df['Accountability and Transparency']),
            dict(range = [0, 1.2],
                label = 'CEO Compensation Percent', values = df['CEO Comp Percent']),
            dict(range = [15000, 775000],
                label = 'CEO Compensation (Actual)', values = df['CEO Compensation'])
        ]),
            showlegend = True
    )
]

layout = go.Layout(
    autosize=False,
    width=1600,
    height=800,
    plot_bgcolor = '#E5E5E5',
    paper_bgcolor = '#E5E5E5',
    
    title='Charity Comparison Plot'
)

# Categorical Labels
labels = [
        dict(xref='paper', yref='paper', x=0.35, y=-0.085,
                              xanchor='center', yanchor='top',
                              text="Health",
                              font=dict(family='Arial',
                                        size=14,
                                        color='#AA1B13'),
                              showarrow=False),
        dict(xref='paper', yref='paper', x=0.5, y=-0.085,
                              xanchor='center', yanchor='top',
                              text="Social Services",
                              font=dict(family='Arial',
                                        size=14,
                                        color='#6C9E12'),
                              showarrow=False),
        dict(xref='paper', yref='paper', x=0.65, y=-0.085,
                              xanchor='center', yanchor='top',
                              text="Humanitarian",
                              font=dict(family='Arial',
                                        size=14,
                                        color='#0D5F67'),
                              showarrow=False),
        dict(xref='paper', yref='paper', x=0.20, y=-0.085,
                              xanchor='center', yanchor='top',
                              text="Environmental",
                              font=dict(family='Arial',
                                        size=14,
                                        color='#69178C'),
                              showarrow=False),
        dict(xref='paper', yref='paper', x=0.80, y=-0.085,
                              xanchor='center', yanchor='top',
                              text="Animal Rights",
                              font=dict(family='Arial',
                                        size=14,
                                        color='#DE9733'),
                              showarrow=False)
                              
        ]
layout['annotations'] = labels

# print the plot
fig = go.Figure(data = data, layout = layout)
py.iplot(fig, filename = 'Charity_Rough')