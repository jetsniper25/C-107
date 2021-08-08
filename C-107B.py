import pandas as pd
import csv
import plotly.graph_objects as go

df=pd.read_csv("data.csv")
m=df.groupby("level")["attempt"].mean()
print(m)

student=df.loc[df["student_id"]=="TRL_mda"]
print(student)
sm=student.groupby("level")["attempt"].mean()
print (sm)
fig=go.Figure(go.Bar(y=sm, x=["Level 1", "Level 2", "Level 3", "Level 4"], orientation="v"))
fig.show()

