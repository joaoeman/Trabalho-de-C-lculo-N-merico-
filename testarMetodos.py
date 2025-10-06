"""
Módulo: Teste e Comparação de Métodos Numéricos
Descrição: Módulo responsável por executar e comparar os diferentes métodos
          numéricos de busca de zeros de funções.

Este módulo executa os quatro métodos principais (Bissecção, Falsa Posição,
Secante e Newton-Raphson) com os mesmos parâmetros e gera uma análise
comparativa detalhada incluindo:
    - Número de iterações
    - Tempo de execução (em milissegundos)
    - Raiz encontrada
    - Precisão final alcançada |f(raiz)|
    - Estatísticas e ranking de desempenho
"""

import sympy as sp
import metodos.bisseccao
import metodos.falsaPosicao
import metodos.secante
import metodos.newton
import time

x = sp.Symbol('x')

def tests(a:float, b: float, x0: float, x1: float, func: sp.Expr, precisao: float, iteracoes: int):
    """
    Executa e compara os quatro métodos numéricos de busca de zeros.
    
    Esta função executa os métodos da Bissecção, Falsa Posição, Secante e
    Newton-Raphson sobre a mesma função com os mesmos parâmetros, medindo
    o desempenho de cada um e gerando uma análise comparativa completa.
    
    Args:
        a (float): Extremo inferior do intervalo [a,b] para métodos de intervalo
        b (float): Extremo superior do intervalo [a,b] para métodos de intervalo
        x0 (float): Primeira estimativa inicial para Secante e Newton-Raphson
        x1 (float): Segunda estimativa inicial para o método da Secante
        func (sp.Expr): Função simbólica a ser analisada
        precisao (float): Critério de parada (tolerância) para todos os métodos
        iteracoes (int): Número máximo de iterações permitidas
        
    Saída:
        Imprime na tela:
        - Resultados individuais de cada método
        - Tabela comparativa completa com todos os métodos
        - Análise estatística de desempenho
        - Ranking dos métodos por eficiência
        - Comparações detalhadas entre os métodos
        
    Exemplo:
        >>> import sympy as sp
        >>> x = sp.Symbol('x')
        >>> func = sp.sympify("x**2 - 4")
        >>> tests(1, 3, 1.5, 2.5, func, 0.000001, 100)
    """
    # Calcular a derivada da função para Newton-Raphson
    derivada = sp.diff(func, x)
    
    # Método da Bissecção
    print("\n1. MÉTODO DA BISSECÇÃO")
    print("-" * 30)
    tempo_inicio = time.perf_counter()
    resultado_biss = metodos.bisseccao.bisseccao(a, b, iteracoes, func, precisao)
    tempo_fim = time.perf_counter()
    tempo_biss = (tempo_fim - tempo_inicio) * 1000  # Converter para milissegundos
    
    print(f"Resultado: {resultado_biss}")
    if resultado_biss[0] != -1:
        print(f"[OK] Raiz encontrada: {resultado_biss[1]:.8f}")
        print(f"Iteracoes: {resultado_biss[0] + 1}")
        print(f"Tempo de execucao: {tempo_biss:.6f} ms")
        
        # Verificação - Precisão final alcançada
        verificacao = func.subs(x, resultado_biss[1])
        precisao_final = abs(float(verificacao))
        print(f"Verificacao f({resultado_biss[1]:.8f}) = {float(verificacao):.2e}")
        print(f"Precisao final |f(raiz)| = {precisao_final:.2e}")
    else:
        print("[ERRO] Raiz nao encontrada no numero maximo de iteracoes")
        tempo_biss = float('inf')
        precisao_final = float('inf')
    
    # Método da Falsa Posição
    print("\n2. MÉTODO DA FALSA POSIÇÃO")
    print("-" * 30)
    tempo_inicio = time.perf_counter()
    resultado_fp = metodos.falsaPosicao.falsaPosicao(a, b, func, precisao, iteracoes)
    tempo_fim = time.perf_counter()
    tempo_fp = (tempo_fim - tempo_inicio) * 1000  # Converter para milissegundos
    
    print(f"Resultado: {resultado_fp}")
    if resultado_fp[0] != -1:
        print(f"[OK] Raiz encontrada: {resultado_fp[1]:.8f}")
        print(f"Iteracoes: {resultado_fp[0] + 1}")
        print(f"Tempo de execucao: {tempo_fp:.6f} ms")
        
        # Verificação - Precisão final alcançada
        verificacao = func.subs(x, resultado_fp[1])
        precisao_final_fp = abs(float(verificacao))
        print(f"Verificacao f({resultado_fp[1]:.8f}) = {float(verificacao):.2e}")
        print(f"Precisao final |f(raiz)| = {precisao_final_fp:.2e}")
    else:
        print("[ERRO] Raiz nao encontrada no numero maximo de iteracoes")
        tempo_fp = float('inf')
        precisao_final_fp = float('inf')
    
    # Método da Secante
    print("\n3. MÉTODO DA SECANTE")
    print("-" * 30)
    try:
        tempo_inicio = time.perf_counter()
        resultado_sc = metodos.secante.secante(x0, x1, func, precisao, iteracoes)
        tempo_fim = time.perf_counter()
        tempo_sc = (tempo_fim - tempo_inicio) * 1000  # Converter para milissegundos
        
        print(f"Resultado: {resultado_sc}")
        if resultado_sc[0] != -1:
            print(f"[OK] Raiz encontrada: {resultado_sc[1]:.8f}")
            print(f"Iteracoes: {resultado_sc[0] + 1}")
            print(f"Tempo de execucao: {tempo_sc:.6f} ms")
            
            # Verificação - Precisão final alcançada
            verificacao = func.subs(x, resultado_sc[1])
            precisao_final_sc = abs(float(verificacao))
            print(f"Verificacao f({resultado_sc[1]:.8f}) = {float(verificacao):.2e}")
            print(f"Precisao final |f(raiz)| = {precisao_final_sc:.2e}")
        else:
            print("[ERRO] Raiz nao encontrada no numero maximo de iteracoes")
            tempo_sc = float('inf')
            precisao_final_sc = float('inf')
    except Exception as e:
        print(f"[ERRO] Erro no metodo da secante: {e}")
        resultado_sc = [-1, 0]
        tempo_sc = float('inf')
        precisao_final_sc = float('inf')

    # Método de Newton-Raphson
    print("\n4. MÉTODO DE NEWTON-RAPHSON")
    print("-" * 30)
    print(f"Derivada: f'(x) = {derivada}")
    try:
        tempo_inicio = time.perf_counter()
        resultado_newton = metodos.newton.newton(x0, func, derivada, precisao, iteracoes)
        tempo_fim = time.perf_counter()
        tempo_newton = (tempo_fim - tempo_inicio) * 1000  # Converter para milissegundos
        
        print(f"Resultado: {resultado_newton}")
        if resultado_newton[0] != -1:
            print(f"[OK] Raiz encontrada: {resultado_newton[1]:.8f}")
            print(f"Iteracoes: {resultado_newton[0] + 1}")
            print(f"Tempo de execucao: {tempo_newton:.6f} ms")
            
            # Verificação - Precisão final alcançada
            verificacao = func.subs(x, resultado_newton[1])
            precisao_final_newton = abs(float(verificacao))
            print(f"Verificacao f({resultado_newton[1]:.8f}) = {float(verificacao):.2e}")
            print(f"Precisao final |f(raiz)| = {precisao_final_newton:.2e}")
            
            # Verificação da derivada no ponto
            verificacao_deriv = derivada.subs(x, resultado_newton[1])
            print(f"f'({resultado_newton[1]:.8f}) = {float(verificacao_deriv):.2e}")
        else:
            print("[ERRO] Raiz nao encontrada no numero maximo de iteracoes")
            tempo_newton = float('inf')
            precisao_final_newton = float('inf')
    except Exception as e:
        print(f"[ERRO] Erro no metodo de Newton-Raphson: {e}")
        resultado_newton = [-1, 0]
        tempo_newton = float('inf')
        precisao_final_newton = float('inf')

    # ANÁLISE DE EFICIÊNCIA MELHORADA
    print("\n" + "=" * 100)
    print("                           ANÁLISE DE EFICIÊNCIA E COMPARAÇÃO DE MÉTODOS")
    print("=" * 100)
    
    # Coletar dados dos métodos que convergiram (método, iterações, raiz, tempo, precisão)
    metodos_data = []
    
    if resultado_biss[0] != -1:
        metodos_data.append(("Bissecção", resultado_biss[0] + 1, resultado_biss[1], tempo_biss, precisao_final))
    
    if resultado_fp[0] != -1:
        metodos_data.append(("Falsa Posição", resultado_fp[0] + 1, resultado_fp[1], tempo_fp, precisao_final_fp))
    
    if resultado_sc[0] != -1:
        metodos_data.append(("Secante", resultado_sc[0] + 1, resultado_sc[1], tempo_sc, precisao_final_sc))
    
    if resultado_newton[0] != -1:
        metodos_data.append(("Newton-Raphson", resultado_newton[0] + 1, resultado_newton[1], tempo_newton, precisao_final_newton))
    
    # Verificar se algum método convergiu
    if not metodos_data:
        print("[ERRO] NENHUM METODO CONVERGIU!")
        return
    
    # Ordenar por número de iterações (menor = mais eficiente)
    metodos_data.sort(key=lambda x: x[1])
    
    # Exibir tabela de resultados completa
    print("\nTABELA COMPARATIVA COMPLETA DE RESULTADOS:")
    print("-" * 100)
    print(f"{'Posicao':<10} {'Metodo':<18} {'Iteracoes':<12} {'Tempo (ms)':<15} {'Raiz':<18} {'|f(raiz)|':<15}")
    print("-" * 100)
    
    for i, (metodo, iter_count, raiz, tempo, precisao_f) in enumerate(metodos_data, 1):
        if i == 1:
            simbolo = "[1o]"  # Ouro
        elif i == 2:
            simbolo = "[2o]"  # Prata
        elif i == 3:
            simbolo = "[3o]"  # Bronze
        else:
            simbolo = f"[{i}o]"  # Menção honrosa
            
        print(f"{simbolo}       {metodo:<18} {iter_count:<12} {tempo:<15.6f} {raiz:<18.10f} {precisao_f:<15.2e}")
    
    print("-" * 100)
    
    # Análise detalhada
    print(f"\n[MELHOR] METODO MAIS EFICIENTE: {metodos_data[0][0].upper()}")
    print(f"   - Convergiu em apenas {metodos_data[0][1]} iteracoes")
    print(f"   - Tempo de execucao: {metodos_data[0][3]:.6f} ms")
    print(f"   - Raiz encontrada: {metodos_data[0][2]:.10f}")
    print(f"   - Precisao final |f(raiz)|: {metodos_data[0][4]:.2e}")
    
    # Comparações detalhadas
    if len(metodos_data) > 1:
        print(f"\nCOMPARACOES:")
        melhor_metodo = metodos_data[0]
        
        for i in range(1, len(metodos_data)):
            metodo_atual = metodos_data[i]
            diferenca = metodo_atual[1] - melhor_metodo[1]
            if melhor_metodo[1] > 0:
                percentual = ((metodo_atual[1] - melhor_metodo[1]) / melhor_metodo[1]) * 100
                print(f"   - {melhor_metodo[0]} foi {diferenca} iteracoes mais rapido que {metodo_atual[0]}")
                print(f"     (Reducao de {percentual:.1f}% nas iteracoes)")
    
    # Estatísticas gerais
    total_iter = sum(data[1] for data in metodos_data)
    media_iter = total_iter / len(metodos_data)
    total_tempo = sum(data[3] for data in metodos_data)
    media_tempo = total_tempo / len(metodos_data)
    
    print(f"\nESTATISTICAS GERAIS:")
    print(f"   - Total de metodos que convergiram: {len(metodos_data)}")
    print(f"   - Media de iteracoes: {media_iter:.1f}")
    print(f"   - Media de tempo de execucao: {media_tempo:.6f} ms")
    print(f"   - Melhor performance (iteracoes): {metodos_data[0][1]} iteracoes")
    print(f"   - Pior performance (iteracoes): {metodos_data[-1][1]} iteracoes")
    
    # Análise por tempo de execução
    metodos_por_tempo = sorted(metodos_data, key=lambda x: x[3])
    print(f"   - Metodo mais rapido: {metodos_por_tempo[0][0]} ({metodos_por_tempo[0][3]:.6f} ms)")
    print(f"   - Metodo mais lento: {metodos_por_tempo[-1][0]} ({metodos_por_tempo[-1][3]:.6f} ms)")
    
    # Análise por eficiência relativa
    if len(metodos_data) > 1:
        print(f"\nEFICIENCIA RELATIVA:")
        base_iter = metodos_data[0][1]  # Melhor método como base
        
        for metodo, iter_count, raiz, tempo, precisao_f in metodos_data:
            if iter_count == base_iter:
                eficiencia = 100.0
                status = "[MAXIMA]"
            else:
                eficiencia = (base_iter / iter_count) * 100
                if eficiencia >= 80:
                    status = "[ALTA]"
                elif eficiencia >= 60:
                    status = "[MEDIA]"
                else:
                    status = "[BAIXA]"
            
            print(f"   - {metodo:<16}: {eficiencia:6.1f}% {status}")
    
    # Análise específica dos métodos
    print(f"\nANALISE ESPECIFICA DOS METODOS:")
    print(f"   - Bisseccao: Metodo robusto, sempre converge se ha mudanca de sinal")
    print(f"   - Falsa Posicao: Melhora a bisseccao usando interpolacao linear")
    print(f"   - Secante: Aproxima a derivada numericamente")
    print(f"   - Newton-Raphson: Convergencia quadratica quando proximo da raiz")