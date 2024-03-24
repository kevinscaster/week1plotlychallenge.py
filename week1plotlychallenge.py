#imported all the needed libraries
import plotly.express as px  
import plotly.graph_objects as go
import pandas as pd            
#Imported the correct csv file using pandas 
#%%
df = pd.read_csv(r"/Users/kevin.caster/Desktop/Homework School/Week 1 data wrangling/AirPassengers.csv")
#Line Plot using the Data from the CSV File
#%%
fig1 = px.line(df, x='Month', y='#Passengers', title='AirPassengers')
fig1.show()
#%%
#Bar Chart using the Data from the CSV File
fig2 = px.bar(df, x='Month', y='#Passengers', title='AirPasasengers')
fig2.show()
#%%
#Histogram using the Data from the CSV File
fig3 = px.histogram(df, x='Month', y='#Passengers', title='AirPassengers')
fig3.show()
#%%
#Line Chart in Plotly Graph Objects using the Data from the CSV File
fig4 = go.Figure()
fig4.add_trace(go.Scatter(x=df['Month'], y=df['#Passengers'], mode='lines', name='AirPassengers'))
fig4.show()
#%%
#updated Layout 
fig4 = go.Figure()
fig4.add_trace(go.Scatter(x=df['Month'], y=df['#Passengers'], mode='lines', name='AirPassengers'))
lines=dict(color='red')
fig4.update_layout(
xaxis=dict(title='Month', showgrid= True, gridcolor='black'),
yaxis=dict(title='#Passengers', showgrid=True, gridcolor ='green'),
plot_bgcolor='rgba(0,0,0,0)',
showlegend=True,
legend=dict(x=0, y=1.0))
fig4.show()
#%%
#Bar Chart in Plotly Graph Objects using the Data from the CSV File
fig5= go.Figure()
fig5.add_trace(go.Bar(x=df['Month'], y=df['#Passengers'], mode='lines', name='AirPassengers'))
fig5.show()
#%%f
fig5 = go.Figure()
fig5.add_trace(go.Scatter(x=df['Month'], y=df['#Passengers'], mode='markers+lines', name='AirPassengers'))
#updated Layout 
markers=dict(symbol='dot')
lines=dict(color='red')
fig5.update_layout(
xaxis=dict(title='Month', showgrid= True, gridcolor='coral'),
yaxis=dict(title='#Passengers', showgrid=True, gridcolor ='blue'),
plot_bgcolor='lightgrey',
showlegend=True,
legend=dict(x=0, y=1.0))
fig5.show()
#%%
#Histogram in Plotly Graph Objects using the Data from the CSV File
fig6 = go.Figure()
fig6.add_trace(go.Histogram(x=df['Month'], y=df['#Passengers'], mode='lines', name='AirPassengers'))
fig6.show() 
#%%
#updated layout
fig6 = go.Figure()
fig6.add_trace(go.histogram(x=df['Month'], y=df['#Passengers'], mode='lines', name='AirPassengers'))
#updated Layout 
lines=dict(color='red')
fig6.update_layout(
xaxis=dict(title='Month', showgrid= True, gridcolor='red'),
yaxis=dict(title='#Passengers', showgrid=True, gridcolor ='yellow')
fig6.show()

#Comments/Notes

# The simplest for me was plotly express.
# I really enjoyed being able to custom,ize the graphs in go. 
# This was fun for me. 