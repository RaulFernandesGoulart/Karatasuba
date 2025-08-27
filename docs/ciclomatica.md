# Análise da Complexidade Ciclomática

A **complexidade ciclomática** é uma métrica introduzida por Thomas McCabe em 1976, utilizada para medir a complexidade lógica de um programa.  
Ela é baseada no número de caminhos linearmente independentes em um fluxo de controle e ajuda a determinar a quantidade mínima de casos de teste necessária para garantir a cobertura completa.

---

## Fórmula

A fórmula da complexidade ciclomática é:

\[
M = E - N + 2P
\]

Onde:  
- **E** = número de **arestas** no grafo de fluxo  
- **N** = número de **nós** no grafo de fluxo  
- **P** = número de componentes conexos (em um único programa, normalmente `P = 1`)

---

## Aplicação no Algoritmo de Karatsuba

### 1. Fluxo de Controle da função `karatsuba`

1. Início  
2. Cálculo do sinal  
3. Decisão D0 → `x == 0 or y == 0`  
   - Sim → Retorna 0  
   - Não → segue para D1  
4. Decisão D1 → `x < 10 or y < 10`  
   - Sim → Retorna `x * y`  
   - Não → executa recursão (split, cálculo de z0, z1, z2, recombinação)  
5. Retorna resultado final  
6. Fim

---

### 2. Estrutura do Grafo de Fluxo

- **Nós (N):** 8  
  - Entrada (Start)  
  - Decisão D0  
  - Retorno 0  
  - Decisão D1  
  - Retorno do caso base  
  - Bloco recursivo (divisão + chamadas z0, z1, z2)  
  - Retorno final  
  - Saída (End)  

- **Arestas (E):** 9  
  - Start → D0  
  - D0 (Sim) → Retorna 0  
  - Retorna 0 → End  
  - D0 (Não) → D1  
  - D1 (Sim) → Retorna caso base  
  - Retorna caso base → End  
  - D1 (Não) → Recursão  
  - Recursão → Retorno final  
  - Retorno final → End  

- **Componentes conexos (P):** 1  

---

### 3. Cálculo

\[
M = E - N + 2P
\]

\[
M = 9 - 8 + 2(1)
\]

\[
M = 3
\]

---

## Interpretação

O valor **M = 3** indica que existem **3 caminhos linearmente independentes** no código:

1. Caminho em que `x == 0 or y == 0` → retorna 0.  
2. Caminho em que `x < 10 or y < 10` → retorna multiplicação direta.  
3. Caminho recursivo → divide, calcula z0/z1/z2 e retorna resultado.  

---

## Conclusão

- A função `karatsuba` possui **complexidade ciclomática igual a 3**.  
- Isso significa que **no mínimo 3 casos de teste distintos** são necessários para cobrir todos os fluxos de execução do código.  
- Essa métrica auxilia na avaliação da **manutenibilidade** e na definição de uma **estratégia de testes** eficaz.
