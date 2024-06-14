import streamlit as st
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import plotly.figure_factory as ff




df = pd.read_csv("euro2024_players.csv")
print("The shape of the data = {}".format(df.shape))
print("The top 5 rows of the date are:")
print(df.head())

st.title("Euro 2024 - Analysis")
cgoals = df.groupby(by = ["Country"])["Goals"].apply("sum")

st.write("Total Number of Goals scored by each Country")
st.line_chart(cgoals)
st.write("X-axis: Country")

st.write("Average height of players with respect to country")
st.line_chart(df.groupby(by = ["Country"])["Age"].apply("mean"))
st.write("X-axis: Country")

positions = {
  "Goalkeeper": "Defence",
  "Centre-Back": "Defence",
  "Full-Back": "Defence",
  "Left-Back" : "Defence",
  "Right-Back" : "Defence",
  "Defensive Midfielder": "Midfield",
  "Central Midfielder": "Midfield",
  "Attacking Midfielder": "Midfield",
  "Right Midfield" : "Midfield",
  "Left Midfield" : "Midfield",
  "Second Striker" : "Attack",
  "Centre-Forward" : "Attack",
  "Left Winger" : "Attack",
  "Right Winger" : "Attack"
}

df["PlayType"] = df.Position.map(positions)
st.write("Number of Players at each position for each country")
st.line_chart(df.groupby(['Country', 'PlayType']).size().unstack(fill_value=0))
st.write("X-axis: Country")

st.line_chart(df.Club.value_counts(ascending = False)[:10])
st.line_chart(df.Club.value_counts(ascending = True)[:10])

feature_counts = df.PlayType.value_counts()
# fig = px.pie(feature_counts, values=feature_counts.values, names=feature_counts.index, color_discrete_sequence=px.colors.sequential.RdBu)
# fig.update_traces(textposition='inside', textinfo='percent+label')
# fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
fig = go.Figure(data=[go.Pie(labels=feature_counts.index, values=feature_counts.values, hole=.3, pull = [0.1, 0 ,0])])
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
st.plotly_chart(fig)

st.bar_chart(df.Position.value_counts())
st.bar_chart(df.groupby(['Country', 'Position']).size().unstack(fill_value=0))

countries = df['Country'].unique()
plot_type = ["boxplot", "histogram", "mixed"]
# Sidebar for country selection
selected_country = st.selectbox("Select Country", countries)
selected_plot = st.selectbox("Select Plot", plot_type)
filtered_df = df[df['Country'] == selected_country]
st.header("Plot of Age Distribution")
if selected_plot == "boxplot":
    fig = px.box(filtered_df['Age'])
elif selected_plot == "histogram":
    fig = px.histogram(filtered_df['Age'])
else:
    fig = px.histogram(filtered_df['Age'], marginal="box")

# st.pyplot(fig, hidden=True)  # Hide initially
 # Check if a country is selected (not the default option)
st.plotly_chart(fig, hidden=True)


st.header("Plot of Height Distribution")
if selected_plot == "boxplot":
    fig = px.box(filtered_df['Height'])
elif selected_plot == "histogram":
    fig = px.histogram(filtered_df['Height'])
else:
    fig = px.histogram(filtered_df['Height'], marginal="box")

# st.pyplot(fig, hidden=True)  # Hide initially
 # Check if a country is selected (not the default option)
st.plotly_chart(fig)

st.header("Plot of Caps Distribution")
if selected_plot == "boxplot":
    fig = px.box(filtered_df['Caps'])
elif selected_plot == "histogram":
    fig = px.histogram(filtered_df['Caps'])
else:
    fig = px.histogram(filtered_df['Caps'], marginal="box")

# st.pyplot(fig, hidden=True)  # Hide initially
 # Check if a country is selected (not the default option)
st.plotly_chart(fig)

st.header("Plot of MarketValue Distribution")
if selected_plot == "boxplot":
    fig = px.box(filtered_df['MarketValue'])
elif selected_plot == "histogram":
    fig = px.histogram(filtered_df['MarketValue'])
else:
    fig = px.histogram(filtered_df['MarketValue'], marginal="box")

# st.pyplot(fig, hidden=True)  # Hide initially
 # Check if a country is selected (not the default option)
st.plotly_chart(fig)

st.write("Foot vs Country")
st.bar_chart(df.groupby(by = ["Country", "Foot"]).size().unstack(fill_value = 0))

st.line_chart(df.groupby(by = ["Country", "PlayType", ])["Goals"].sum().unstack(fill_value=0))

