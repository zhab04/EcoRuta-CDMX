import pandas as pd
import plotly.express as px


def plot_demanda_por_hora(df: pd.DataFrame):
  """Genera gráfica de barras con la demanda promedio por hora del día."""
  df_hourly = df.groupby("hora")["demanda_viajes"].mean().reset_index()
  fig = px.bar(
      df_hourly,
      x="hora",
      y="demanda_viajes",
      title="<b>Demanda Promedio de Viajes por Hora del Día</b>",
      labels={
          "hora": "Hora del Día (0-23)",
          "demanda_viajes": "Promedio de Viajes",
      },
      color="demanda_viajes",
      color_continuous_scale="Viridis",
  )
  fig.update_layout(
      template="plotly_dark",
      paper_bgcolor="rgba(0,0,0,0)",
      plot_bgcolor="rgba(0,0,0,0)",
      font=dict(family="sans-serif", color="#E6EDF3"),
  )
  return fig


def plot_mapa_riesgo(df: pd.DataFrame):
  """Genera un Mapa de Calor (Density Heatmap) de siniestralidad e intensidad vial en CDMX."""
  density_map_fn = getattr(px, "density_map", None)
  density_mapbox_fn = getattr(px, "density_mapbox", None)

  # Opción 1: Plotly v6+ (density_map)
  if density_map_fn is not None:
    try:
      fig = density_map_fn(
          df,
          lat="latitud",
          lon="longitud",
          z="incidentes_previos",
          radius=32,  # Radio de dispersión del calor
          center={"lat": 19.38, "lon": -99.13},
          zoom=10,
          color_continuous_scale="Inferno",  # Escala de calor (Negro -> Morado -> Naranja -> Amarillo)
          hover_name="estacion_origen",
          hover_data=["demanda_viajes", "incidentes_previos"],
          title=(
              "<b>Mapa de Calor: Concentración de Riesgo e Incidentes Viales"
              " (CDMX)</b>"
          ),
          height=480,
      )
      fig.update_layout(
          map_style="carto-darkmatter",
          paper_bgcolor="rgba(0,0,0,0)",
          plot_bgcolor="rgba(0,0,0,0)",
          font=dict(family="sans-serif", color="#E6EDF3"),
      )
      return fig
    except Exception:
      pass

  # Opción 2: Plotly v5.x (density_mapbox)
  if density_mapbox_fn is not None:
    try:
      fig = density_mapbox_fn(
          df,
          lat="latitud",
          lon="longitud",
          z="incidentes_previos",
          radius=32,  # Radio de dispersión del calor
          center={"lat": 19.38, "lon": -99.13},
          zoom=10,
          color_continuous_scale="Inferno",
          hover_name="estacion_origen",
          hover_data=["demanda_viajes", "incidentes_previos"],
          title=(
              "<b>Mapa de Calor: Concentración de Riesgo e Incidentes Viales"
              " (CDMX)</b>"
          ),
          height=480,
      )
      fig.update_layout(
          mapbox_style="carto-darkmatter",
          paper_bgcolor="rgba(0,0,0,0)",
          plot_bgcolor="rgba(0,0,0,0)",
          font=dict(family="sans-serif", color="#E6EDF3"),
      )
      return fig
    except Exception:
      pass

  # Opción 3: Fallback a Mapa de Calor 2D (Density Heatmap) si falla el motor de mapas
  fig = px.density_heatmap(
      df,
      x="longitud",
      y="latitud",
      z="incidentes_previos",
      color_continuous_scale="Inferno",
      title="<b>Mapa de Calor: Densidad de Incidentes en Intersecciones</b>",
      labels={"longitud": "Longitud (º)", "latitud": "Latitud (º)"},
      height=480,
  )
  fig.update_layout(
      template="plotly_dark",
      paper_bgcolor="rgba(0,0,0,0)",
      plot_bgcolor="rgba(0,0,0,0)",
      font=dict(family="sans-serif", color="#E6EDF3"),
  )
  return fig