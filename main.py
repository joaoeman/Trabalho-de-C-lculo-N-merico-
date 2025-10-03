import sympy as sp
import metodos.bisseccao
import metodos.falsaPosicao
import metodos.secante
import metodos.newton
import testarMetodos

# Define a variável simbólica
x = sp.Symbol('x')

def main():
    print("=" * 50)
    print("   SIMULADOR DE MÉTODOS NUMÉRICOS")
    print("=" * 50)
    
    # Recebe a função como string
    func_str = input("Digite a função em x: ")
    
    try:
        # Converte a string em expressão simbólica
        func = sp.sympify(func_str)
        print(f"Função: {func}")
        
        # Calcula a derivada
        derivada = sp.diff(func, x)
        print(f"Derivada: {derivada}")
        
    except Exception as e:
        print(f"Erro ao processar a função: {e}")
        return
    
    # Parâmetros para métodos de intervalo
    try:
        a = float(input("Digite o início do intervalo [a,b]: "))
        b = float(input("Digite o fim do intervalo [a,b]: "))
        x0 = float(input("Digite uma estimativa inicial: "))
        x1 = float(input("Digite uma segunda estimativa inicial: "))
        precisao = float(input("Digite a precisão desejada: "))
        iteracoes = int(input("Digite o máximo de iterações: "))
    except ValueError:
        print("Erro: Digite valores numéricos válidos")
        return
    
    print("\n" + "=" * 50)
    print("RESULTADOS DOS MÉTODOS NUMÉRICOS")
    print("=" * 50)
    
    testarMetodos.tests(a, b, x0, x1, func, precisao, iteracoes)

if __name__ == "__main__":
    main()