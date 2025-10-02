import pandas as pd
import plotly.express as px
import streamlit as st
        
war_data = pd.read_csv('killed-in-gaza.csv') # lendo os dados
hist_button = st.button('Criar histograma') # criar um botão
        
if hist_button: # se o botão for clicado
            # escrever uma mensagem 
    st.write('Criando um histograma para o conjunto de dados sobre mortes em Gaza')
            
            # criar um histograma
    fig = px.histogram(war_data, x="age")
        
            # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

    print("Olá")