import time
import pandas as pd
import optuna
from sklearn.model_selection import (
    train_test_split,
    cross_val_score
)
from sklearn.ensemble import (
    RandomForestRegressor
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
def cria_instancia_modelo_fa(trial):
    parametros = {
        "n_estimators": trial.suggest_int(
            "n_estimators",
            50,
            500
        ),
        "max_depth": trial.suggest_int(
            "max_depth",
            2,
            30
        ),
        "min_samples_split": trial.suggest_int(
            "min_samples_split",
            2,
            30
        ),
        "min_samples_leaf": trial.suggest_int(
            "min_samples_leaf",
            1,
            20
        ),
        "max_features": trial.suggest_categorical(
            "max_features",
            [None, "sqrt", "log2"]
        ),
        "bootstrap": trial.suggest_categorical(
            "bootstrap",
            [True, False]
        ),
        "random_state": 42,
        "n_jobs": -1
    }
    return RandomForestRegressor(
        **parametros
    )
def funcao_objetivo_fa(trial):
    modelo = cria_instancia_modelo_fa(
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
estudo_fa = optuna.create_study(
    direction="minimize"
)
estudo_fa.optimize(
    funcao_objetivo_fa,
    n_trials=150
)
fim = time.time()
tempo_total = fim - inicio
print("\n===== RESULTADOS =====\n")
print("Melhores hiperparâmetros:")
print(estudo_fa.best_params)
print(
    f"\nMelhor RMSE médio: "
    f"{estudo_fa.best_value:.4f}"
)
print(
    f"\nTempo de execução: "
    f"{tempo_total:.2f} segundos"
)
with open(
    "resultado_fa.txt",
    "w"
) as f:
    f.write(
        "Melhores hiperparâmetros:\n"
    )
    f.write(
        str(estudo_fa.best_params)
    )
    f.write("\n\n")
    f.write(
        f"Melhor RMSE médio: "
        f"{estudo_fa.best_value:.2f}\n"
    )
    f.write(
        f"Tempo de execução: "
        f"{tempo_total:.2f} segundos\n"
    )
estudo_fa.trials_dataframe().to_csv(
    "trials_random_forest.csv",
    index=False
)
