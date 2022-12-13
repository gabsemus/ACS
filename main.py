import streamlit as st

st.title('Agente Comunitário de Saúde')

st.header('Arquivo de dados de Produção:')

st.subheader('Ficha de Cadastro Domiciliar')

with st.expander("Operações"):
    st.checkbox('Visualizar')
    st.checkbox('Incluir')
    st.checkbox('Alterar')
    st.checkbox('Inativar')

st.subheader('Ficha de Cadastro Individual')

with st.expander("Operações "):
    st.checkbox('Incluir ')
    st.checkbox('Alterar ')

st.subheader('Ficha de Visita Domiciliar')

with st.expander("Fluxo  "):
    st.checkbox('1- Selecionar o Domícilio  ')
    st.checkbox('2- Selecionar Membros  ')
    st.checkbox('3- Atualizar o Cadastro dos Usuários  ')
    st.checkbox('4- Formulários de Ações (situacional) ')

with st.expander("Operações  "):
    st.checkbox('Incluir  ')
    st.checkbox('Visualizar  ')
    st.checkbox('Alterar  ')

st.write('')
st.write('Referência: ')
st.write("[Ficha de Cadastro Domiciliar](https://integracao.esusab.ufsc.br/ledi/documentacao/estrutura_arquivos/dicionario-fci.html)")
st.write("[Ficha de Cadastro Individual](https://integracao.esusab.ufsc.br/ledi/documentacao/estrutura_arquivos/dicionario-fcd.html)")
st.write("[Ficha de Visita Domiciliar](https://integracao.esusab.ufsc.br/ledi/documentacao/estrutura_arquivos/dicionario-fvd.html)")


st.header("Bônus")
with st.expander("Sistema Pronto"):
    st.write('Cadastro de Atendimento')
    st.checkbox('Visualizar    ')
    st.checkbox('Incluir   ')
    st.checkbox('Alterar   ')
    st.checkbox('Registrar Óbito   ')

with st.expander("DesempenhaSUS"):
    st.checkbox('Relatórios de Busca Ativa')
    st.checkbox('Inconsistências da Unidade')




