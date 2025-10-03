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

build_histogram = st.checkbox('Criar um histograma')

if build_histogram:
        age_counts = war_data.groupby('age')["id"].count().reset_index(name='deaths') 
        fig_scatter_age = px.scatter(
        age_counts,
        x='age',          
        y='deaths',       
        size='deaths',    
        title='Number of Deaths by Age in Gaza',
        labels={'age': 'Age', 'deaths': 'Number of Deaths'},
        hover_data={'age': True, 'deaths': True}  
        )
        st.plotly_chart(fig_scatter_age, use_container_width=True)

        st.write('Criando um histograma para a coluna de idade')