import pandas as pd
import numpy as np

np.random.seed(42)

N = 6000000

velocidade = np.random.uniform(180, 320, N)
altitude = np.random.uniform(0, 1000, N)
taxa_descida = np.random.uniform(1, 10, N)
vento_lateral = np.random.uniform(0, 50, N)
peso = np.random.uniform(30000, 120000, N)

distancia_pouso = (
    velocidade * 4
    + peso * 0.02
    + vento_lateral * 10
    - taxa_descida * 30
)

df = pd.DataFrame({
    "velocidade": velocidade,
    "altitude": altitude,
    "taxa_descida": taxa_descida,
    "vento_lateral": vento_lateral,
    "peso": peso,
    "distancia_pouso": distancia_pouso
})

df.to_csv("pouso_aeronave.csv", index=False)

print(df.head())
print("Dataset criado com sucesso!")