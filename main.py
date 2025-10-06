import sympy as sp
import metodos.bisseccao
import metodos.falsaPosicao
import metodos.secante
import metodos.newton
import testarMetodos
import os

# Define a variável simbólica
x = sp.Symbol('x')

def ler_arquivo(nome_arquivo):
    """
    Lê os parâmetros de um arquivo de entrada.
    
    Formato esperado do arquivo:
    - Linha 1: Função em x (ex: x**2 - 4)
    - Linha 2: Início do intervalo [a]
    - Linha 3: Fim do intervalo [b]
    - Linha 4: Primeira estimativa inicial [x0]
    - Linha 5: Segunda estimativa inicial [x1]
    - Linha 6: Precisão desejada (ex: 0.000001)
    - Linha 7: Máximo de iterações (ex: 100)
    
    Args:
        nome_arquivo (str): Caminho do arquivo de entrada
        
    Returns:
        tuple: (func, a, b, x0, x1, precisao, iteracoes) ou None se erro
    """
    try:
        with open(nome_arquivo, 'r') as file:
            linhas = file.readlines()
            
            # Remover espaços em branco e quebras de linha
            linhas = [linha.strip() for linha in linhas if linha.strip()]
            
            if len(linhas) < 7:
                print(f"[ERRO] O arquivo deve conter 7 linhas de parametros")
                return None
            
            # Processar função
            func_str = linhas[0]
            func = sp.sympify(func_str)
            
            # Processar parâmetros numéricos
            a = float(linhas[1])
            b = float(linhas[2])
            x0 = float(linhas[3])
            x1 = float(linhas[4])
            precisao = float(linhas[5])
            iteracoes = int(linhas[6])
            
            return func, a, b, x0, x1, precisao, iteracoes
            
    except FileNotFoundError:
        print(f"[ERRO] Arquivo '{nome_arquivo}' nao encontrado")
        return None
    except Exception as e:
        print(f"[ERRO] ao ler arquivo: {e}")
        return None

def entrada_manual():
    """
    Solicita entrada manual dos parâmetros pelo usuário.
    
    Returns:
        tuple: (func, a, b, x0, x1, precisao, iteracoes) ou None se erro
    """
    print("\nENTRADA MANUAL DE DADOS")
    print("-" * 50)
    
    # Recebe a função como string
    func_str = input("Digite a função em x: ")
    
    try:
        # Converte a string em expressão simbólica
        func = sp.sympify(func_str)
        print(f"[OK] Funcao: {func}")
        
        # Calcula a derivada
        derivada = sp.diff(func, x)
        print(f"[OK] Derivada: {derivada}")
        
    except Exception as e:
        print(f"[ERRO] ao processar a funcao: {e}")
        return None
    
    # Parâmetros para métodos de intervalo
    try:
        a = float(input("Digite o início do intervalo [a,b]: "))
        b = float(input("Digite o fim do intervalo [a,b]: "))
        x0 = float(input("Digite uma estimativa inicial x0: "))
        x1 = float(input("Digite uma segunda estimativa inicial x1: "))
        precisao = float(input("Digite a precisão desejada (ex: 0.000001): "))
        iteracoes = int(input("Digite o máximo de iterações (ex: 100): "))
        
        return func, a, b, x0, x1, precisao, iteracoes
        
    except ValueError:
        print("[ERRO] Digite valores numericos validos")
        return None

def executar_simulacao(func, a, b, x0, x1, precisao, iteracoes):
    """
    Executa a simulação dos métodos numéricos com os parâmetros fornecidos.
    
    Args:
        func: Função simbólica
        a: Início do intervalo
        b: Fim do intervalo
        x0: Primeira estimativa inicial
        x1: Segunda estimativa inicial
        precisao: Precisão desejada
        iteracoes: Máximo de iterações
    """
    print("\n" + "=" * 100)
    print("                        SIMULACAO DE METODOS NUMERICOS - ZEROS DE FUNCOES")
    print("=" * 100)
    print(f"\nPARAMETROS DA SIMULACAO:")
    print(f"   - Funcao: f(x) = {func}")
    print(f"   - Intervalo: [{a}, {b}]")
    print(f"   - Estimativas iniciais: x0 = {x0}, x1 = {x1}")
    print(f"   - Precisao: {precisao}")
    print(f"   - Maximo de iteracoes: {iteracoes}")
    
    testarMetodos.tests(a, b, x0, x1, func, precisao, iteracoes)

