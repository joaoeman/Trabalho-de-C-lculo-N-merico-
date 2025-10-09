# Trabalho de Cálculo Numérico - Zeros de Funções

**Disciplina:** Cálculo Numérico  
**Instituição:** Fundação Universidade Federal do Vale do São Francisco  
**Período:** 2025.2

---

## 📋 Descrição do Projeto

Este projeto implementa e compara quatro métodos numéricos iterativos para encontrar zeros de funções:

1. **Método da Bissecção**
2. **Método da Falsa Posição (Regula Falsi)**
3. **Método da Secante**
4. **Método de Newton-Raphson**

O objetivo é analisar e comparar a eficiência e velocidade de convergência de cada método em problemas práticos de engenharia.

---

## 🎯 Funcionalidades

- ✅ Implementação dos 4 métodos numéricos principais
- ✅ Entrada de dados manual ou por arquivo
- ✅ Medição de tempo de execução (em milissegundos)
- ✅ Cálculo da precisão final alcançada |f(raiz)|
- ✅ Tabela comparativa completa de resultados
- ✅ Análise estatística de desempenho
- ✅ Menu interativo para múltiplas execuções
- ✅ Exemplos de problemas de engenharia
- ✅ Documentação completa do código

---

## 🚀 Como Executar

### Pré-requisitos

```bash
python >= 3.8
sympy
```

### Instalação de Dependências

```bash
pip install sympy
```

### Execução do Programa

```bash
python main.py
```

---

## 📂 Estrutura do Projeto

```
.
├── main.py                     # Programa principal com menu interativo
├── testarMetodos.py           # Módulo de testes e comparação
├── metodos/                   # Pasta com implementação dos métodos
│   ├── __init__.py
│   ├── bisseccao.py          # Método da Bissecção
│   ├── falsaPosicao.py       # Método da Falsa Posição
│   ├── secante.py            # Método da Secante
│   └── newton.py             # Método de Newton-Raphson
├── input.txt                  # Exemplo 1: x² - 4
├── input2.txt                 # Exemplo do trabalho: x³ - 5x² + 8x - 4
├── problema_bacterias.txt     # Problema 1: Concentração de bactérias
├── problema_deslocamento.txt  # Problema 2: Deslocamento de estruturas
└── README.md                  # Este arquivo
```

---

## 📝 Formato dos Arquivos de Entrada

Os arquivos de entrada devem conter 7 linhas:

```
<função em x>
<início do intervalo a>
<fim do intervalo b>
<primeira estimativa x0>
<segunda estimativa x1>
<precisão desejada>
<máximo de iterações>
```

### Exemplo (input.txt):

```
x**2 - 4
1
3
1.5
2.5
0.000001
100
```

---

## 🔬 Problemas de Engenharia Implementados

### Exemplo do Trabalho: Acelerador de Partículas
**Função:** f(x) = x³ - 5x² + 8x - 4  
**Problema:** Determinar para qual valor de x o campo magnético se anula no acelerador de partículas da Suíça.  
**Arquivo:** `input2.txt`

### Problema 1: Concentração de Bactérias
**Função:** C(t) = 80e^(-2t) + 20e^(-0.1t) - 10  
**Problema:** Determinar o tempo necessário para reduzir a concentração da bactéria poluente a 10.  
**Arquivo:** `problema_bacterias.txt`

### Problema 2: Deslocamento de Estruturas
**Função:** y(t) = 10e^(-0.5t)cos(2t) - 5  
**Problema:** Determinar o tempo para que o deslocamento horizontal de um prédio chegue a 5.  
**Arquivo:** `problema_deslocamento.txt`

---

## 📊 Saída do Programa

O programa gera uma análise completa contendo:

1. **Resultados Individuais de Cada Método:**
   - Raiz encontrada
   - Número de iterações
   - Tempo de execução (ms)
   - Precisão final |f(raiz)|

2. **Tabela Comparativa:**
   - Ranking dos métodos por eficiência
   - Comparação de iterações, tempo e precisão

3. **Análise Estatística:**
   - Média de iterações e tempo
   - Melhor e pior performance
   - Eficiência relativa dos métodos

---

## 🔍 Métodos Implementados

### 1. Método da Bissecção
- **Tipo:** Método de intervalo
- **Convergência:** Linear
- **Vantagens:** Sempre converge, robusto
- **Desvantagens:** Convergência lenta
- **Requisitos:** Mudança de sinal no intervalo

### 2. Método da Falsa Posição
- **Tipo:** Método de intervalo com interpolação
- **Convergência:** Superlinear
- **Vantagens:** Geralmente mais rápido que bissecção
- **Desvantagens:** Pode convergir lentamente em funções muito curvas
- **Requisitos:** Mudança de sinal no intervalo

### 3. Método da Secante
- **Tipo:** Método aberto
- **Convergência:** Superlinear (~1.618)
- **Vantagens:** Não requer derivada, rápido
- **Desvantagens:** Pode divergir, requer 2 estimativas iniciais
- **Requisitos:** Duas estimativas iniciais próximas da raiz

### 4. Método de Newton-Raphson
- **Tipo:** Método aberto
- **Convergência:** Quadrática
- **Vantagens:** Convergência muito rápida
- **Desvantagens:** Requer derivada, pode divergir
- **Requisitos:** Estimativa inicial e derivada da função

---

## 💡 Uso do Menu Interativo

```
MENU PRINCIPAL:
   1. Entrada manual de dados
   2. Ler dados de arquivo (input.txt)
   3. Ler dados de arquivo (input2.txt)
   4. Ler dados de arquivo personalizado
   5. Exemplos de problemas de engenharia
   0. Sair
```

---

## 🧪 Exemplos de Uso

### Entrada Manual
```python
python main.py
# Escolha opção 1
# Digite: x**2 - 4
# Intervalo: 1 a 3
# Estimativas: 1.5 e 2.5
# Precisão: 0.000001
# Iterações: 100
```

### Leitura de Arquivo
```python
python main.py
# Escolha opção 2 (para input.txt)
# ou opção 3 (para input2.txt)
```

### Problemas de Engenharia
```python
python main.py
# Escolha opção 5
# Selecione o problema desejado
```

---

## 📈 Critérios de Parada

Todos os métodos param quando:
1. **Precisão da função:** |f(x)| < ε
2. **Precisão da variável:** |x_{n+1} - x_n| < ε
3. **Máximo de iterações:** n ≥ n_max

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x:** Linguagem de programação
- **SymPy:** Biblioteca para matemática simbólica
- **time:** Medição de tempo de execução

---

## 🎓 Equipe

- David Rios Santana
- Guilherme Emetério Santos Lima
- João Emanuel Santos Do Nascimento

---

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais como parte da disciplina de Cálculo Numérico.
