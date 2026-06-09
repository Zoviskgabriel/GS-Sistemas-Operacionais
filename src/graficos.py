import numpy as np
import matplotlib.pyplot as plt

tempo_float = 1.4237
tempo_int8 = 1.7628

mse_float = 3.1707
mse_int8 = 304327.4105

mae_float = 1.2637
mae_int8 = 457.3551

try:
    loss_float = np.load("loss_float64.npy")
    loss_int8 = np.load("loss_int8.npy")

    plt.figure(figsize=(8, 5))
    plt.plot(loss_float, label="float64")
    plt.plot(loss_int8, label="int8")
    plt.title("Curva de Loss por Época")
    plt.xlabel("Épocas")
    plt.ylabel("Loss")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("loss.png")
    plt.close()

    print("loss.png gerado com sucesso!")

except FileNotFoundError:
    print("Arquivos loss_float64.npy ou loss_int8.npy não encontrados.")

plt.figure(figsize=(8, 5))
plt.bar(
    ["float64", "int8"],
    [tempo_float, tempo_int8]
)
plt.title("Tempo de Processamento")
plt.ylabel("Tempo (min)")
plt.tight_layout()
plt.savefig("tempo_processamento.png")
plt.close()

print("tempo_processamento.png gerado com sucesso!")

plt.figure(figsize=(8, 5))
plt.bar(
    ["float64", "int8"],
    [mse_float, mse_int8]
)
plt.yscale("log")
plt.title("Comparação do MSE")
plt.ylabel("MSE (Escala Logarítmica)")
plt.tight_layout()
plt.savefig("mse.png")
plt.close()

print("mse.png gerado com sucesso!")

plt.figure(figsize=(8, 5))
plt.bar(
    ["float64", "int8"],
    [mae_float, mae_int8]
)
plt.yscale("log")
plt.title("Comparação do MAE")
plt.ylabel("MAE (Escala Logarítmica)")
plt.tight_layout()
plt.savefig("mae.png")
plt.close()

print("mae.png gerado com sucesso!")

print("\nTodos os gráficos foram gerados com sucesso!")