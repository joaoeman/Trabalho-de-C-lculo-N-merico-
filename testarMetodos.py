import sympy as sp
import metodos.bisseccao
import metodos.falsaPosicao
import metodos.secante

x = sp.Symbol('x')

def tests(a:float, b: float, x0: float, x1: float, func: sp.Expr, precisao: float, iteracoes: int):
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
    
    # Metodo da secante
    print("\n3. MÉTODO DA SECANTE")
    print("-" * 30)
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

    # Comparação de eficiência
    if resultado_biss[0] != -1 and resultado_fp[0] != -1 and resultado_sc[0] != -1:
        print("\n" + "=" * 50)
        print("COMPARAÇÃO DE EFICIÊNCIA")
        print("=" * 50)
        print(f"Bissecção:     {resultado_biss[0] + 1:3d} iterações")
        print(f"Falsa Posição: {resultado_fp[0] + 1:3d} iterações")
        print(f"Secante: {resultado_sc[0] + 1:3d} iterações")