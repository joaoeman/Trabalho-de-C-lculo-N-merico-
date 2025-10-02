import sympy as sp
from typing import List, Union

x = sp.Symbol('x')

def secante(x0: float, x1:float, func: sp.Expr,precisao:float,iteracao:int)-> List[Union[int,float]]:
    for i in range(iteracao):
        x2 = x1 + - func.subs(x,x1)*(x1-x0)/(func.subs(x,x1)-func.subs(x,x0))

        if(abs(x2-x1)<precisao) or abs(func.subs(x,x2))<precisao:
            return [i,x2]
        x0,x1 = x1,x2
    return [-1,0]

        
