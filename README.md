# Angry Birds em Python

Este projeto é uma versão simples de um jogo tipo Angry Birds feita com Python, usando as bibliotecas `pygame` e `pymunk`.

## Como funciona

O jogo cria uma janela com tamanho de 800x600 pixels e um mundo físico simulado por `pymunk`.

### 1. Inicialização

O código inicia o Pygame, cria a tela e define o relógio do jogo para controlar a taxa de quadros por segundo:

- `pygame.init()` ativa os módulos do jogo
- `screen = pygame.display.set_mode((WIDTH, HEIGHT))` cria a janela
- `clock = pygame.time.Clock()` controla o FPS

### 2. Carregamento de assets

As imagens do pássaro e dos blocos são carregadas da pasta `assets`:

- `bird.png`
- `pig.png`

Essas imagens são redimensionadas para caber no jogo e recebem transparência com `convert_alpha()`.

### 3. Física do mundo

O jogo usa `pymunk.Space()` para criar o ambiente físico:

- `space.gravity = (0, 900)` faz tudo cair para baixo
- um segmento no chão é criado para representar o solo
- blocos são criados em posições fixas e recebem massa, atrito e elasticidade

Isso permite que os objetos caiam, se movam e colidam entre si em um cenário físico realista.

### 4. Lançamento do projétil

A função `launch_projectile(pos, impulse)` cria um corpo circular que representa o pássaro ou projétil. Ele recebe:

- posição inicial
- impulso calculado com base no arrasto do mouse

Ao soltar o clique, o código calcula a diferença entre a origem do lançamento e a posição atual do mouse, aplica esse valor como força e dispara o objeto.

### 5. Interação com o mouse

O jogador arrasta o mouse em direção oposta ao ponto de lançamento:

- se o mouse estiver perto do ponto inicial, o jogo entra no modo de arrasto
- ao soltar o botão, o pássaro é lançado
- uma linha de mira aparece para indicar a direção e a força do arremesso

### 6. Atualização da cena

No loop principal do jogo:

- o evento de fechar a janela é tratado
- a física é atualizada com `space.step(1.0 / 60.0)`
- a tela é preenchida e redesenhada
- os blocos e os projéteis são desenhados na posição correta
- o jogo atualiza a tela em 60 FPS

### 7. Objetivo da mecânica

A ideia do jogo é simples:

- posicionar o pássaro na origem do lançamento
- arrastar para definir a força
- lançar contra os blocos
- observar como a física reage ao impacto

Esse código funciona como uma base para jogos de física 2D e pode ser expandido com:

- pontuação
- colisão com múltiplos alvos
- reinício do nível
- mais tipos de blocos
- som e efeitos visuais

## Tecnologias usadas

- Python
- Pygame
- Pymunk

## Como executar

No diretório do projeto, rode:

```bash
python game.py
```

Se o ambiente tiver dependências instaladas corretamente, a janela do jogo será aberta.

## Observação

Este é um projeto educativo e simples, voltado para aprender física em jogos 2D e também o uso básico de renderização gráfica com Pygame.
