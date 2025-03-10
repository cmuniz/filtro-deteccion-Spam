# Proyecto de Detección de Spam con Machine Learning

Este proyecto tiene como objetivo la **detección de correos electrónicos spam** utilizando técnicas de **Machine Learning**. El modelo fue entrenado y evaluado utilizando diferentes métricas de rendimiento para asegurar una alta precisión y capacidad de detección de spam sin generar demasiados falsos positivos o negativos.

## Tecnologías utilizadas

En este proyecto, se emplearon las siguientes tecnologías y bibliotecas:

- **Python**: Lenguaje de programación utilizado para desarrollar el modelo de Machine Learning.

- **Scikit-learn**: Biblioteca de Python utilizada para implementar el modelo de **regresión logística** y evaluar las métricas de rendimiento.

- **NLTK (Natural Language Toolkit)**: Utilizado para el procesamiento del lenguaje natural, que incluye tareas como la tokenización, lematización y eliminación de stopwords.

- **Pandas**: Biblioteca de Python utilizada para la manipulación y análisis de datos, especialmente útil para cargar y procesar los datos del conjunto de correos electrónicos.

## Descripción del Proyecto

La **detección de spam** es un problema clásico de clasificación en Machine Learning, que tiene un gran impacto en la gestión del correo electrónico. El objetivo principal de este proyecto es entrenar un modelo de Machine Learning para identificar correctamente los correos **spam** y **ham** (no spam) y minimizar los errores.

### **Pasos seguidos en el proyecto:**

1. **Recolección de datos**:
   - El conjunto de datos utilizado proviene de un archivo CSV que contiene correos electrónicos etiquetados como **spam** o **ham**.
   
2. **Preprocesamiento de datos**:
   - **Tokenización** y **eliminación de stopwords** utilizando la biblioteca **NLTK**.
   - Conversión de las palabras en vectores numéricos utilizando **TF-IDF** (Term Frequency-Inverse Document Frequency).
   
3. **Entrenamiento del modelo**:
   - Se utilizó el algoritmo de **Regresión Logística** implementado en **scikit-learn** para entrenar el modelo.

4. **Evaluación del modelo**:
   - Se evaluó el modelo utilizando diversas métricas: **precisión**, **recall**, **F1-score** y **accuracy**.
   - También se presentó un análisis detallado de la **matriz de confusión**.

5. **Resultados**:
   - El modelo alcanzó un rendimiento superior al 99% en precisión y recall, con un bajo número de falsos positivos y falsos negativos, lo que demuestra su efectividad para la detección de spam.

