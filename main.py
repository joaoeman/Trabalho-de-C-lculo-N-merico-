
import sympy as sp
# Importar funções da pasta metodos
import metodos.bisseccao 
import metodos.secante

# Define a variável simbólica
x = sp.Symbol('x')

# Recebe a função como string
func_str = input("Digite a função em x: ")

a = input("Digite o inicio do intervalo fechado(Método Bissecção e Falsa posição): ")
b = input("Digite o fim do intervalo fechado(Método Bissecção e Falsa posição): ")

x0 = input("Digite uma estimativa inicial(Método da Secante): ")
x1 = input("Digite a segunda estimativa inicial(Método da Secante): ")

precisao = input("Digite a precisão desejada: ")

iteracoes = input("Digite o máximo de iterações")

# Converte a string em expressão simbólica
func = sp.sympify(func_str)

# Converte os inputs para números
a_num = float(a)
b_num = float(b)

x1_num = float(x1)
x0_num = float(x0)

iteracoes1 = int(iteracoes)
precisao_num = float(precisao)

# Usa a função bissecção da pasta metodos
resultado = metodos.bisseccao.bisseccao(a_num, b_num, iteracoes1, func, precisao_num)
resultado2 = metodos.secante.secante(x0_num, x1_num, func, precisao_num,iteracoes1 )

print()
print(f"Função: {func}")

# Calcula a derivada
derivada = sp.diff(func, x)
print(f"Derivada: {derivada}")

#metodo da bisseccao
print(f"Resultado da bissecção: {resultado}")
if resultado[0] != -1:
    print(f"Raiz encontrada: {resultado[1]} em {resultado[0]+1} iterações")
else:
    print("Raiz não encontrada no número máximo de iterações")

#metodo da secante
print(f"Resultado da secante: {resultado2}")
if resultado[0] != -1:
    print(f"Raiz encontrada: {resultado2[1]} em {resultado2[0]+1} iterações")
else:
    print("Raiz não encontrada no número máximo de iterações")