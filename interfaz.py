import streamlit as st
from langchain_ollama import ChatOllama

# Título de la aplicación
st.title("🔗🤝 Sepanka 1.0 (LLaMA 3.2 Fine-Tuned)")

# Inicializar el estado de los mensajes si no existe
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Mah cualli xihualacan / bienvenidos"}]

# Inicializar el estado del historial si no existe
if "history" not in st.session_state:
    st.session_state["history"] = [("system", "You are a helpful assistant that answers user's question")]

# Mostrar los mensajes previos
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

# Capturar el input del usuario de manera indefinida
if prompt := st.chat_input("tlajkuilouaj ipa ikanikan / Escribe justo aqui"):
    # Agregar el mensaje del usuario a los mensajes y al historial
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.session_state["history"].append(("human", prompt))
    st.chat_message("user").write(prompt)

    # Instanciar el modelo de ChatOllama
    llm = ChatOllama(
        model="llama3.2",
        temperature=0
    )

    # Generar la respuesta del modelo
    response = llm.invoke(st.session_state["history"])

    # Agregar la respuesta del asistente a los mensajes y al historial
    st.chat_message("assistant").write(response.content)
    st.session_state["messages"].append({"role": "assistant", "content": response.content})
    st.session_state["history"].append(("assistant", response.content))
