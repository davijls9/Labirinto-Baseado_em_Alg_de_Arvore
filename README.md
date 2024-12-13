# Labirinto com IA

Este projeto é um jogo de labirinto interativo onde o jogador pode controlar manualmente os movimentos ou permitir que uma Inteligência Artificial (IA) tente resolver o labirinto automaticamente. A IA utiliza algoritmos para explorar o labirinto e encontrar a saída, aprendendo com as decisões e descobertas feitas durante a exploração.

---

## Estrutura do Projeto

```
labirinto_projeto/
├── src/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── gerador_labirinto.py        # Lógica de geração do labirinto
│   │   ├── grafo.py                    # Criação e manipulação do grafo do labirinto
│   │   ├── jogo.py                     # Classe principal que gerencia o jogo
│   │   └── ia.py                       # Lógica da IA para movimentação
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── terminal_render.py          # Renderização e interação no terminal
│   │   └── gui_render.py               # (Opcional) Renderização com GUI (ex: pygame)
│   └── utils/
│       ├── __init__.py
│       ├── estado.py                   # Salvar e carregar estado
│       ├── comandos.py                 # Manipulação de comandos de entrada
│       └── logger.py                   # Configuração e gestão de logs
├── assets/
│   ├── config.json                     # Configurações do jogo (ex: tamanhos padrão)
│   ├── estado_exemplo.json             # Estado inicial de exemplo
│   └── comando_exemplo.json            # Comandos de exemplo para testes
├── tests/
│   ├── test_gerador_labirinto.py       # Testes para o gerador de labirinto
│   ├── test_grafo.py                   # Testes para o grafo
│   ├── test_ia.py                      # Testes para a IA
│   ├── test_estado.py                  # Testes para salvar/carregar estado
│   └── test_jogo.py                    # Testes para o fluxo principal
├── main.py                             # Arquivo principal para iniciar o jogo
├── requirements.txt                    # Dependências do projeto
├── README.md                           # Documentação do projeto
└── .gitignore
```

---

## Funcionalidades

- **Controle Manual**:
  - O jogador pode navegar pelo labirinto utilizando as teclas `W` (cima), `S` (baixo), `A` (esquerda), `D` (direita).
- **Controle Automático (IA)**:
  - A IA assume o controle e tenta resolver o labirinto sozinha.
- **Revisitação de Locais**:
  - Penalidades maiores para revisitar locais já explorados.
- **Customização**:
  - O jogador pode definir o tamanho do labirinto ao iniciar um novo jogo.
- **Sistema de Pontuação**:
  - Pontos são reduzidos a cada movimento, com penalidades adicionais para revisitação.

---

## Dependências

- Python 3.9+
- Bibliotecas:
  - `time`
  - `logging`
  - `heapq`
  - Outras especificadas em `requirements.txt`

Para instalar as dependências, use:
```bash
pip install -r requirements.txt
```

---

## Como Jogar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu_usuario/labirinto_projeto.git
   cd labirinto_projeto
   ```

2. Execute o jogo:
   ```bash
   python main.py
   ```

3. Escolha suas ações:
   - `W/A/S/D`: Movimentação
   - `N`: Novo jogo
   - `Q`: Sair do jogo
   - `I`: Ativar IA

---

## Fluxo de Jogo

- **Início**:
  - O jogo gera um labirinto aleatório com uma entrada e uma saída.
- **Objetivo**:
  - Alcance a saída (`E`) antes que o tempo se esgote.
- **Sistema de Pontuação**:
  - Cada movimento reduz a pontuação.
  - Movimentos para locais revisitados aplicam penalidades maiores.

---

## Logs de Depuração

- Logs detalhados são gerados no arquivo `ia_debug.log` para acompanhar as decisões da IA e possíveis erros.

---

## Testes

Para executar os testes, use:
```bash
pytest tests/
```

---

## Melhorias Futuras

- Adicionar interface gráfica com `pygame`.
- Melhorar os algoritmos de IA para considerar heurísticas avançadas.
- Implementar modos de dificuldade.

---

## Contribuição

Contribuições são bem-vindas! Por favor, abra um issue ou envie um pull request no repositório.

---

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais informações.
