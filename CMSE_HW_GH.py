import seaborn as sns
import plotly.express as px
import streamlit as st
df_iris= sns.load_dataset("iris")

fig = px.scatter_3d(df_iris, x='sepal_length', y='sepal_width', z='petal_width',
              color='petal_length', size='petal_length', size_max=13,
              symbol='species', opacity=0.7)

st.plotly_chart(fig)
