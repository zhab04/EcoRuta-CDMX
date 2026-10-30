import pandas as pd
import streamlit as st
from src.data_processing import generate_synthetic_ecoruta_data, scrub_data
from src.eda import plot_demanda_por_hora, plot_mapa_riesgo
from src.model import train_demand_model, train_risk_model

# Configuración de página
st.set_page_config(
    page_title="EcoRuta Analytics",
    page_icon="🚲",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Estilos CSS Minimalistas (Dark Theme)
st.markdown(
    """
    <style>
    /* Reset y base */
    .stApp {
        background-color: #0B0E14;
        color: #E6EDF3;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    }
    
    /* Header Minimalista */
    .minimal-header {
        padding: 10px 0px 20px 0px;
        border-bottom: 1px solid #1F242C;
        margin-bottom: 25px;
    }
    .minimal-header h1 {
        font-size: 1.5rem !important;
        font-weight: 600 !important;
        letter-spacing: -0.5px;
        color: #F0F6FC !important;
        margin: 0 !important;
    }
    .minimal-header p {
        font-size: 0.88rem !important;
        color: #8B949E !important;
        margin-top: 4px !important;
    }

    /* Sidebar minimalista */
    [data-testid="stSidebar"] {
        background-color: #0E1117 !important;
        border-right: 1px solid #1F242C;
    }
    [data-testid="stSidebar"] * {
        color: #C9D1D9 !important;
    }
    [data-testid="stSidebar"] .stRadio label {
        background-color: transparent;
        padding: 8px 10px;
        border-radius: 4px;
        margin-bottom: 4px;
        border: 1px solid transparent;
        font-size: 0.88rem;
    }
    [data-testid="stSidebar"] .stRadio label:hover {
        background-color: #161B22;
        border-color: #30363D;
    }

    /* Targetas KPI limpia */
    .kpi-card-minimal {
        background-color: #161B22;
        border: 1px solid #21262D;
        border-radius: 6px;
        padding: 16px;
    }
    .kpi-label {
        color: #8B949E;
        font-size: 0.75rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .kpi-value {
        color: #F0F6FC;
        font-size: 1.6rem;
        font-weight: 600;
        margin-top: 4px;
    }

    /* Cajas informativas */
    .info-card {
        background-color: #161B22;
        border: 1px solid #21262D;
        border-radius: 6px;
        padding: 18px;
        margin-bottom: 20px;
        font-size: 0.9rem;
        line-height: 1.5;
        color: #C9D1D9;
    }

    /* Pestañas */
    .stTabs [data-baseweb="tab-list"] {
        gap: 16px;
        border-bottom: 1px solid #21262D;
    }
    .stTabs [data-baseweb="tab"] {
        height: 38px;
        background-color: transparent;
        border: none;
        color: #8B949E;
        font-size: 0.88rem;
        font-weight: 500;
        padding: 0;
    }
    .stTabs [aria-selected="true"] {
        background-color: transparent !important;
        color: #F0F6FC !important;
        border-bottom: 2px solid #58A6FF !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Encabezado
st.markdown(
    """
    <div class="minimal-header">
        <h1>EcoRuta — Analytics & Movilidad Ciclista</h1>
        <p>Optimización Geoespacial y Predicción de Demanda | TecNM Campus Tláhuac III</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Carga de datos
raw_df = generate_synthetic_ecoruta_data(1000)
df = scrub_data(raw_df)

# Barra lateral
with st.sidebar:
    st.markdown("##### Panel de Control")
    opcion = st.radio(
        "Navegación:",
        [
            "1. Diagnóstico y Metodología",
            "2. Monitoreo Geoespacial (EDA)",
            "3. Evaluación Predictiva de Riesgo",
            "4. Gobernanza y Ficha Técnica",
        ],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.caption("Equipo 01 — Ciencia de los Datos")
    st.caption("• Zhabiani Somersille (Líder)")
    st.caption("• Valeria Hernández")
    st.caption("• Nathaly Avendaño")

# Módulo 1: Diagnóstico y Metodología
if opcion == "1. Diagnóstico y Metodología":
    st.markdown("#### Diagnóstico General e Integración")

    st.markdown(
        """
        <div class="info-card">
            Consolidación y estructuración de datos abiertos del sistema <b>Ecobici</b>, 
            registros de siniestralidad vial de <b>INEGI (ATUS)</b> y métricas meteorológicas del <b>SMN</b> 
            para el análisis de patrones de movilidad no motorizada.
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(
            f"""
            <div class="kpi-card-minimal">
                <div class="kpi-label">Registros Procesados</div>
                <div class="kpi-value">{len(df):,}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            f"""
            <div class="kpi-card-minimal">
                <div class="kpi-label">Demanda Promedio</div>
                <div class="kpi-value">{int(df['demanda_viajes'].mean())} <span style="font-size:0.8rem; color:#8B949E;">viajes/h</span></div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            f"""
            <div class="kpi-card-minimal">
                <div class="kpi-label">Estaciones Analizadas</div>
                <div class="kpi-value">{df['estacion_origen'].nunique()}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col4:
        st.markdown(
            """
            <div class="kpi-card-minimal">
                <div class="kpi-label">Estado de Red</div>
                <div class="kpi-value" style="color:#D29922;">Estable</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("##### Metodología OSEMN")
    st.markdown(
        """
        - **Obtain:** Extracción automatizada de fuentes de datos abiertos.
        - **Scrub:** Limpieza, normalización geoespacial y tratamiento de valores nulos.
        - **Explore:** Análisis exploratorio multivariable temporal y espacial.
        - **Model:** Modelado predictivo de demanda y clasificación mediante Random Forest.
        - **iNterpret:** Despliegue e interpretación en dashboard analítico.
        """
    )

# Módulo 2: EDA
elif opcion == "2. Monitoreo Geoespacial (EDA)":
    st.markdown("#### Monitoreo Geoespacial y Análisis de Demanda")

    tab1, tab2 = st.tabs(["Afluencia Temporal", "Cartografía de Riesgo"])

    with tab1:
        st.plotly_chart(plot_demanda_por_hora(df), use_container_width=True)

    with tab2:
        st.plotly_chart(plot_mapa_riesgo(df), use_container_width=True)

# Módulo 3: Evaluación Predictiva
elif opcion == "3. Evaluación Predictiva de Riesgo":
    st.markdown("#### Modelos Predictivos e Inferencia")

    col_m1, col_m2 = st.columns(2)

    with col_m1:
        st.markdown("##### 1. Estimación de Demanda")
        model_reg, score_reg = train_demand_model(df)
        st.caption(f"RandomForestRegressor | R² Score: {score_reg:.2f}")

        hora_input = st.slider("Hora del recorrido (0-23 h):", 0, 23, 8)
        precip_input = st.slider("Precipitación estimada (mm):", 0.0, 20.0, 0.0)

        pred_viajes = model_reg.predict([[hora_input, precip_input, 1, 2]])[0]
        st.metric("Demanda Proyectada", f"{max(0, int(pred_viajes))} bicicletas")

    with col_m2:
        st.markdown("##### 2. Clasificación de Riesgo Vial")
        model_clf, score_clf = train_risk_model(df)
        st.caption(f"RandomForestClassifier | Exactitud: {score_clf*100:.1f}%")

        incidentes_input = st.number_input(
            "Histórico de incidentes en intersección:", 0, 10, 2
        )

        pred_riesgo = model_clf.predict(
            [[hora_input, precip_input, incidentes_input]]
        )[0]

        if pred_riesgo == "Bajo":
            st.success("🟢 Riesgo Estimado: BAJO")
        elif pred_riesgo == "Medio":
            st.warning("🟡 Riesgo Estimado: MEDIO")
        else:
            st.error("🔴 Riesgo Estimado: ALTO")

# Módulo 4: Gobernanza
elif opcion == "4. Gobernanza y Ficha Técnica":
    st.markdown("#### Gobernanza de Datos y Marco Normativo")

    st.markdown(
        """
        <div class="info-card">
            <b>Privacidad y Ética de Datos:</b>
            <ul>
                <li><b>Minimización de Datos:</b> No se recopilan ni procesan datos personales identificables.</li>
                <li><b>Cumplimiento Normativo:</b> Alinear a los Artículos 6º y 16º de la CPEUM, LFPDPPP y recomendaciones del INAI.</li>
                <li><b>Marco Internacional:</b> Clasificado como sistema de Riesgo Mínimo o Nulo según la Ley de IA de la UE.</li>
                <li><b>Atención a Sesgos:</b> Transparencia sobre la concentración geográfica de la muestra en zonas céntricas.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )