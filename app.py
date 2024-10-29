import streamlit as st
import random

# Función para generar un ejercicio de energía potencial
def generar_ejercicio():
    masa = random.randint(1, 10)  # Masa en kg
    altura = random.randint(1, 20)  # Altura en metros
    gravedad = 9.8  # Gravedad en m/s^2
    energia_potencial = masa * gravedad * altura
    return masa, altura, energia_potencial

# Título de la página
st.title("Ejercicios de Energía Potencial")

# Generar un ejercicio de ejemplo
masa, altura, energia_correcta = generar_ejercicio()
st.write(f"Un objeto de {masa} kg está a una altura de {altura} metros sobre el suelo. Calcula su energía potencial.")

# Input del usuario para la respuesta
respuesta_usuario = st.number_input("Ingresa la energía potencial en Joules:", min_value=0.0, step=0.1)

# Botón para verificar la respuesta
if st.button("Verificar"):
    if abs(respuesta_usuario - energia_correcta) < 0.1:
        st.success("¡Correcto! La respuesta es correcta.")
    else:
        st.error(f"Incorrecto. La respuesta correcta es {energia_correcta:.2f} Joules.")

