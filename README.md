# 🚲 EcoRuta: Optimización Geoespacial y Predicción de Demanda para la Movilidad Ciclista Sustentable en Smart Cities

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B.svg)](https://streamlit.io/)
[![Metodología](https://img.shields.io/badge/Metodolog%C3%ADa-OSEMN-green.svg)](#metodología-osemn)
[![Institución](https://img.shields.io/badge/TecNM-Tl%C3%A1huac%20III-red.svg)](https://www.tlahuac3.tecnm.mx/)

## 📌 Descripción del Proyecto
**EcoRuta** es una solución analítica integral desarrollada en la carrera de **Ingeniería en Ciencia de los Datos** del **Instituto Tecnológico de Tláhuac III**. El sistema integra datos históricos abiertos del programa **Ecobici**, registros de incidentes viales del **INEGI (ATUS)** y datos meteorológicos del **Servicio Meteorológico Nacional (SMN)** para analizar patrones de movilidad, prevenir siniestros viales y predecir la demanda de viajes en la Zona Metropolitana del Valle de México.

---

## 👥 Equipo de Trabajo (Equipo 01)
* **Zhabiani Somersille Aguilar** (`L261120449@Tlahuac3.tecnm.mx`) – *Líder de Proyecto / Product Owner*
* **Valeria Hernández González** (`L261120304@Tlahuac3.tecnm.mx`) – *Compliance & Data Engineer*
* **Nathaly Lilian Avendaño Sanchez** (`L261120414@Tlahuac3.tecnm.mx`) – *Auditora Ética & Data Scientist*

---

## ⚙️ Metodología OSEMN
El proyecto implementa la metodología ágil **OSEMN**:

1. **Obtain (Obtener):** Ingesta de datos abiertos desde los portales oficiales de Ecobici, INEGI y SMN.
2. **Scrub (Limpiar):** Tratamiento de nulos, eliminación de duplicados, estandarización de coordenadas y filtrado de sesgos geográficos.
3. **Explore (Explorar):** Análisis Exploratorio de Datos (EDA) geoespacial y temporal mediante mapas interactivos y diagramas de correlación.
4. **Model (Modelar):** Entrenamiento de algoritmos supervisados (`RandomForestRegressor` y `RandomForestClassifier`) con `scikit-learn` para estimar volumen de viajes y nivel de riesgo por intersección.
5. **iNterpret (Interpretar):** Despliegue de un tablero interactivo en **Streamlit** enfocado en la toma de decisiones ciudadanas y la movilidad segura.

---

## 🚀 Instalación y Ejecución Local

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/Equipo01-TecNM/EcoRuta-CDMX.git
   cd EcoRuta-CDMX
   ```

2. **Crear y activar un entorno virtual:**
   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En Linux/macOS:
   source venv/bin/activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación interactiva de Streamlit:**
   ```bash
   streamlit run app.py
   ```

---

## ⚖️ Marco Legal y Privacidad
El proyecto opera bajo el principio de **minimización de datos** e **imposibilidad de reidentificación**, en cumplimiento con el **Art. 6º y 16º de la CPEUM**, la **LFPDPPP**, las recomendaciones del **INAI** y los criterios de **Riesgo Mínimo** del **AI Act de la Unión Europea**.
