import os
import duckdb
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import roc_auc_score, classification_report

# 1. Rutas del proyecto en Google Drive
BASE_DIR = '/content/drive/MyDrive/Maestria ia/Modulo 3 Visualizacion de datos/Modulo3_Tarea2/Proyecto_EH2025_ML_Caso1'
parquet_path = os.path.join(BASE_DIR, 'EH2025_Persona.parquet')

# 2. Consulta en DuckDB corregida (usando p.aestudio)
query = f"""
WITH JefeHogar AS (
    SELECT folio, niv_ed AS niv_ed_jefe, s01a_03 AS edad_jefe
    FROM '{parquet_path}'
    WHERE s01a_05 = 1
),
CargaHogar AS (
    SELECT
        folio,
        COUNT(CASE WHEN s01a_03 BETWEEN 6 AND 19 THEN 1 END) AS total_menores_escolares,
        COUNT(CASE WHEN pet = 1 THEN 1 END) AS total_pet
    FROM '{parquet_path}'
    GROUP BY folio
)
SELECT
    p.area,
    p.depto,
    p.s01a_02 AS sexo,
    p.s01a_03 AS edad,
    p.s01a_07_1 AS idioma_principal,
    p.s01a_09 AS autoidentificacion_indigena,
    p.s03a_01 AS sabe_leer_escribir,
    p.aestudio, -- <-- Corregido aquí
    p.s03c_13 AS tiene_celular,
    p.s03c_16a AS uso_internet,
    p.s04a_01 AS trabajo_semana_pasada,
    p.tipohogar,
    p.yhogpc AS ingreso_per_capita,
    p.p0 AS pobreza_hogar,
    COALESCE(j.niv_ed_jefe, 0) AS niv_ed_jefe,
    COALESCE(j.edad_jefe, 40) AS edad_jefe,
    COALESCE(c.total_menores_escolares, 1) AS total_menores_escolares,
    COALESCE(ROUND(CAST(c.total_menores_escolares AS FLOAT) / NULLIF(c.total_pet, 0), 2), 0) AS ratio_dependencia,
    CASE WHEN p.cmasi != 1 THEN 1 ELSE 0 END AS target_desercion
FROM '{parquet_path}' p
LEFT JOIN JefeHogar j ON p.folio = j.folio
LEFT JOIN CargaHogar c ON p.folio = c.folio
WHERE p.s01a_03 BETWEEN 6 AND 19
  AND p.cmasi IS NOT NULL
  AND p.p0 IS NOT NULL
"""

print("Extrayendo dataset para modelado predictivo...")
df_model = duckdb.sql(query).df()

# 3. Preparación de features (X) y target (y)
feature_cols = [
    'area', 'depto', 'sexo', 'edad', 'idioma_principal',
    'autoidentificacion_indigena', 'sabe_leer_escribir', 'aestudio',  # <-- Corregido aquí también
    'tiene_celular', 'uso_internet', 'trabajo_semana_pasada', 'tipohogar',
    'ingreso_per_capita', 'pobreza_hogar', 'niv_ed_jefe', 'edad_jefe',
    'total_menores_escolares', 'ratio_dependencia'
]

X = df_model[feature_cols].fillna(0)
y = df_model['target_desercion']

print(f"Dimensiones del dataset de entrenamiento: {X.shape}")
print(f"Distribución del Target (Deserción / Inasistencia):\n{y.value_counts(normalize=True)}")

# 4. Configuración de Validación Cruzada Estratificada (5 Folds)
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

rf_model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42, n_jobs=-1)
xgb_model = XGBClassifier(n_estimators=100, max_depth=6, learning_rate=0.1, random_state=42, eval_metric='logloss')

models = {
    'Random Forest': rf_model,
    'XGBoost': xgb_model
}

# 5. Bucle de Evaluación con Validación Cruzada
for name, model in models.items():
    print(f"\n--- Evaluando modelo: {name} ---")
    roc_auc_scores = []

    for fold, (train_idx, val_idx) in enumerate(skf.split(X, y)):
        X_train, X_val = X.iloc[train_idx], X.iloc[val_idx]
        y_train, y_val = y.iloc[train_idx], y.iloc[val_idx]

        model.fit(X_train, y_train)
        y_pred_proba = model.predict_proba(X_val)[:, 1]
        score = roc_auc_score(y_val, y_pred_proba)
        roc_auc_scores.append(score)

    print(f"ROC-AUC Promedio (5 Folds) [{name}]: {np.mean(roc_auc_scores):.4f} (+/- {np.std(roc_auc_scores):.4f})")

xgb_model.fit(X, y)
print("\n¡Modelado supervisado completado exitosamente!")