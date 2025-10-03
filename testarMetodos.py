import sympy as sp
import metodos.bisseccao
import metodos.falsaPosicao
import metodos.secante
import metodos.newton

x = sp.Symbol('x')

def tests(a:float, b: float, x0: float, x1: float, func: sp.Expr, precisao: float, iteracoes: int):
    # Calcular a derivada da função para Newton-Raphson
    derivada = sp.diff(func, x)
    
    # Método da Bissecção
    print("\n1. MÉTODO DA BISSECÇÃO")
    print("-" * 30)
    resultado_biss = metodos.bisseccao.bisseccao(a, b, iteracoes, func, precisao)
    print(f"Resultado: {resultado_biss}")
    if resultado_biss[0] != -1:
        print(f"✅ Raiz encontrada: {resultado_biss[1]:.8f}")
        print(f"📊 Iterações: {resultado_biss[0] + 1}")
        
        # Verificação
        verificacao = func.subs(x, resultado_biss[1])
        print(f"🔍 Verificação f({resultado_biss[1]:.8f}) = {float(verificacao):.2e}")
    else:
        print("❌ Raiz não encontrada no número máximo de iterações")
    
    # Método da Falsa Posição
    print("\n2. MÉTODO DA FALSA POSIÇÃO")
    print("-" * 30)
    resultado_fp = metodos.falsaPosicao.falsaPosicao(a, b, func, precisao, iteracoes)
    print(f"Resultado: {resultado_fp}")
    if resultado_fp[0] != -1:
        print(f"✅ Raiz encontrada: {resultado_fp[1]:.8f}")
        print(f"📊 Iterações: {resultado_fp[0] + 1}")
        
        # Verificação
        verificacao = func.subs(x, resultado_fp[1])
        print(f"🔍 Verificação f({resultado_fp[1]:.8f}) = {float(verificacao):.2e}")
    else:
        print("❌ Raiz não encontrada no número máximo de iterações")
    
    # Método da Secante
    print("\n3. MÉTODO DA SECANTE")
    print("-" * 30)
    try:
        resultado_sc = metodos.secante.secante(x0, x1, func, precisao, iteracoes)
        print(f"Resultado: {resultado_sc}")
        if resultado_sc[0] != -1:
            print(f"✅ Raiz encontrada: {resultado_sc[1]:.8f}")
            print(f"📊 Iterações: {resultado_sc[0] + 1}")
            
            # Verificação
            verificacao = func.subs(x, resultado_sc[1])
            print(f"🔍 Verificação f({resultado_sc[1]:.8f}) = {float(verificacao):.2e}")
        else:
            print("❌ Raiz não encontrada no número máximo de iterações")
    except Exception as e:
        print(f"❌ Erro no método da secante: {e}")
        resultado_sc = [-1, 0]

    # Método de Newton-Raphson
    print("\n4. MÉTODO DE NEWTON-RAPHSON")
    print("-" * 30)
    print(f"Derivada: f'(x) = {derivada}")
    try:
        resultado_newton = metodos.newton.newton(x0, func, derivada, precisao, iteracoes)
        print(f"Resultado: {resultado_newton}")
        if resultado_newton[0] != -1:
            print(f"✅ Raiz encontrada: {resultado_newton[1]:.8f}")
            print(f"📊 Iterações: {resultado_newton[0] + 1}")
            
            # Verificação
            verificacao = func.subs(x, resultado_newton[1])
            print(f"🔍 Verificação f({resultado_newton[1]:.8f}) = {float(verificacao):.2e}")
            
            # Verificação da derivada no ponto
            verificacao_deriv = derivada.subs(x, resultado_newton[1])
            print(f"📈 f'({resultado_newton[1]:.8f}) = {float(verificacao_deriv):.2e}")
        else:
            print("❌ Raiz não encontrada no número máximo de iterações")
    except Exception as e:
        print(f"❌ Erro no método de Newton-Raphson: {e}")
        resultado_newton = [-1, 0]

    # ANÁLISE DE EFICIÊNCIA MELHORADA
    print("\n" + "=" * 60)
    print("                ANÁLISE DE EFICIÊNCIA")
    print("=" * 60)
    
    # Coletar dados dos métodos que convergiram
    metodos_data = []
    
    if resultado_biss[0] != -1:
        metodos_data.append(("Bissecção", resultado_biss[0] + 1, resultado_biss[1]))
    
    if resultado_fp[0] != -1:
        metodos_data.append(("Falsa Posição", resultado_fp[0] + 1, resultado_fp[1]))
    
    if resultado_sc[0] != -1:
        metodos_data.append(("Secante", resultado_sc[0] + 1, resultado_sc[1]))
    
    if resultado_newton[0] != -1:
        metodos_data.append(("Newton-Raphson", resultado_newton[0] + 1, resultado_newton[1]))
    
    # Verificar se algum método convergiu
    if not metodos_data:
        print("❌ NENHUM MÉTODO CONVERGIU!")
        return
    
    # Ordenar por número de iterações (menor = mais eficiente)
    metodos_data.sort(key=lambda x: x[1])
    
    # Exibir tabela de resultados
    print("\n📊 TABELA DE RESULTADOS:")
    print("-" * 70)
    print(f"{'Posição':<8} {'Método':<16} {'Iterações':<12} {'Raiz':<15}")
    print("-" * 70)
    
    for i, (metodo, iter_count, raiz) in enumerate(metodos_data, 1):
        if i == 1:
            emoji = "🥇"  # Ouro
        elif i == 2:
            emoji = "🥈"  # Prata
        elif i == 3:
            emoji = "🥉"  # Bronze
        else:
            emoji = "🏅"  # Menção honrosa
            
        print(f"{emoji} {i}º     {metodo:<16} {iter_count:<12} {raiz:<15.8f}")
    
    print("-" * 70)
    
    # Análise detalhada
    print(f"\n🏆 MÉTODO MAIS EFICIENTE: {metodos_data[0][0].upper()}")
    print(f"   • Convergiu em apenas {metodos_data[0][1]} iterações")
    print(f"   • Raiz encontrada: {metodos_data[0][2]:.8f}")
    
    # Comparações detalhadas
    if len(metodos_data) > 1:
        print(f"\n📈 COMPARAÇÕES:")
        melhor_metodo = metodos_data[0]
        
        for i in range(1, len(metodos_data)):
            metodo_atual = metodos_data[i]
            diferenca = metodo_atual[1] - melhor_metodo[1]
            if melhor_metodo[1] > 0:
                percentual = ((metodo_atual[1] - melhor_metodo[1]) / melhor_metodo[1]) * 100
                print(f"   • {melhor_metodo[0]} foi {diferenca} iterações mais rápido que {metodo_atual[0]}")
                print(f"     (Redução de {percentual:.1f}% nas iterações)")
    
    # Estatísticas gerais
    total_iter = sum(data[1] for data in metodos_data)
    media_iter = total_iter / len(metodos_data)
    
    print(f"\n📊 ESTATÍSTICAS GERAIS:")
    print(f"   • Total de métodos que convergiram: {len(metodos_data)}")
    print(f"   • Média de iterações: {media_iter:.1f}")
    print(f"   • Melhor performance: {metodos_data[0][1]} iterações")
    print(f"   • Pior performance: {metodos_data[-1][1]} iterações")
    
    # Análise por eficiência relativa
    if len(metodos_data) > 1:
        print(f"\n⚡ EFICIÊNCIA RELATIVA:")
        base_iter = metodos_data[0][1]  # Melhor método como base
        
        for metodo, iter_count, _ in metodos_data:
            if iter_count == base_iter:
                eficiencia = 100.0
                status = "🔥 MÁXIMA"
            else:
                eficiencia = (base_iter / iter_count) * 100
                if eficiencia >= 80:
                    status = "✅ ALTA"
                elif eficiencia >= 60:
                    status = "⚠️  MÉDIA"
                else:
                    status = "❌ BAIXA"
            
            print(f"   • {metodo:<16}: {eficiencia:6.1f}% {status}")
    
    # Análise específica dos métodos
    print(f"\n🔬 ANÁLISE ESPECÍFICA DOS MÉTODOS:")
    print(f"   • Bissecção: Método robusto, sempre converge se há mudança de sinal")
    print(f"   • Falsa Posição: Melhora a bissecção usando interpolação linear")
    print(f"   • Secante: Aproxima a derivada numericamente")
    print(f"   • Newton-Raphson: Convergência quadrática quando próximo da raiz")