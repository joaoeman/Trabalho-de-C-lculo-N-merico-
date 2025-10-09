"""
Módulo: Método da Bissecção
Descrição: Implementa o método da Bissecção para encontrar zeros de funções contínuas.

O método da Bissecção é um método iterativo baseado no Teorema do Valor Intermediário.
Dado um intervalo [a,b] onde f(a) e f(b) têm sinais opostos, o método reduz
progressivamente o intervalo pela metade até encontrar a raiz com a precisão desejada.

Vantagens:
    - Sempre converge se a função for contínua e houver mudança de sinal
    - Robusto e estável
    - Simples de implementar

Desvantagens:
    - Convergência linear (lenta)
    - Requer intervalo inicial com mudança de sinal
"""

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


        
