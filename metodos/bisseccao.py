import sympy as sp
from typing import List, Union

x = sp.Symbol('x')

def bisseccao(a: float, b: float, intervalo: int, func: sp.Expr, precisao: float) -> List[Union[int, float]]:
    
    if func.subs(x,b)*func.subs(x,a) > 0:
        return [-1,0]
    i = 0
    for i in range(intervalo):
        m = ((a+b)/2)

        if abs(func.subs(x,m))< precisao or abs(a - b) < precisao:
            return [i,m]
        
        elif func.subs(x,m)*func.subs(x,a)< 0:
            b = m

        elif func.subs(x,m)*func.subs(x,b)< 0:
            a = m
    return [-1,0]


        
