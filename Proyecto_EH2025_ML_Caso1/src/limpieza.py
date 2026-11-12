import os
import duckdb
import sweetviz as sv
from sweetviz import FeatureConfig

# 1. Rutas del proyecto en Google Drive
BASE_DIR = '/content/drive/MyDrive/Maestria ia/Modulo 3 Visualizacion de datos/Modulo3_Tarea2/Proyecto_EH2025_ML_Caso1'
parquet_path = os.path.join(BASE_DIR, 'EH2025_Persona.parquet')
report_path = os.path.join(BASE_DIR, 'EDA_Desercion_Escolar_Sweetviz.html')

# 2. Consulta en DuckDB: Extraer menores en edad escolar (6 a 19 años) + variables clave y entorno del hogar
query = f"""
WITH JefeHogar AS (
    SELECT
        folio,
        niv_ed AS niv_ed_jefe,
        s01a_02 AS sexo_jefe,
        s01a_03 AS edad_jefe
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
    p.s03a_04 AS matriculado_este_anio,
    p.s03a_05 AS razon_no_matricula,
    p.s03b_10 AS asiste_actualmente,
    p.s03b_11 AS razon_no_asiste,
    p.cmasi AS condicion_matricula_asistencia,
    p.niv_ed AS nivel_educativo,
    p.aestudio AS anios_estudio,
    p.s03c_13 AS tiene_celular,
    p.s03c_16a AS uso_internet,
    p.s04a_01 AS trabajo_semana_pasada,
    p.tipohogar,
    p.yhogpc AS ingreso_per_capita_hogar,
    p.p0 AS pobreza_hogar,
    j.niv_ed_jefe,
    j.edad_jefe,
    c.total_menores_escolares,
    ROUND(CAST(c.total_menores_escolares AS FLOAT) / NULLIF(c.total_pet, 0), 2) AS ratio_dependencia
FROM '{parquet_path}' p
LEFT JOIN JefeHogar j ON p.folio = j.folio
LEFT JOIN CargaHogar c ON p.folio = c.folio
WHERE p.s01a_03 BETWEEN 6 AND 19
"""

print("Extrayendo dataset analítico con DuckDB...")
df_eda = duckdb.sql(query).df()
print(f"Registros extraídos para EDA (6 a 19 años): {len(df_eda):,} filas y {df_eda.shape[1]} columnas.")

# 3. Configurar Sweetviz para aceptar la variable objetivo forzándola como numérica
config_objetivo = FeatureConfig(force_num=["condicion_matricula_asistencia"])

# 4. Generar el reporte interactivo de Sweetviz (usando feat_cfg)
print("Generando reporte Sweetviz...")
reporte = sv.analyze(df_eda, target_feat='condicion_matricula_asistencia', feat_cfg=config_objetivo)

# 5. Guardar el archivo HTML en Google Drive
reporte.show_html(filepath=report_path, open_browser=False)
print(f"¡Reporte EDA guardado exitosamente en:\n{report_path}")