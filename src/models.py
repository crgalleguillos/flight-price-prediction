import argparse
import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

from features import split_features_target, make_pipeline

def evaluate(y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    rmse = mean_squared_error(y_true, y_pred, squared=False)
    r2 = r2_score(y_true, y_pred)
    return mae, rmse, r2

def main(args):
    # Placeholder: Replace with your data loading
    # df = pd.read_csv("data/your_file.csv")
    raise SystemExit("Coloca tu carga de datos en src/models.py (línea ~23) y vuelve a ejecutar.")

    # Example:
    # if args.segment == "economy":
    #     df = df[df['Segment'] == 'Economy'].copy()
    # elif args.segment == "business":
    #     df = df[df['Segment'] == 'Business'].copy()

    # X, y = split_features_target(df, target="Price")
    # pipe_ridge = make_pipeline(Ridge(), X)
    # pipe_rf = make_pipeline(RandomForestRegressor(random_state=123), X)
    # pipe_gb = make_pipeline(GradientBoostingRegressor(random_state=123), X)

    # param_grid = {
    #     "model": [Ridge(), RandomForestRegressor(random_state=123), GradientBoostingRegressor(random_state=123)],
    # }
    # cv = KFold(n_splits=5, shuffle=True, random_state=123)
    # grid = GridSearchCV(make_pipeline(Ridge(), X), param_grid={"model": [Ridge()]}, cv=cv)  # Simplify or expand
    # # Fit, predict, evaluate...

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--segment", type=str, default="economy", choices=["economy", "business"])
    args = parser.parse_args()
    main(args)