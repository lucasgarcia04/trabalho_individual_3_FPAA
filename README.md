# Caminho Hamiltoniano  
**Fundamentos de Projeto e Análise de Algoritmos — Engenharia de Software (5º período)**  
**Professor: João Paulo Carneiro Aramuni**
**Aluno: Lucas Ferreira Garcia**

---

## Descrição do Projeto

Este projeto tem como objetivo implementar um algoritmo em Python que determina a existência de um Caminho Hamiltoniano em um grafo. Um Caminho Hamiltoniano é um caminho que visita cada vértice do grafo exatamente uma vez, e esse é um problema clássico em Teoria dos Grafos e da Complexidade Computacional.

A abordagem utilizada é baseada em backtracking, uma técnica de busca que testa todas as possibilidades de caminhos até encontrar uma solução válida.

---

## Estrutura do Projeto

├── assets
│   └── grafo.png           # Imagem do grafo com Caminho Hamiltoniano destacado
├── main.py              # Implementação do algoritmo de Caminho Hamiltoniano
├── test.py              # Testes automatizados para o algoritmo
├── view.py              # Visualização do grafo com NetworkX e Matplotlib
├── requirements.txt     # Dependências do projeto
└── README.md            # Documentação do projeto e relatório técnico

---

## Como executar o projeto

### Requisitos
- Projeto realizado na versão do Python 3.13.2

### 1. Clone o repositório

```bash
git clone https://github.com/lucasgarcia04/trabalho_individual_3_FPAA.git
cd trabalho_individual_3_FPAA
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Execute o visualizador gráfico

```bash
python view.py
```

### 4. Execute os testes

```bash
python test.py
```

---

## Explicação do algoritmo linha a linha (`main.py`)

```python
def hamiltonian_path(graph):
    n = len(graph)
    path = []

    def backtrack(v, visited):
        path.append(v)
        if len(path) == n:
            return True
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                if backtrack(u, visited):
                    return True
                visited[u] = False
        path.pop()
        return False

    for start in range(n):
        visited = [False] * n
        visited[start] = True
        path.clear()
        if backtrack(start, visited):
            return path
    return None
```

### Análise linha por linha:

1. **Definição da Função:**
   ```python
   def hamiltonian_path(graph):
   ```
   - Define a função principal que tenta encontrar um Caminho Hamiltoniano em `graph`.

2. **Número de vértices e caminho inicial:**
   ```python
   n = len(graph)
   path = []
   ```
   - `n` armazena o número de vértices do grafo.
   - `path` é a lista que vai armazenar o caminho atual.

3. **Função recursiva de backtracking:**
   ```python
   def backtrack(v, visited):
   ```
   - Define uma função interna para percorrer o grafo recursivamente.

4. **Adiciona o vértice atual ao caminho:**
   ```python
   path.append(v)
   ```
   - Adiciona o vértice `v` ao caminho atual.

5. **Verifica se todos os vértices foram visitados:**
   ```python
   if len(path) == n:
       return True
   ```
   - Se o comprimento do caminho for igual ao número de vértices, encontramos um Caminho Hamiltoniano.

6. **Itera sobre os vizinhos:**
   ```python
   for u in graph[v]:
   ```
   - Para cada vizinho `u` do vértice atual `v`.

7. **Verifica se o vizinho ainda não foi visitado:**
   ```python
   if not visited[u]:
   ```
   - Garante que cada vértice seja visitado no máximo uma vez.

8. **Marca o vizinho como visitado e continua a busca:**
   ```python
   visited[u] = True
   if backtrack(u, visited):
       return True
   ```
   - Marca `u` como visitado e chama `backtrack` recursivamente.

9. **Desfaz a marcação (backtracking):**
   ```python
   visited[u] = False
   ```
   - Se o caminho a partir de `u` não funcionar, desfaz a visita.

10. **Remove o último vértice (volta atrás):**
    ```python
    path.pop()
    ```
    - Remove o último vértice adicionado, voltando ao estado anterior.

11. **Tenta iniciar o caminho a partir de cada vértice:**
    ```python
    for start in range(n):
    ```
    - Tenta iniciar o caminho por todos os vértices possíveis.

12. **Inicializa os visitados e chama o backtrack:**
    ```python
    visited = [False] * n
    visited[start] = True
    path.clear()
    if backtrack(start, visited):
        return path
    ```

13. **Se nenhum caminho for encontrado:**
    ```python
    return None
    ```
    - Retorna `None` se nenhum Caminho Hamiltoniano for encontrado.

---

## Relatório Técnico

### Classes de Complexidade

#### Qual a classe do problema?

O **Caminho Hamiltoniano** pertence à classe **NP-Completo**, pois:

- Está em **NP**: dado um caminho, é possível verificar em tempo polinomial se ele é Hamiltoniano.
- É **NP-Difícil**, porque qualquer problema da classe NP pode ser reduzido a ele em tempo polinomial.

#### Relação com o Caixeiro Viajante:

O **Problema do Caixeiro Viajante (TSP)** é uma variação do Caminho Hamiltoniano com peso nas arestas e objetivo de minimizar o custo — ou seja, o TSP é ainda mais difícil (NP-Difícil na versão de otimização).

---

### ⏱Análise da Complexidade Assintótica

#### Complexidade Temporal:
- **Pior caso:** `O(n!)`  
  - O algoritmo tenta todas as permutações possíveis de vértices.
  - Essa análise foi feita por expansão de recorrência, pois:

```
T(n) = (n - 1) * T(n - 1) → O(n!)
```

#### Método utilizado:
- Utilizei a técnica de **expansão de recorrência**, já que o algoritmo reduz o problema em `n - 1` a cada chamada.

---

### Aplicação do Teorema Mestre

#### O Teorema Mestre **não se aplica** aqui

##### Por quê?

- A fórmula do Teorema Mestre exige:
  ```
  T(n) = a * T(n/b) + f(n)
  ```
- Mas no nosso caso temos:
  ```
  T(n) = (n - 1) * T(n - 1) + O(1)
  ```
- Ou seja, o problema é reduzido de forma linear, não fracionária. Portanto, utilizamos expansão de recorrência.

---

### 📈 Análise dos Casos de Complexidade

| Caso        | Descrição                                                              | Complexidade | Impacto             |
|-------------|------------------------------------------------------------------------|--------------|----------------------|
| **Melhor**  | O caminho é encontrado na primeira tentativa                          | O(n)         | Muito eficiente      |
| **Médio**   | Algumas tentativas antes de encontrar o caminho válido                | O(k * n)     | Tolerável em grafos pequenos |
| **Pior**    | Todas as permutações são tentadas e nenhuma solução é encontrada      | O(n!)        | Muito lento          |

---

## Visualização do Caminho Hamiltoniano

O arquivo `view.py` utiliza:

- `networkx` para construir e desenhar o grafo
- `matplotlib` para exibir o grafo
- As arestas do **Caminho Hamiltoniano** são destacadas em **vermelho**

---

## 📎 Referências

- PDF - Aula 02: Introdução à Teoria da Complexidade

---