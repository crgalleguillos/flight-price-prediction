# Predicción de Precios de Vuelos con Machine Learning

## Descripción general
Este proyecto desarrolla un modelo de predicción de precios de vuelos en los segmentos **Economy** y **Business**, aplicando un flujo completo de **Machine Learning supervisado**, desde la exploración de datos hasta la evaluación de modelos.

El análisis busca **identificar los factores que más influyen en el costo de los vuelos** y construir modelos capaces de anticipar precios a partir de variables como la aerolínea, el origen, el destino, la duración del vuelo y las escalas.

El trabajo integra una perspectiva **analítica, técnica y de negocio**, orientada a mejorar la comprensión del mercado aéreo y apoyar estrategias de **pricing dinámico y optimización comercial**.

---

## Flujo metodológico

### 1. Exploratory Data Analysis (EDA)
- Limpieza y detección de valores atípicos.
- Análisis univariado y bivariado de variables clave.
- Estudio de correlaciones y distribución de precios.

### 2. Ingeniería de características
- Generación de variables temporales (`month`, `day`, `weekday`).
- Codificación categórica mediante **One-Hot Encoding**.
- Escalado selectivo de variables numéricas con **MinMaxScaler**.

### 3. Modelado predictivo
Comparación de tres enfoques de regresión representativos:
- **Ridge Regression**: modelo base lineal con regularización L2.
- **Random Forest Regressor**: ensamble de árboles que captura relaciones no lineales.
- **Gradient Boosting Regressor**: modelo secuencial optimizado sobre errores residuales.

Las métricas de evaluación utilizadas fueron: **MAE**, **RMSE** y **R²**.

---

## Resultados principales

| Segmento | Modelo | R² | MAE (error medio) |
|-----------|---------|----|------------------|
| Economy   | Random Forest | **0.87** | 586 |
| Business  | Random Forest | **0.85** | 2550 |

- **Random Forest** fue el modelo con mejor equilibrio entre precisión y generalización.
- Las variables de **duración del vuelo**, **aerolínea** y **rutas origen–destino** mostraron la mayor influencia en el precio final.

---

## Tecnologías utilizadas

| Herramienta | Uso principal |
|--------------|---------------|
| **Python 3.11+** | Lenguaje de desarrollo |
| **Pandas / NumPy** | Limpieza y transformación de datos |
| **Matplotlib / Seaborn** | Visualización exploratoria |
| **Scikit-learn** | Modelado predictivo y evaluación |
| **Jupyter Notebook** | Documentación y flujo analítico |

---

## Autor

**Cristián Andrés Galleguillos Vega**  
Biólogo · Máster en Ingeniería en Recursos Naturales · Máster en Data Science & Big Data  
**Ubicación:** Chile  
**LinkedIn:** [Cristián Galleguillos Vega](https://www.linkedin.com/in/cristi%C3%A1n-galleguillos-vega-267343198/)

---

## Conclusión
Este proyecto demuestra la aplicación práctica de **Machine Learning para la predicción de precios** en un contexto real de negocio.  
El flujo analítico propuesto es **reproducible, interpretable y escalable**, lo que lo convierte en una base sólida para futuros proyectos de **optimización de precios, predicción de demanda** o análisis de comportamiento del consumidor.
