import pandas as pd
import numpy as np
import time

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error

df = pd.read_csv("pouso_aeronave.csv")

X = df.drop("distancia_pouso", axis=1)
y = df["distancia_pouso"]

X = X.astype(np.float64)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

scaler_X = StandardScaler()
scaler_y = StandardScaler()

X_train = scaler_X.fit_transform(X_train)
X_test = scaler_X.transform(X_test)

y_train_scaled = scaler_y.fit_transform(
    y_train.values.reshape(-1, 1)
).ravel()

mlp = MLPRegressor(
    hidden_layer_sizes=(20,),
    activation="logistic",
    max_iter=50,
    early_stopping=True,
    random_state=42
)

inicio = time.time()

mlp.fit(X_train, y_train_scaled)

fim = time.time()

pred_scaled = mlp.predict(X_test)

pred = scaler_y.inverse_transform(
    pred_scaled.reshape(-1, 1)
).ravel()

mse = mean_squared_error(y_test, pred)
mae = mean_absolute_error(y_test, pred)

tempo_min = (fim - inicio) / 60

print("\n===== FLOAT64 =====")
print(f"Tempo (min): {tempo_min:.4f}")
print(f"MSE: {mse:.4f}")
print(f"MAE: {mae:.4f}")

np.save("loss_float64.npy", mlp.loss_curve_)