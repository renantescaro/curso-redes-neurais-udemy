
import numpy as np

# OPERADOR AND
# saidas = np.array([0,0,0,1])

# OOPERADOR OR
saidas = np.array([0,1,1,1])

# OOPERADOR XOR - não linearmente separavel
# saidas = np.array([0,1,1,0])

entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
pesos = np.array([0.0,0.0])
taxaAprendizagem = 0.1

def stepFunction(soma):
    if(soma >= 1):
        return 1
    return 0

def calcularSaida(registro):
    saida = registro.dot(pesos)
    return stepFunction(saida)

def treinar():
    erroTotal = 1
    while (erroTotal != 0):
        erroTotal = 0
        for i in range(len(saidas)):
            saidaCalculada = calcularSaida(np.asarray(entradas[i]))
            erro = abs(saidas[i] - saidaCalculada)
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j] * erro)
                print('Peso atualizado: '+str(pesos[j]))
        print('Total de erros: '+str(erroTotal))

treinar()
