# Geração do Triângulo de Sierpiński via Autômato Celular 1D

Este projeto contém um script em Python que implementa um autômato celular unidimensional (1D) para gerar o famoso fractal conhecido como Triângulo de Sierpiński. Este é um exemplo clássico de como regras locais muito simples podem levar à emergência de comportamentos globais complexos e ordenados.

O modelo é baseado no documento "Cellular Automata: A Discrete View of the World"  e serve como uma demonstração prática de complexidade emergente.

## Como Funciona

O autômato opera em uma grade 1D de células, onde cada célula pode estar em um de dois estados: 0 (inativa) ou 1 (ativa). A simulação começa com uma única célula ativa no centro.

A cada passo de tempo (geração), o estado de cada célula é atualizado com base nos estados de seus vizinhos imediatos (esquerda, centro, direita) na geração anterior. A regra de atualização utilizada é a **Regra 90**, que define o novo estado de uma célula como a soma (módulo 2) dos estados de seus vizinhos esquerdo e direito.

$S_i^{t+1} = (S_{i-1}^t + S_{i+1}^t) \pmod 2$

A evolução do sistema ao longo do tempo, quando visualizada em 2D, revela o padrão do Triângulo de Sierpiński.

## Requisitos

* Python 3.x
* NumPy
* Matplotlib

## Instalação

1.  Clone este repositório;

2.  Instale as dependências:
    ```bash
    pip install numpy matplotlib
    ```

## Uso

Para executar a simulação e visualizar o resultado, basta rodar o script principal:

```bash
python sierpinski_ca.py
