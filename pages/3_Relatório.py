import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config('Relatório', '📈', 'wide')

# Acessar dados armazenados no session_state
clientes = st.session_state['clientes']
eventos = st.session_state['eventos']

caminho_arquivo = os.path.join(os.getcwd(), 'pages/relatorio.md')

# Abrindo e lendo o arquivo
with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()

# Exibindo o conteúdo em Markdown no Streamlit
st.markdown(conteudo)