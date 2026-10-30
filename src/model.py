import pandas as pd
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.model_selection import train_test_split

def train_demand_model(df: pd.DataFrame):
    """Entrena un modelo Random Forest para predecir la demanda de viajes (Target Continuo)."""
    X = df[["hora", "precipitacion_mm", "incidentes_previos"]].copy()
    dias_map = {"Lunes": 1, "Martes": 2, "Miércoles": 3, "Jueves": 4, "Viernes": 5, "Sábado": 6, "Domingo": 7}
    X["dia_num"] = df["dia_semana"].map(dias_map)
    y = df["demanda_viajes"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    score = model.score(X_test, y_test)
    return model, score

def train_risk_model(df: pd.DataFrame):
    """Entrena un modelo de clasificación para el Nivel de Riesgo Vial."""
    X = df[["hora", "precipitacion_mm", "incidentes_previos"]].copy()
    y = df["nivel_riesgo"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    
    acc = clf.score(X_test, y_test)
    return clf, acc
