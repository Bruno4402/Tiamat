import time
import pandas as pd
import optuna
from sklearn.model_selection import (
    train_test_split,
    cross_val_score
)
from sklearn.ensemble import (
    GradientBoostingRegressor
)
inicio = time.time()
df = pd.read_csv(
    "escolas_processado.csv"
)
TARGET = "Média nacional (com redação)"
X = df.drop(columns=[TARGET])
y = df[TARGET]
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X,
    y,
    test_size=0.1,
    random_state=42
)
def cria_instancia_modelo_gb(trial):
    parametros = {
        "n_estimators": trial.suggest_int(
            "n_estimators",
            250,
            600
        ),
        "learning_rate": trial.suggest_float(
            "learning_rate",
            0.02,
            0.15,
            log=True
        ),
        "max_depth": trial.suggest_int(
            "max_depth",
            2,
            8
        ),
        "min_samples_split": trial.suggest_int(
            "min_samples_split",
            2,
            25
        ),
        "min_samples_leaf": trial.suggest_int(
            "min_samples_leaf",
            1,
            10
        ),
        "subsample": trial.suggest_float(
            "subsample",
            0.4,
            1.0
        ),
        "random_state": 42
    }
    return GradientBoostingRegressor(
        **parametros
    )
def funcao_objetivo_gb(trial):
    modelo = cria_instancia_modelo_gb(
        trial
    )
    scores = cross_val_score(
        modelo,
        X_treino,
        y_treino.values.ravel(),
        cv=5,
        scoring="neg_root_mean_squared_error",
        n_jobs=1
    )
    return -scores.mean()
optuna.logging.set_verbosity(
    optuna.logging.WARNING
)
estudo_gb = optuna.create_study(
    direction="minimize"
)
estudo_gb.optimize(
    funcao_objetivo_gb,
    n_trials=150
)
fim = time.time()
tempo_total = fim - inicio
print("\n===== RESULTADOS =====\n")
print("Melhores hiperparâmetros:")
print(estudo_gb.best_params)
print(
    f"\nMelhor RMSE médio: "
    f"{estudo_gb.best_value:.2f}"
)
print(
    f"\nTempo de execução: "
    f"{tempo_total:.2f} segundos"
)
with open(
    "resultado_gb.txt",
    "w"
) as f:
    f.write(
        "Melhores hiperparâmetros:\n"
    )
    f.write(
        str(estudo_gb.best_params)
    )
    f.write("\n\n")
    f.write(
        f"Melhor RMSE médio: "
        f"{estudo_gb.best_value:.4f}\n"
    )
    f.write(
        f"Tempo de execução: "
        f"{tempo_total:.2f} segundos\n"
    )
estudo_gb.trials_dataframe().to_csv(
    "trials_gradient_boosting.csv",
    index=False
)

