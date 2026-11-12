import os
import duckdb
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import plotly.express as px

# 1. Rutas del proyecto
BASE_DIR = '/content/drive/MyDrive/Maestria ia/Modulo 3 Visualizacion de datos/Modulo3_Tarea2/Proyecto_EH2025_ML_Caso1'
parquet_path = os.path.join(BASE_DIR, 'EH2025_Persona.parquet')

# 2. Consulta en DuckDB: Extracción de variables para clustering (6 a 19 años)
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
    p.folio,
    p.s01a_03 AS edad,
    p.aestudio AS anios_estudio,
    p.yhogpc AS ingreso_per_capita,
    COALESCE(j.edad_jefe, 40) AS edad_jefe,
    COALESCE(j.niv_ed_jefe, 0) AS niv_ed_jefe,
    COALESCE(ROUND(CAST(c.total_menores_escolares AS FLOAT) / NULLIF(c.total_pet, 0), 2), 0) AS ratio_dependencia
FROM '{parquet_path}' p
LEFT JOIN JefeHogar j ON p.folio = j.folio
LEFT JOIN CargaHogar c ON p.folio = c.folio
WHERE p.s01a_03 BETWEEN 6 AND 19
  AND p.yhogpc IS NOT NULL
  AND p.aestudio IS NOT NULL
"""

print("Extrayendo dataset para clustering...")
df_cluster = duckdb.sql(query.replace('\n', ' ')).df()

# 3. Preparación y escalado de datos para K-Means
features = ['edad', 'anios_estudio', 'ingreso_per_capita', 'edad_jefe', 'niv_ed_jefe', 'ratio_dependencia']
X = df_cluster[features].fillna(0)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Aplicación de K-Means (agrupando en 3 perfiles principales)
print("Ejecutando algoritmo K-Means (k=3)...")
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df_cluster['cluster'] = kmeans.fit_predict(X_scaled)
df_cluster['cluster_label'] = df_cluster['cluster'].map({
    0: 'Perfil 1: Vulnerabilidad / Ingresos Bajos',
    1: 'Perfil 2: Clase Media Estándar',
    2: 'Perfil 3: Hogares con Mayor Acceso / Estabilidad'
})

# 5. Visualización interactiva con Plotly (Diagrama de dispersión por clústeres)
fig = px.scatter(
    df_cluster.sample(min(3000, len(df_cluster)), random_state=42), # Muestra para fluidez visual en el navegador
    x='anios_estudio',
    y='ingreso_per_capita',
    color='cluster_label',
    size='edad',
    hover_data=['edad', 'edad_jefe', 'ratio_dependencia'],
    title='<b>Segmentación por Clústeres (K-Means) de Población Escolar</b><br><sup>Relación entre Años de Estudio e Ingreso Per Cápita del Hogar</sup>',
    labels={
        'anios_estudio': 'Años de Estudio Aprobados',
        'ingreso_per_capita': 'Ingreso Per Cápita del Hogar (Bs)',
        'cluster_label': 'Perfil de Clúster',
        'edad': 'Edad del Menor'
    },
    template='plotly_white',
    log_y=True # Aplicar escala logarítmica en ingresos para mejor visualización
)

fig.update_layout(
    title_font_size=15,
    legend_title_text='Perfiles Identificados'
)

# Mostrar gráfico interactivo
fig.show()

# Guardar como HTML en Google Drive
html_path = os.path.join(BASE_DIR, 'Visualizacion_3_Clustering_KMeans.html')
fig.write_html(html_path)
print(f"Gráfico de clustering guardado exitosamente en: {html_path}")