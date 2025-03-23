# Juego de Preguntas y Respuestas con Ranking de Puntajes

## 📌 Descripción
Este es un juego interactivo de preguntas y respuestas donde el usuario debe responder a 5 preguntas de opción múltiple. Cada pregunta tiene 3 respuestas posibles. El usuario tiene un tiempo limitado de 10 segundos para responder cada pregunta. Si el tiempo se acaba, se pasa automáticamente a la siguiente pregunta sin puntuar.

## 📌 Requisitos

### ✅ Pantallas
- **Inicio**: 
  - Un botón "Iniciar Juego" que permite al usuario comenzar la partida.
  
- **Juego**:
  - Muestra la pregunta actual.
  - Tres botones de respuesta para seleccionar la respuesta correcta.
  - Un temporizador de 10 segundos que cuenta regresivamente.
  - Muestra el puntaje actual y una barra de progreso que indica el avance del juego.

- **Resultados**:
  - Muestra el puntaje obtenido al final del juego.
  - Presenta los 3 mejores puntajes de la sesión.

### ✅ Lógica del Juego
- Utiliza una lista de preguntas y respuestas predefinidas.
- Si el usuario responde correctamente, se suma 1 punto y el fondo de la pantalla cambia a verde.
- Si el usuario responde incorrectamente, no se suman puntos y el fondo cambia a rojo.
- Si el temporizador llega a 0 segundos, se pasa automáticamente a la siguiente pregunta sin puntuar.
- Al finalizar el juego, se compara el puntaje obtenido con los 3 mejores puntajes de la sesión.

## 📌 Criterios de Evaluación
- ✔️ Implementación del temporizador de 10 segundos.
- ✔️ Comparación de puntajes sin almacenamiento persistente.
- ✔️ Uso de listas y validación de respuestas.

## 📌 Tecnologías Utilizadas
- Python
- Flet (para la interfaz gráfica)

## 📌 Cómo Ejecutar el Proyecto
1. Clona este repositorio en tu máquina local.
   ```bash
   git clone https://github.com/Nosebone96/QuizApp.git