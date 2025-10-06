"""
Arquivo de Exemplo: Como usar o simulador de métodos numéricos

Este arquivo demonstra como usar diretamente os métodos implementados
sem passar pelo menu interativo do main.py.

Útil para:
- Testes automatizados
- Integração com outros sistemas
- Experimentação rápida
"""

import sympy as sp
import testarMetodos

# Define a variável simbólica
x = sp.Symbol('x')

def exemplo_basico():
    """
    Exemplo básico: Encontrar raiz de x² - 4 = 0
    Raiz esperada: x = 2
    """
    print("="*80)
    print("EXEMPLO 1: Função Simples - x² - 4 = 0")
    print("="*80)
    
    # Definir a função
    func = sp.sympify("x**2 - 4")
    
    # Parâmetros
    a = 1.0           # Início do intervalo
    b = 3.0           # Fim do intervalo
    x0 = 1.5          # Primeira estimativa
    x1 = 2.5          # Segunda estimativa
    precisao = 0.000001  # Precisão desejada
    iteracoes = 100   # Máximo de iterações
    
    # Executar comparação de métodos
    testarMetodos.tests(a, b, x0, x1, func, precisao, iteracoes)

def exemplo_acelerador_particulas():
    """
    Exemplo do trabalho: Acelerador de Partículas
    f(x) = x³ - 5x² + 8x - 4
    """
    print("\n" + "="*80)
    print("EXEMPLO 2: Acelerador de Partículas - x³ - 5x² + 8x - 4 = 0")
    print("="*80)
    
    func = sp.sympify("x**3 - 5*x**2 + 8*x - 4")
    a = 0.0
    b = 3.0
    x0 = 1.0
    x1 = 2.0
    precisao = 0.000001
    iteracoes = 100
    
    testarMetodos.tests(a, b, x0, x1, func, precisao, iteracoes)

def exemplo_bacterias():
    """
    Problema de Engenharia 1: Concentração de Bactérias
    C(t) = 80e^(-2t) + 20e^(-0.1t) - 10
    """
    print("\n" + "="*80)
    print("EXEMPLO 3: Concentração de Bactérias")
    print("="*80)
    
    func = sp.sympify("80*exp(-2*x) + 20*exp(-0.1*x) - 10")
    a = 0.0
    b = 10.0
    x0 = 1.0
    x1 = 2.0
    precisao = 0.000001
    iteracoes = 100
    
    testarMetodos.tests(a, b, x0, x1, func, precisao, iteracoes)

def exemplo_deslocamento():
    """
    Problema de Engenharia 2: Deslocamento de Estruturas
    y(t) = 10e^(-0.5t)cos(2t) - 5
    """
    print("\n" + "="*80)
    print("EXEMPLO 4: Deslocamento de Estruturas de Prédio")
    print("="*80)
    
    func = sp.sympify("10*exp(-0.5*x)*cos(2*x) - 5")
    a = 0.0
    b = 5.0
    x0 = 0.5
    x1 = 1.5
    precisao = 0.000001
    iteracoes = 100
    
    testarMetodos.tests(a, b, x0, x1, func, precisao, iteracoes)

def exemplo_funcao_trigonometrica():
    """
    Exemplo adicional: Função trigonométrica
    f(x) = sin(x) - x/2
    """
    print("\n" + "="*80)
    print("EXEMPLO 5: Função Trigonométrica - sin(x) - x/2 = 0")
    print("="*80)
    
    func = sp.sympify("sin(x) - x/2")
    a = 1.0
    b = 3.0
    x0 = 1.5
    x1 = 2.0
    precisao = 0.000001
    iteracoes = 100
    
    testarMetodos.tests(a, b, x0, x1, func, precisao, iteracoes)

def exemplo_com_metodo_individual():
    """
    Exemplo de como usar um método individual
    """
    print("\n" + "="*80)
    print("EXEMPLO 6: Usando um Método Individual (Bissecção)")
    print("="*80)
    
    import metodos.bisseccao
    
    func = sp.sympify("x**2 - 4")
    a = 1.0
    b = 3.0
    precisao = 0.000001
    max_iter = 100
    
    resultado = metodos.bisseccao.bisseccao(a, b, max_iter, func, precisao)
    
    if resultado[0] != -1:
        print(f"[OK] Raiz encontrada: {resultado[1]:.10f}")
        print(f"Iteracoes: {resultado[0] + 1}")
        print(f"Verificacao: f({resultado[1]:.8f}) = {float(func.subs(x, resultado[1])):.2e}")
    else:
        print("[ERRO] Metodo nao convergiu")

def main():
    """
    Executa todos os exemplos em sequência
    """
    print("\n" + "="*80)
    print(" "*20 + "EXEMPLOS DE USO DO SIMULADOR")
    print("="*80 + "\n")
    
    # Executar exemplos
    exemplo_basico()
    input("\n[PAUSA] Pressione ENTER para continuar para o proximo exemplo...")
    
    exemplo_acelerador_particulas()
    input("\n[PAUSA] Pressione ENTER para continuar para o proximo exemplo...")
    
    exemplo_bacterias()
    input("\n[PAUSA] Pressione ENTER para continuar para o proximo exemplo...")
    
    exemplo_deslocamento()
    input("\n[PAUSA] Pressione ENTER para continuar para o proximo exemplo...")
    
    exemplo_funcao_trigonometrica()
    input("\n[PAUSA] Pressione ENTER para continuar para o proximo exemplo...")
    
    exemplo_com_metodo_individual()
    
    print("\n" + "="*80)
    print("[OK] Todos os exemplos foram executados com sucesso!")
    print("="*80)

if __name__ == "__main__":
    main()
