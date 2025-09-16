from textblob import TextBlob
import streamlit as st

st.set_page_config(page_title="Analisador de Sentimentos", layout="centered")
st.title("📝 Analisador de Sentimentos Intermediario")

st.write("Digite um texto abaixo e descubra se ele é positivo, negativo ou neutro, além de ver estatísticas e resumo.")

# Input do usuário
texto = st.text_area("Digite seu texto aqui:")

if st.button("Analisar"):
    if not texto.strip():
        st.warning("Por favor, digite algum texto antes de analisar.")
    else:
        analise = TextBlob(texto)
        polaridade = analise.sentiment.polarity
        subjetividade = analise.sentiment.subjectivity

        # Determinar sentimento
        if polaridade > 0:
            st.success(f"Sentimento Positivo 😊 (Polaridade: {polaridade:.2f})")
        elif polaridade < 0:
            st.error(f"Sentimento Negativo 😞 (Polaridade: {polaridade:.2f})")
        else:
            st.info(f"Sentimento Neutro 😐 (Polaridade: {polaridade:.2f})")
        
        # Mostrar subjetividade
        st.info(f"Subjetividade: {subjetividade:.2f} (0 = Objetivo, 1 = Subjetivo)")

        # Estatísticas adicionais
        palavras = texto.split()
        st.write(f"📊 Número de palavras: {len(palavras)}")
        st.write(f"📊 Número de caracteres: {len(texto)}")

        # Resumo simples (primeira frase)
        primeira_frase = texto.split(".")[0]
        st.write(f"📝 Resumo (primeira frase): {primeira_frase.strip()}")
