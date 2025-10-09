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
    
    for i in range(iteracao):
        fx0 = float(func.subs(x,x0))
        fx1 = float(func.subs(x,x1))

        if math.isnan(fx0) or math.isnan(fx1) or math.isinf(fx0) or math.isinf(fx1):
            print(f"Erro: Valores inválidos na iteração {i}")
            return [-1, 0]
        
        if abs(fx1 - fx0) < 1e-15:
            print(f"Erro: Divisão por zero iminente na iteração {i} (f(x1) - f(x0) ≈ 0)")
            return [-1, 0]
        
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        
        if math.isnan(x2) or math.isinf(x2):
            print(f"Erro: x2 inválido na iteração {i}")
            return [-1, 0]
        
        fx2 = float(func.subs(x, x2))
        
        if math.isnan(fx2) or math.isinf(fx2):
            print(f"Erro: f(x2) inválido na iteração {i}")
            return [-1, 0]

        if(abs(x2-x1)<precisao) or abs(func.subs(x,x2))<precisao:
            return [i,x2] 
        
        x0,x1 = x1,x2
        
    return [-1,0]

        
