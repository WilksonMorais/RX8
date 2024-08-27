import streamlit as st

# Título do aplicativo
st.title("Mensagem de Amor")

# Campo de entrada para o usuário
mensagem = st.text_input("Digite sua mensagem de amor:", "")

# Quando o usuário digitar "Elaine eu te amo"
if mensagem == "Elaine eu te amo":
    st.success("Você digitou a mensagem correta! ❤️")
    st.write("❤️" * 50)  # Exibe vários corações

    st.write("Aqui estão algumas frases de amor:")
    
    # Lista de frases de amor
    frases = [
        "Você é a razão do meu sorriso.",
        "Te amo mais do que ontem e menos do que amanhã.",
        "Amar você é a melhor parte do meu dia.",
        "Você é meu sol em dias nublados.",
        "Seu amor é meu tesouro.",
        "Cada dia ao seu lado é um lindo dia.",
        "Você faz meu coração bater mais rápido.",
    ]
    
    # Exibe as frases de amor em um formato amigável
    for frase in frases:
        st.write("- " + frase)
else:
    st.warning("Por favor, digite 'Elaine eu te amo' para ver a mágica!")