def menu_principal():
    """
    Exibe o menu principal e controla o fluxo do programa.
    """
    while True:
        print("\n" + "=" * 100)
        print("                    SIMULADOR DE METODOS NUMERICOS - ZEROS DE FUNCOES")
        print("=" * 100)
        print("\nMENU PRINCIPAL:")
        print("   1. Entrada manual de dados")
        print("   2. Ler dados de arquivo (input.txt)")
        print("   3. Ler dados de arquivo (input2.txt)")
        print("   4. Ler dados de arquivo personalizado")
        print("   5. Exemplos de problemas de engenharia")
        print("   0. Sair")
        print("-" * 100)
        
        try:
            opcao = input("\n=> Escolha uma opcao: ").strip()
            
            if opcao == '0':
                print("\nEncerrando o programa. Ate logo!")
                break
                
            elif opcao == '1':
                # Entrada manual
                resultado = entrada_manual()
                if resultado:
                    executar_simulacao(*resultado)
                    
            elif opcao == '2':
                # Ler de input.txt
                print("\nLendo dados de 'input.txt'...")
                resultado = ler_arquivo('input.txt')
                if resultado:
                    executar_simulacao(*resultado)
                    
            elif opcao == '3':
                # Ler de input2.txt
                print("\nLendo dados de 'input2.txt'...")
                resultado = ler_arquivo('input2.txt')
                if resultado:
                    executar_simulacao(*resultado)
                    
            elif opcao == '4':
                # Ler de arquivo personalizado
                nome_arquivo = input("\nDigite o nome do arquivo: ").strip()
                print(f"Lendo dados de '{nome_arquivo}'...")
                resultado = ler_arquivo(nome_arquivo)
                if resultado:
                    executar_simulacao(*resultado)
                    
            elif opcao == '5':
                # Exemplos de problemas de engenharia
                menu_exemplos()
                
            else:
                print("\n[ERRO] Opcao invalida! Por favor, escolha uma opcao valida.")
                
        except KeyboardInterrupt:
            print("\n\nPrograma interrompido pelo usuario. Ate logo!")
            break
        except Exception as e:
            print(f"\n[ERRO] Erro inesperado: {e}")

def menu_exemplos():
    """
    Exibe o menu de exemplos de problemas de engenharia.
    """
    print("\n" + "=" * 100)
    print("                           EXEMPLOS DE PROBLEMAS DE ENGENHARIA")
    print("=" * 100)
    print("\nPROBLEMAS DISPONIVEIS:")
    print("\n1. EXEMPLO DO TRABALHO: Acelerador de Particulas")
    print("   Problema: O polinomio f(x) = x³ – 5x² + 8x – 4 representa o potencial magnetico")
    print("   de um tubo no qual foram dispostos varios imas, no acelerador de particulas na Suica.")
    print("   Objetivo: Para qual valor de x o campo se anula?")
    print("   Arquivo: input2.txt")
    
    print("\n2. PROBLEMA 1: Concentracao de Bacterias")
    print("   Problema: A concentracao C de uma bacteria poluente em uma lagoa decresce conforme:")
    print("   C = 80e^(-2t) + 20e^(-0.1t)")
    print("   Objetivo: Determinar o tempo necessario para reduzir a concentracao da bacteria a 10.")
    print("   Sugestao: Resolva 80*exp(-2*t) + 20*exp(-0.1*t) - 10 = 0")
    
    print("\n3. PROBLEMA 2: Deslocamento de Estruturas")
    print("   Problema: O deslocamento horizontal da estrutura de um predio e definido por:")
    print("   y(t) = 10e^(-kt)cos(wt) onde k = 0.5 e w = 2")
    print("   Objetivo: Determinar o tempo necessario para que o deslocamento horizontal chegue a 5.")
    print("   Sugestao: Resolva 10*exp(-0.5*t)*cos(2*t) - 5 = 0")
    
    print("\n" + "-" * 100)
    opcao = input("\n=> Digite o numero do exemplo para executar ou 0 para voltar: ").strip()
    
    if opcao == '1':
        print("\nExecutando exemplo do acelerador de particulas...")
        resultado = ler_arquivo('input2.txt')
        if resultado:
            executar_simulacao(*resultado)
    elif opcao == '2':
        print("\nProblema de Concentracao de Bacterias")
        print("Digite manualmente a funcao: 80*exp(-2*t) + 20*exp(-0.1*t) - 10")
        print("(Substitua 't' por 'x' na entrada)")
        input("\nPressione ENTER para continuar...")
        resultado = entrada_manual()
        if resultado:
            executar_simulacao(*resultado)
    elif opcao == '3':
        print("\nProblema de Deslocamento de Estruturas")
        print("Digite manualmente a funcao: 10*exp(-0.5*x)*cos(2*x) - 5")
        input("\nPressione ENTER para continuar...")
        resultado = entrada_manual()
        if resultado:
            executar_simulacao(*resultado)

def main():
    """
    Função principal do programa.
    """
    menu_principal()

if __name__ == "__main__":
    main()