
import sympy as sp
# Importar funções da pasta metodos
import metodos.bisseccao 

# Define a variável simbólica
x = sp.Symbol('x')

# Recebe a função como string
func_str = input("Digite a função em x: ")

a = input("Digite o inicio do intervalo fechado(Método Bissecção e Falsa posição): ")
b = input("Digite o fim do intervalo fechado(Método Bissecção e Falsa posição): ")



precisao = input("Digite a precisão desejada: ")

iteracoes = input("Digite o máximo de iterações")

# Converte a string em expressão simbólica
func = sp.sympify(func_str)

# Converte os inputs para números
a_num = float(a)
b_num = float(b)
iteracoes1 = int(iteracoes)
precisao_num = float(precisao)

# Usa a função bissecção da pasta metodos
resultado = metodos.bisseccao.bisseccao(a_num, b_num, iteracoes1, func, precisao_num)

print()
print(f"Função: {func}")

# Calcula a derivada
derivada = sp.diff(func, x)
print(f"Derivada: {derivada}")

print(f"Resultado da bissecção: {resultado}")
if resultado[0] != -1:
    print(f"Raiz encontrada: {resultado[1]} em {resultado[0]+1} iterações")
else:
    print("Raiz não encontrada no número máximo de iterações")
