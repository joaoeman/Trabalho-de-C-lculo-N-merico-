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
    """
    Implementa o método da Falsa Posição para encontrar zeros de funções.
    
    Algoritmo:
    1. Verifica se há mudança de sinal no intervalo [a,b]
    2. Calcula o ponto c onde a reta que passa por (a,f(a)) e (b,f(b)) cruza o eixo x:
       c = a - f(a)*(b-a)/(f(b)-f(a))
    3. Avalia f(c):
       - Se |f(c)| < precisão: raiz encontrada
       - Se f(a)*f(c) < 0: raiz está em [a,c], atualiza b = c
       - Caso contrário: raiz está em [c,b], atualiza a = c
    4. Repete até convergir ou atingir o máximo de iterações
    
    Args:
        a (float): Extremo inferior do intervalo inicial
        b (float): Extremo superior do intervalo inicial
        func (sp.Expr): Função simbólica a ser analisada
        precisao (float): Critério de parada (tolerância)
        maxIter (int): Número máximo de iterações permitidas
        
    Returns:
        List[Union[int, float]]: Lista [iterações, raiz] onde:
            - iterações: número de iterações realizadas (ou -1 se não convergir)
            - raiz: valor aproximado da raiz (ou 0 se não convergir)
            
    Condições de parada:
        - |f(c)| < precisao: valor da função no ponto c é menor que a precisão
        - Número máximo de iterações atingido
        
    Exemplo:
        >>> func = sp.sympify("x**2 - 4")
        >>> resultado = falsaPosicao(1, 3, func, 0.000001, 100)
        >>> print(f"Raiz: {resultado[1]:.6f}, Iterações: {resultado[0]+1}")
    """
    # Verificar se há mudança de sinal no intervalo
    if func.subs(x, a) * func.subs(x, b) >= 0:
        return [-1, 0]  # Não há garantia de raiz no intervalo

    for i in range(maxIter):
        # Calcular os valores da função nos extremos
        fa, fb = func.subs(x, a), func.subs(x, b)
        
        # Verificar divisão por zero
        if abs(fb - fa) < 1e-15:
            print("Erro: Divisao por zero")
            return [-1,0]

        # Calcular o ponto c usando interpolação linear
        c = a - fa*(b-a)/(fb-fa)
        fc = func.subs(x, c)

        # Verificar critério de convergência
        if abs(fc) < precisao:
            return [i, c]  # Raiz encontrada com precisão desejada
        
        # Determinar em qual metade do intervalo está a raiz
        if fa*fc < 0:
            # Raiz está em [a, c]
            b = c
        else:
            # Raiz está em [c, b]
            a = c

    return [-1,0]  # Não convergiu no número máximo de iterações