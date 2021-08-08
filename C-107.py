import pandas as pd
import csv
import plotly.graph_objects as go

df=pd.read_csv("data.csv")
m=df.groupby("level")["attempt"].mean()
print(m)

fig=go.Figure(go.Bar(y=m, x=["Level 1", "Level 2", "Level 3", "Level 4"], orientation="v"))
fig.show()