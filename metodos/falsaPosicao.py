import sympy as sp
from typing import List, Union

x = sp.Symbol('x')

def falsaPosicao(a, b: float, func: sp.Expr, precisao: float, maxIter: int) -> List[Union[int,float]]:
    
    if func.subs(x, a) * func.subs(x, b) >= 0:
        return [-1, 0]

    for i in range(maxIter):
        fa, fb = func.subs(x, a), func.subs(x, b)
        
        if abs(fb - fa) < 1e-15:
            print("Erro: Divisao por zero")
            return [-1,0]

        c = a - fa*(b-a)/(fb-fa)
        fc = func.subs(x, c)

        if abs(fc) < precisao:
            return [i, c]
        
        if fa*fc < 0:
            b = c
        else:
            a = c

    return [-1,0]