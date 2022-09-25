import seaborn as sns
import plotly.express as px
import streamlit as st
df_iris= sns.load_dataset("iris")

fig = px.scatter_3d(df_iris, x='sepal_length', y='sepal_width', z='petal_width',
              color='petal_length', size='petal_length', size_max=13,
              symbol='species', opacity=0.7)

st.plotly_chart(fig)
st.text('1. The colors of dots show that the petal length of setosa is about 1 unit, that of versicolor is between 3 and 4, and that of virginica is between 5 and 6.')
st.text('2. The setosa species shows a positive correlation between the sepal_length and the sepal_width, while the petal_width is likely to have similar values regardless of the sepal_length and the sepal_width.')
st.text('3. The versicolor species demonstrates a positive correlation between the sepal_length and the sepal_width, the sepal_width and the petal_width, but it seems like there is no correlation between the sepal_lenth and the petal_width.')
st.text('4. The virginica species also shows a positive correlation between the sepal_length and the sepal_width, the sepal_width and the petal_width, but not in the sepal_lenth and the petal_width.')
