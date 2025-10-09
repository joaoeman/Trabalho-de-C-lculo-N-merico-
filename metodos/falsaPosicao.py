"""
Módulo: Método da Falsa Posição (Regula Falsi)
Descrição: Implementa o método da Falsa Posição para encontrar zeros de funções contínuas.

O método da Falsa Posição é uma variação do método da Bissecção que utiliza
interpolação linear ao invés de dividir o intervalo ao meio. Conecta os pontos
(a, f(a)) e (b, f(b)) por uma reta e usa o ponto onde a reta cruza o eixo x
como nova aproximação da raiz.

Vantagens:
    - Geralmente converge mais rápido que a Bissecção
    - Sempre converge se houver mudança de sinal
    - Usa informação dos valores da função

Desvantagens:
    - Pode ser mais lento que métodos de ordem superior
    - Pode convergir lentamente se a função for muito convexa/côncava
"""

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