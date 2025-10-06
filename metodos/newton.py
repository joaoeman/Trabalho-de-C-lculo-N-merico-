"""
Módulo: Método de Newton-Raphson
Descrição: Implementa o método de Newton-Raphson para encontrar zeros de funções diferenciáveis.

O método de Newton-Raphson usa a reta tangente à curva f(x) no ponto atual
para encontrar uma melhor aproximação da raiz. É um dos métodos mais eficientes
quando próximo da raiz.

Vantagens:
    - Convergência quadrática quando próximo da raiz
    - Geralmente o mais rápido dos métodos iterativos
    - Requer apenas uma estimativa inicial

Desvantagens:
    - Requer cálculo da derivada
    - Pode divergir se a estimativa inicial for ruim
    - Falha se a derivada for zero ou muito pequena
    - Não garante convergência
"""

import sympy as sp
from typing import List, Union
import math
x = sp.Symbol('x')

def newton(x0: float, func: sp.Expr, derivative: sp.Expr, precisao: float, iteracoes: int) -> List[Union[int, float]]:
    """
    Implementa o método de Newton-Raphson para encontrar zeros de funções.
    
    Algoritmo:
    1. Começa com uma estimativa inicial x0
    2. Para cada iteração:
       - Calcula f(x_atual) e f'(x_atual)
       - Verifica se f'(x_atual) ≈ 0 (evitar divisão por zero)
       - Calcula nova aproximação: x_novo = x_atual - f(x_atual)/f'(x_atual)
       - Verifica critérios de convergência:
         * |f(x_novo)| < precisão: valor da função é próximo de zero
         * |x_novo - x_atual| < precisão: valores consecutivos são próximos
    3. Atualiza x_atual = x_novo
    4. Repete até convergir ou atingir o máximo de iterações
    
    Args:
        x0 (float): Estimativa inicial da raiz
        func (sp.Expr): Função simbólica a ser analisada
        derivative (sp.Expr): Derivada da função (f'(x))
        precisao (float): Critério de parada (tolerância)
        iteracoes (int): Número máximo de iterações permitidas
        
    Returns:
        List[Union[int, float]]: Lista [iterações, raiz] onde:
            - iterações: número de iterações realizadas (ou -1 se não convergir)
            - raiz: valor aproximado da raiz (ou 0 se não convergir)
            
    Condições de parada:
        - |f(x_novo)| < precisao: valor da função é próximo de zero
        - |x_novo - x_atual| < precisao: valores consecutivos estão próximos
        - Número máximo de iterações atingido
        - Derivada próxima de zero (evitar divisão por zero)
        
    Exemplo:
        >>> func = sp.sympify("x**2 - 4")
        >>> derivada = sp.diff(func, x)
        >>> resultado = newton(1.5, func, derivada, 0.000001, 100)
        >>> print(f"Raiz: {resultado[1]:.6f}, Iterações: {resultado[0]+1}")
    """
    # Inicializar valor atual com a estimativa inicial
    xAtual = x0

    for i in range(iteracoes):
        # Calcular f(x_atual) e f'(x_atual)
        fx, dfx = func.subs(x, xAtual), derivative.subs(x, xAtual)
        
        # Verificar se a derivada é zero ou muito pequena
        if abs(dfx) < 1e-15:
            print(f"Derivada proxima de zero em x = {xAtual:.6f}")
            return [-1,0]  # Método falha quando f'(x) ≈ 0
        
        # Aplicar fórmula de Newton-Raphson
        novoX = xAtual - fx / dfx

        # Verificar se o novo valor é válido (não NaN ou infinito)
        if math.isnan(novoX) or math.isinf(novoX):
            print(f"novo x inválido na iteração {i+1}")
            return [-1, 0]

        # Calcular erro entre iterações consecutivas
        erro_x = abs(novoX-xAtual)

        # Calcular erro da função no novo ponto
        try:
            erro_f = abs(float(func.subs(x, novoX)))
        except Exception as e:
            print(f"Erro ao calcular f(x_novo) na iteração {i+1}: {e}")
            return [-1, 0]
        
        # Verificar critérios de convergência
        if (erro_f < precisao) or (erro_x < precisao):
            return [i, novoX]  # Raiz encontrada com precisão desejada

        # Atualizar valor para próxima iteração
        xAtual = novoX
        
    return [-1,0]  # Não convergiu no número máximo de iterações