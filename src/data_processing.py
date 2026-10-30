import numpy as np
import pandas as pd


def generate_synthetic_ecoruta_data(n_samples: int = 1000) -> pd.DataFrame:
    """Genera un dataset sintético estructurado para simular la integración

    de fuentes de datos de Ecobici, INEGI (incidentes) y SMN (clima).
    """
    np.random.seed(42)

    estaciones = [
        "Buenavista",
        "Reforma - Insurgentes",
        "Zócalo",
        "Condesa",
        "Polanco",
        "Roma Norte",
        "Tláhuac Centro",
    ]
    coordenadas = {
        "Buenavista": (19.4461, -99.1530),
        "Reforma - Insurgentes": (19.4290, -99.1610),
        "Zócalo": (19.4326, -99.1332),
        "Condesa": (19.4116, -99.1746),
        "Polanco": (19.4338, -99.1913),
        "Roma Norte": (19.4181, -99.1589),
        "Tláhuac Centro": (19.2867, -99.0042),
    }

    estacion_origen = np.random.choice(estaciones, size=n_samples)
    lats = [coordenadas[e][0] for e in estacion_origen]
    lons = [coordenadas[e][1] for e in estacion_origen]

    horas = np.random.randint(0, 24, size=n_samples)
    dias = np.random.choice(
        [
            "Lunes",
            "Martes",
            "Miércoles",
            "Jueves",
            "Viernes",
            "Sábado",
            "Domingo",
        ],
        size=n_samples,
    )
    precipitacion_mm = np.random.exponential(scale=2.0, size=n_samples)
    precipitacion_mm = np.where(precipitacion_mm < 0.5, 0.0, precipitacion_mm)

    duracion_min = np.random.gamma(shape=3, scale=5, size=n_samples) + 5
    historia_incidentes = np.random.poisson(lam=1.2, size=n_samples)

    # Cálculo base de demanda
    base_demanda = (
        (horas >= 7) & (horas <= 9)
    ) * 40 + ((horas >= 18) & (horas <= 20)) * 50

    # Cambio aquí: se usa '=' en lugar de '+=' para permitir cambio de tipo implícito antes del astype(int)
    viajes_estimados = (
        base_demanda
        + np.random.randint(5, 25, size=n_samples)
        - (precipitacion_mm * 3)
    )
    viajes_estimados = np.clip(viajes_estimados, a_min=1, a_max=None).astype(
        int
    )

    df = pd.DataFrame(
        {
            "estacion_origen": estacion_origen,
            "latitud": lats,
            "longitud": lons,
            "hora": horas,
            "dia_semana": dias,
            "duracion_minutos": np.round(duracion_min, 2),
            "precipitacion_mm": np.round(precipitacion_mm, 2),
            "incidentes_previos": historia_incidentes,
            "demanda_viajes": viajes_estimados,
        }
    )

    df["nivel_riesgo"] = pd.cut(
        df["incidentes_previos"] + (df["precipitacion_mm"] > 5).astype(int),
        bins=[-1, 1, 3, 10],
        labels=["Bajo", "Medio", "Alto"],
    )

    return df


def scrub_data(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia y prepara el dataset filtrando valores atípicos y nulos."""
    df_clean = df.copy()
    df_clean = df_clean.dropna()
    df_clean = df_clean[df_clean["duracion_minutos"] <= 120]
    return df_clean