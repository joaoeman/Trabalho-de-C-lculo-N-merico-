import sympy as sp
from typing import List, Union
import math
x = sp.Symbol('x')

def newton(x0: float, func: sp.Expr, derivative: sp.Expr, precisao: float, iteracoes: int) -> List[Union[int, float]]:
    
    xAtual = x0

    for i in range(iteracoes):
        fx, dfx = func.subs(x, xAtual), derivative.subs(x, xAtual)
        
        # Verificar se a derivada eh zero
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