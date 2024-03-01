import streamlit as st
from scripts.pandasagent import get_llm_response
from scripts.pocv1 import *
from scripts.pocv2 import get_df, get_map

st.set_page_config(page_title="POC VR", page_icon="🦜")
st.title("POC VR 🦜")

if "btn2" not in st.session_state:
    st.session_state.btn2 = False

with st.sidebar.form("Input"):
    queryText = st.text_input("Endereço",
                              placeholder="Rua N QNN 26 - Ceilândia, Brasília",
                              max_chars=None)
    queryRadius = st.slider("Raio (em km)",
                            min_value=1,
                            max_value=100,
                            help="Deve ser um valor de 1 a 100 km")

    c1, c2 = st.columns(2)
    with c1:
        btnResult = st.form_submit_button('Resumo')
    with c2:
        btnResult2 = st.form_submit_button('Chat BOT')

if btnResult:
    with st.spinner("Resgatando dados..."):
        try:
            df = get_df(queryText, queryRadius)

            st.session_state.btn2 = False
            if len(df['estabelecimento'].drop_duplicates()) > 3:
                info_c1, info_c2 = st.columns(2)
                with info_c1:
                    st.write(get_estabelecimentos(df, queryRadius))
                    st.write(get_ticket_medio(df))
                    st.write(get_valor_mediano_tickets(df))

                with info_c2:
                    st.write(get_numero_transacoes(df))
                    st.write(get_quantidade_clientes(df))

                small_c1, small_c2 = st.columns(2, gap="small")
                with st.container():
                    small_c1.pyplot(plot_heatmap(df).figure)
                    small_c2.pyplot(plot_hist(df))

                st.pyplot(plot_line(df))

                st.map(get_map(queryText), latitude="lat", longitude="long", size=queryRadius * 1000, color=[96, 255, 93, 0.3])

            else:
                st.write("Não foi possível encontrar estabelecimentos no endereço/área solicitada.")

        except AttributeError as e:
            st.write("Não foi possível encontrar estabelecimentos no endereço/área solicitada.")
            print(e)

if btnResult2 or st.session_state.btn2:
    st.session_state.btn2 = True

    df = get_df(queryText, queryRadius)

    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "Como posso te ajudar?"}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input(placeholder="Digite aqui sua pergunta..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        with st.spinner("Gerando resposta..."):
            response = get_llm_response(df, prompt)

        with st.chat_message("assistant"):
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.write(response)

