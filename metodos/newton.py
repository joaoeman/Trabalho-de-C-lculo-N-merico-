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
    
    xAtual = x0

    for i in range(iteracoes):
        fx, dfx = func.subs(x, xAtual), derivative.subs(x, xAtual)
        
        if abs(dfx) < 1e-15:
            print(f"Derivada proxima de zero em x = {xAtual:.6f}")
            return [-1,0] 
        
        novoX = xAtual - fx / dfx

        if math.isnan(novoX) or math.isinf(novoX):
            print(f"novo x inválido na iteração {i+1}")
            return [-1, 0]

        erro_x = abs(novoX-xAtual)

        try:
            erro_f = abs(float(func.subs(x, novoX)))
        except Exception as e:
            print(f"Erro ao calcular f(x_novo) na iteração {i+1}: {e}")
            return [-1, 0]
        
        if (erro_f < precisao) or (erro_x < precisao):
            return [i, novoX]

        xAtual = novoX
        
    return [-1,0] 