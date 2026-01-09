Hero Jump

Hero Jump é um jogo de plataforma 2D desenvolvido com Pygame Zero, onde o jogador controla um herói que deve correr, pular e evitar inimigos para alcançar o objetivo final. É um projeto educativo e divertido que explora conceitos de programação de jogos, animação de sprites e interação com o usuário.

🎮 Gameplay

Controle um herói que corre e pula por plataformas.

Evite inimigos que se movem de um lado para o outro.

Alcance o objetivo final para vencer o jogo.

O herói possui vidas, representadas por corações na tela.

O jogo possui música de fundo e efeitos sonoros de salto e colisão.

Existe um menu inicial com opções para iniciar o jogo, ligar/desligar som e sair.

⬇️ Controles

Seta Esquerda: mover para a esquerda

Seta Direita: mover para a direita

Espaço: pular

Mouse: clicar nos botões do menu

🛠 Recursos

Animação de sprites para o herói e inimigos

Sistema de física simples: gravidade e colisão com plataformas

Sistema de vidas

Música de fundo e efeitos sonoros

Menu interativo com botões para iniciar, som e sair

📂 Estrutura do projeto
HeroJump/
│
├── images/           # Sprites do herói, inimigos, plataforma, coração, botões e fundo
│   ├── hero_idle_0.png
│   ├── hero_run_0.png
│   ├── hero_run_1.png
│   ├── enemy_idle_0.png
│   ├── enemy_run_0.png
│   └── ...
│
├── sounds/           # Sons do jogo
│   ├── musica_aventura.wav
│   ├── jump.wav
│   └── hit.wav
│
├── game.py           # Código principal do jogo
└── README.md         # Este arquivo

⚡ Como rodar

Certifique-se de ter o Python 3 instalado.

Instale o Pygame Zero:

pip install pgzero


Abra o terminal na pasta do projeto e rode:

pgzrun game.py


O jogo iniciará com o menu principal, onde você poderá iniciar o jogo e controlar o som.

📝 Observações

O som de música de fundo deve estar na pasta sounds para funcionar corretamente.

Os efeitos de salto e colisão podem ter volume ajustado no código.
O jogo é projetado para aprendizado e pode ser expandido com novos inimigos, fases e power-ups.
