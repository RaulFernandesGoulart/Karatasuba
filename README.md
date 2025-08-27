# Projeto Karatsuba

O **Karatsuba** é um projeto desenvolvido para implementar e analisar o **algoritmo de Karatsuba**, um método eficiente para a multiplicação de inteiros grandes. Este projeto foi desenvolvido como atividade prática da disciplina **Fundamentos de Projeto e Análise de Algoritmos**.

---

## Descrição do Projeto

O algoritmo de Karatsuba foi proposto em 1960 por Anatolii Karatsuba e foi o primeiro a superar a complexidade quadrática da multiplicação tradicional.  
Enquanto a multiplicação escolar exige `O(n²)` operações para números de `n` dígitos, o Karatsuba reduz esse custo para `O(n^log₂3) ≈ O(n^1.585)`.

### Implementação (linha a linha)

O código está no arquivo **`main.py`** e funciona da seguinte forma:

1. **Função `karatsuba(x, y)`**  
   - Calcula o sinal do resultado (positivo/negativo).  
   - Trata casos base:  
     - Se um dos números é **0**, retorna 0.  
     - Se algum número tem apenas **1 dígito**, retorna a multiplicação direta.  
   - Divide os números ao meio em **parte alta** e **parte baixa**.  
   - Calcula três produtos recursivos:  
     - `z0 = karatsuba(x_low, y_low)`  
     - `z2 = karatsuba(x_high, y_high)`  
     - `z1 = karatsuba(x_low + x_high, y_low + y_high) - z0 - z2`  
   - Recombina o resultado final:  
     ```
     res = (z2 * 10^(2m)) + (z1 * 10^m) + z0
     ```
   - Retorna `sign * res`.

2. **Função `_cli()`**  
   - Permite rodar o programa via linha de comando.  
   - Se o usuário passar dois números como argumentos → calcula direto.  
   - Caso contrário, pede os valores via `input()` e mostra o resultado.

---

## Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/karatsuba.git
cd karatsuba

Criar e ativar ambiente virtual

python -m venv .venv

Instalar dependências

pip install pytest

Executar o programa

python main.py
