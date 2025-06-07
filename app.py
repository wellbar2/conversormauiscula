import streamlit as st

st.title("Exemplo de upload, manipulação e download de arquivo")

arquivoUpload = st.file_uploader("Faça o upload de um arquivo .txt", type="txt")


if arquivoUpload is not None:
    conteudo = arquivoUpload.read().decode("utf-8")

    linhas = conteudo.splitlines()
    maiusculas = []
    st.subheader("Linhas convertidas para MAIÚSCULAS")
    for linha in linhas:
        st.text(str(linha).upper())
        maiusculas.append(str(linha).upper())


    conteudoProcessado = "\n".join(maiusculas)

    st.download_button("Baixar arquivo convertido para MAIÚSCULAS",
                       data=conteudoProcessado,
                       file_name="arquivo_CONVERTIDO.txt")