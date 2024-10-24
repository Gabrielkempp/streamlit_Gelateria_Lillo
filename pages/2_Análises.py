import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config('Análise', '📊', 'wide')

# Acessar dados armazenados no session_state
clientes = st.session_state['clientes']
eventos = st.session_state['eventos']
portfolio = st.session_state['portfolio']

st.title('Análise')

# Gráfico 1
col1, col2 = st.columns(2)
fig1 = px.histogram(clientes, x='idade', nbins=20, title='Qauntidade de clientes por idade')
col1.plotly_chart(fig1)

# Gráfico 2
fig3 = px.histogram(clientes, x='renda_anual', nbins=20, title='Distribuição de Renda Anual')
col2.plotly_chart(fig3)

# Gráfico 3
col3, col4 = st.columns(2)
fig2 = px.pie(clientes, names='genero', title='Distribuição por Gênero')
col3.plotly_chart(fig2)

# Visão geral gráfico 3
col4.subheader('Visão Geral sobre Generos')
col4.write("""Embora esteja um pouco equilibrado, os perfis de genero masculino tendem a ser maior que o feminino em quantidade.\n\n
**Homens: 57,2%**\n
**Mulheres: 41,3%**\n\n
O equilíbrio entre os gêneros oferece oportunidades de segmentação direcionada para campanhas de marketing mais personalizadas.""")

#Grafico 4
col5, col6 = st.columns([0.7,0.3])
# Filtra os eventos de transação
eventos_transacoes = eventos[eventos['tipo_evento'] == 'transacao']
# Preenche os valores nulos na coluna 'valor' com zero
eventos_transacoes['valor'].fillna(0, inplace=True)
# Junta as tabelas pelos IDs dos clientes
dados = eventos_transacoes.merge(clientes, left_on='cliente', right_on='id')
# Agrupa por gênero e idade e calcula o total gasto por grupo demográfico
gasto_por_genero_idade = dados.groupby(['genero', 'idade'])['valor'].sum().reset_index()
# Exibe os dados em um gráfico de barras
fig = px.bar(gasto_por_genero_idade, x='idade', y='valor', color='genero', barmode='group', 
             title='Valor Gasto por Gênero e Idade', 
             labels={'valor': 'Valor Gasto', 'idade': 'Idade', 'genero': 'Gênero'})
col5.plotly_chart(fig)
col6.subheader(' ')
col6.subheader('Visão Geral')
col6.write("""A análise revelou uma predominância de clientes do gênero masculino até 47 anos e, a partir desta idade, as mulheres passam a ser a maioria em muitas das faixas etárias.""")
