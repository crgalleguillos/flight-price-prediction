# Flight Price Prediction with Machine Learning

## Overview
This project develops a **flight price prediction model** for the **Economy** and **Business** segments, applying a complete **supervised Machine Learning workflow**, from data exploration to model evaluation.

The analysis aims to **identify the factors that most strongly influence flight prices** and to build models capable of anticipating fares based on variables such as airline, origin, destination, flight duration, and number of stops.

The project integrates an **analytical, technical, and business-oriented perspective**, focused on improving the understanding of the airline market and supporting **dynamic pricing strategies and commercial optimization**.

---

## Methodological Workflow

### 1. Exploratory Data Analysis (EDA)
- Data cleaning and outlier detection.
- Univariate and bivariate analysis of key variables.
- Study of correlations and price distributions.

### 2. Feature Engineering
- Generation of time-based variables (`month`, `day`, `weekday`).
- Categorical encoding using **One-Hot Encoding**.
- Selective scaling of numerical variables with **MinMaxScaler**.

### 3. Predictive Modeling
Comparison of three representative regression approaches:
- **Ridge Regression**: linear baseline model with L2 regularization.
- **Random Forest Regressor**: tree-based ensemble capturing non-linear relationships.
- **Gradient Boosting Regressor**: sequential model optimized on residual errors.

The evaluation metrics used were **MAE**, **RMSE**, and **R²**.

---

## Main Results

| Segment  | Model         | R²   | MAE (mean error) |
|----------|---------------|------|------------------|
| Economy  | Random Forest | **0.87** | 586 |
| Business | Random Forest | **0.85** | 2550 |

- **Random Forest** achieved the best balance between accuracy and generalization.
- **Flight duration**, **airline**, and **origin–destination routes** showed the strongest influence on final ticket prices.

---

## Technologies Used

| Tool | Main Use |
|------|----------|
| **Python 3.11+** | Development language |
| **Pandas / NumPy** | Data cleaning and transformation |
| **Matplotlib / Seaborn** | Exploratory visualization |
| **Scikit-learn** | Predictive modeling and evaluation |
| **Jupyter Notebook** | Documentation and analytical workflow |

---

## Author

**Cristián Andrés Galleguillos Vega**  
Biologist · MSc in Natural Resources Engineering · MSc in Data Science & Big Data  
**Location:** Chile  
**LinkedIn:** [Cristián Galleguillos Vega](https://www.linkedin.com/in/cristi%C3%A1n-galleguillos-vega-267343198/)

---

## Conclusion
This project demonstrates the practical application of **Machine Learning for price prediction** in a real-world business context.  
The proposed analytical workflow is **reproducible, interpretable, and scalable**, making it a solid foundation for future projects in **price optimization, demand forecasting**, or **consumer behavior analysis**.
