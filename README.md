# Análisis Predictivo y Factores de Deserción Escolar en Bolivia
## Evidencia Empírica basada en la Encuesta de Hogares 2025 (INE) y Machine Learning

Este repositorio contiene el desarrollo completo del caso de estudio enfocado en identificar y analizar los factores sociodemográficos, económicos y geográficos que influyen en la deserción e inasistencia escolar en Bolivia, utilizando microdatos oficiales de la Encuesta de Hogares 2025 del Instituto Nacional de Estadística (INE).

---

## 📌 Pregunta de Investigación
> **¿Cuáles son los factores sociodemográficos, económicos y geográficos que más influyen en la deserción escolar en Bolivia?**

---

## 📂 Estructura del Repositorio

La organización de los archivos responde a la siguiente jerarquía:

```text
Proyecto_EH2025_ML_Caso1/
│
├── data/               # Microdatos crudos (.dta) o scripts de conexión al Parquet
├── notebooks/          # Jupyter Notebooks limpios, comentados y ejecutables (.ipynb)
├── src/                # Scripts de Python modulares (limpieza, features, modelado)
├── outputs/            # Reportes EDA en HTML y datasets procesados (.parquet / .csv)
├── docs/               # Informe final de Storytelling (HTML5 / PDF) y recursos visuales
├── .gitignore          # Exclusión de archivos pesados y entornos virtuales
├── requirements.txt    # Dependencias exactas del proyecto
└── README.md           # Documentación técnica y guía de ejecución

🛠️ Stack Tecnológico y Metodología
Procesamiento de Datos: DuckDB (consultas SQL optimizadas sobre microdatos).

Machine Learning & Clustering: Scikit-Learn (K-Means, Random Forest, Validación Cruzada Estratificada) y XGBoost.

Explicabilidad (XAI): SHAP (SHapley Additive exPlanations) para la interpretación de modelos de ensambles.

Visualización y Reportes: Plotly, Folium y Quarto (HTML5 interactivo / PDF).

🚀 Instrucciones de Ejecución
Clonar o descargar el repositorio:
Descarga o clona la carpeta principal en tu entorno local o en Google Drive.

Instalar dependencias:
Abre una terminal en la carpeta raíz del proyecto y ejecuta:

Bash
pip install -r requirements.txt
Ejecutar el análisis:

Abre el cuaderno principal ubicado en la carpeta notebooks/ en Google Colab o Jupyter.

Ejecuta las celdas secuencialmente para reproducir el flujo desde la ingesta en DuckDB hasta la evaluación de modelos y gráficos SHAP.

O revisa el informe final consolidado en formato web o PDF dentro de la carpeta docs/.

👤 Autor
Tito Junior Quiroga Cuenca
Maestría en Inteligencia Artificial / Ciencia de Datos

"Fuente: Instituto Nacional de Estadística, Encuesta de Hogares 2025 - http://anda.ine.gob.bo/index.php/catalog/256. Fecha de acceso: 10/11/2026."