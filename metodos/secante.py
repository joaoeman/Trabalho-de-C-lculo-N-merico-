"""
Módulo: Método da Secante
Descrição: Implementa o método da Secante para encontrar zeros de funções.

O método da Secante é similar ao método de Newton-Raphson, mas não requer
o cálculo da derivada. Ao invés disso, aproxima a derivada usando uma diferença
finita: f'(x) ≈ (f(x1) - f(x0)) / (x1 - x0)

Vantagens:
    - Não requer cálculo da derivada
    - Convergência superlinear (~1.618)
    - Geralmente mais rápido que métodos de intervalo

Desvantagens:
    - Pode divergir se as estimativas iniciais forem ruins
    - Requer duas estimativas iniciais
    - Menos robusto que métodos de intervalo
"""

import sympy as sp
import math
from typing import List, Union


x = sp.Symbol('x')

def secante(x0: float, x1:float, func: sp.Expr,precisao:float,iteracao:int)-> List[Union[int,float]]:
    """
    Implementa o método da Secante para encontrar zeros de funções.
    
    Algoritmo:
    1. Começa com duas estimativas iniciais x0 e x1
    2. Calcula f(x0) e f(x1)
    3. Usa a fórmula da secante para calcular a próxima aproximação:
       x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
    4. Verifica critérios de convergência:
       - |x2 - x1| < precisão: valores consecutivos são próximos
       - |f(x2)| < precisão: valor da função é próximo de zero
    5. Atualiza: x0 = x1, x1 = x2
    6. Repete até convergir ou atingir o máximo de iterações
    
    Args:
        x0 (float): Primeira estimativa inicial
        x1 (float): Segunda estimativa inicial
        func (sp.Expr): Função simbólica a ser analisada
        precisao (float): Critério de parada (tolerância)
        iteracao (int): Número máximo de iterações permitidas
        
    Returns:
        List[Union[int, float]]: Lista [iterações, raiz] onde:
            - iterações: número de iterações realizadas (ou -1 se não convergir)
            - raiz: valor aproximado da raiz (ou 0 se não convergir)
            
    Condições de parada:
        - |x2 - x1| < precisao: valores consecutivos estão próximos
        - |f(x2)| < precisao: valor da função é próximo de zero
        - Número máximo de iterações atingido
        
    Exemplo:
        >>> func = sp.sympify("x**2 - 4")
        >>> resultado = secante(1.5, 2.5, func, 0.000001, 100)
        >>> print(f"Raiz: {resultado[1]:.6f}, Iterações: {resultado[0]+1}")
    """
    for i in range(iteracao):
        # Calcular f(x0) e f(x1)
        fx0 = float(func.subs(x,x0))
        fx1 = float(func.subs(x,x1))

        # Verificar se os valores são válidos (não NaN ou infinito)
        if math.isnan(fx0) or math.isnan(fx1) or math.isinf(fx0) or math.isinf(fx1):
            print(f"Erro: Valores inválidos na iteração {i}")
            return [-1, 0]
        
        # Verificar divisão por zero (quando f(x1) ≈ f(x0))
        if abs(fx1 - fx0) < 1e-15:
            print(f"Erro: Divisão por zero iminente na iteração {i} (f(x1) - f(x0) ≈ 0)")
            return [-1, 0]
        
        # Aplicar a fórmula da secante
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        
        # Verificar se x2 é válido
        if math.isnan(x2) or math.isinf(x2):
            print(f"Erro: x2 inválido na iteração {i}")
            return [-1, 0]
        
        # Calcular f(x2)
        fx2 = float(func.subs(x, x2))
        
        # Verificar se f(x2) é válido
        if math.isnan(fx2) or math.isinf(fx2):
            print(f"Erro: f(x2) inválido na iteração {i}")
            return [-1, 0]

        # Verificar critérios de convergência
        if(abs(x2-x1)<precisao) or abs(func.subs(x,x2))<precisao:
            return [i,x2]  # Raiz encontrada com precisão desejada
        
        # Atualizar valores para próxima iteração
        x0,x1 = x1,x2
        
    return [-1,0]  # Não convergiu no número máximo de iterações

        
