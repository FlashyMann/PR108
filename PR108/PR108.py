import csv
import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as po

df=pd.read_csv("Bell.csv")
fig=ff.create_distplot([df["Avg Rating"].tolist()],["Avg Rating"])
fig.show()