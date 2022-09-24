import seaborn as sns
# sns.load_dataset("iris")
# df_iris= sns.load_dataset("iris")
# # df_iris # anyway to see the dataset in VScode?
import plotly.express as px
import streamlit as st

df = px.data.iris()
fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width',
              color='petal_length', size='petal_length', size_max=13,
              symbol='species', opacity=0.7)
fig.show()
st.pyplot_chart(fig)
