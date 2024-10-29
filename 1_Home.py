import streamlit as st
import pandas as pd

st.set_page_config('Home', '🏠', 'wide')

st.title('Análise de Segmentação de Clientes - Gelateria Lillo')
st.write("""
Bem-vindo ao projeto de análise de segmentação de clientes da Gelateria Lillo. Este projeto visa explorar os dados fornecidos para gerar insights que ajudem a otimizar as campanhas de marketing e aumentar a receita da empresa. 
Abaixo, você pode visualizar os dados utilizados nesta análise.
""")

st.sidebar.markdown('Desenvolvido por Gabriel Kempp https://github.com/Gabrielkempp')

# Verifia se os dados ja foram carregados
if 'portfolio' not in st.session_state or 'clientes' not in st.session_state or 'eventos' not in st.session_state or 'data_null' not in st.session_state:
    # Carregar os dados
    portfolio = pd.read_excel('dados/portfolio_ofertas.xlsx', index_col='Unnamed: 0')
    clientes = pd.read_csv('dados/dados_clientes.csv', sep=',', index_col='Unnamed: 0')
    eventos = pd.read_csv('dados/eventos_ofertas.csv', sep=',', encoding='ISO-8859-1', index_col='Unnamed: 0')

    # Limpeza de dados
    clientes = clientes.dropna()
    # Convertendo a data de 'membro desde'
    clientes['membro_desde'] = pd.to_datetime(clientes['membro_desde'], format='%Y%m%d')

    # Armazenar dados no session_state para uso nas outras paginas
    st.session_state['portfolio'] = portfolio
    st.session_state['clientes'] = clientes
    st.session_state['eventos'] = eventos

# Acessando os dados armazenados no session_state
portfolio = st.session_state['portfolio']
clientes = st.session_state['clientes']
eventos = st.session_state['eventos']

# Checkbox para visualização de dados
if st.checkbox("Visualizar dados brutos"):
    col1,col2 = st.columns(2)
    col1.subheader('Dados de Clientes')
    col1.write(clientes)
    col2.subheader('Dados demográficos:')
    col2.markdown(
        '''· **Gênero**: gênero do cliente\n
· **Idade**: idade dos clientes\n
· **Id**: código único de cada cliente\n
· **Membro desde**: data em que o cliente criou uma conta\n
· **Renda anual**: renda anual fornecida pelo cliente.''')
    
    st.divider()

    col3, col4 = st.columns(2)
    col3.subheader('Portfólio de Ofertas')
    col3.write(portfolio)
    col4.subheader('Ofertas que são enviadas')
    col4.markdown(
        '''· **Recompensa**: pontuação obtida por completar a compra da oferta\n
· **Canal**: canal de envio da comunicação podendo ser e-mail, web, celular e redes sociais.\n
· **Valor mínimo**: valor mínimo necessário a ser gasto para aproveitar a oferta\n
· **Duração**: tempo de duração da oferta em dias.\n
· **Oferta**: Tipo de oferta enviada, podendo ser informativo, desconto e compre 1 e leve 2.\n
· **ID**: código de identificação da oferta
''')
    
    st.divider()
    
    col5, col6 = st.columns(2)
    col5.subheader('Eventos de Ofertas')
    col5.write(eventos)
    col6.subheader('Base com registros de todos os eventos')
    col6.markdown('''· **Tipo evento**: descrição dos eventos ocorridos, podendo ser: transação, oferta recebida, oferta vista, oferta finalizada.\n
· **Cliente**: código do cliente que executou aquele evento\n
· **Tempo decorrido**: tempo em horas desde o envio da oferta\n
· **Valor**: contém informação do valor gasto na compra\n
· **id oferta**: código da oferta
''')