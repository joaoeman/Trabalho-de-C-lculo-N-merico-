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
    """
    Implementa o método da Bissecção para encontrar zeros de funções.
    
    Algoritmo:
    1. Verifica se há mudança de sinal no intervalo [a,b]
    2. Calcula o ponto médio m = (a+b)/2
    3. Avalia f(m):
       - Se |f(m)| < precisão ou |a-b| < precisão: raiz encontrada
       - Se f(m)*f(a) < 0: raiz está em [a,m], atualiza b = m
       - Se f(m)*f(b) < 0: raiz está em [m,b], atualiza a = m
    4. Repete até convergir ou atingir o máximo de iterações
    
    Args:
        a (float): Extremo inferior do intervalo inicial
        b (float): Extremo superior do intervalo inicial
        intervalo (int): Número máximo de iterações permitidas
        func (sp.Expr): Função simbólica a ser analisada
        precisao (float): Critério de parada (tolerância)
        
    Returns:
        List[Union[int, float]]: Lista [iterações, raiz] onde:
            - iterações: número de iterações realizadas (ou -1 se não convergir)
            - raiz: valor aproximado da raiz (ou 0 se não convergir)
            
    Condições de parada:
        - |f(m)| < precisao: valor da função no ponto médio é menor que a precisão
        - |a - b| < precisao: o intervalo é menor que a precisão
        - Número máximo de iterações atingido
        
    Exemplo:
        >>> func = sp.sympify("x**2 - 4")
        >>> resultado = bisseccao(1, 3, 100, func, 0.000001)
        >>> print(f"Raiz: {resultado[1]:.6f}, Iterações: {resultado[0]+1}")
    """
    # Verificar se há mudança de sinal no intervalo (Teorema do Valor Intermediário)
    if func.subs(x,b)*func.subs(x,a) > 0:
        return [-1,0]  # Não há garantia de raiz no intervalo
    
    i = 0
    for i in range(intervalo):
        # Calcular o ponto médio do intervalo
        m = ((a+b)/2)

        # Verificar critérios de convergência
        if abs(func.subs(x,m))< precisao or abs(a - b) < precisao:
            return [i,m]  # Raiz encontrada com precisão desejada
        
        # Determinar em qual metade do intervalo está a raiz
        elif func.subs(x,m)*func.subs(x,a)< 0:
            # Raiz está na primeira metade [a, m]
            b = m

        elif func.subs(x,m)*func.subs(x,b)< 0:
            # Raiz está na segunda metade [m, b]
            a = m
            
    return [-1,0]  # Não convergiu no número máximo de iterações


        
