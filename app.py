import streamlit as st # lib para criar a aplicação web
import pandas as pd # lib para manipulação de dados
from sklearn.linear_model import LinearRegression # lib para criar o modelo de regressão linear

df = pd.read_csv('pizzas.csv') # lendo o arquivo csv

modelo = LinearRegression() # instanciando o modelo de regressão linear
x = df[['diametro']]
y = df['preco']

modelo.fit(x, y) # treinando o modelo

st.title('Predição de Preço de Pizza') # título da aplicação
st.divider() # separador

diametro = st.number_input('Digite o diâmetro da pizza em cm:', min_value=0, max_value=50000000) # input para o usuário inserir o diâmetro da pizza

if diametro:
    preco = modelo.predict([[diametro]])[0] # predizendo o preço da pizza
    st.write(f'O preço da pizza com diâmetro de {diametro} cm é R${preco:.2f}') # exibindo o preço da pizza

st.balloons()