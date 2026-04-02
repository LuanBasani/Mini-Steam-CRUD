# Mini Steam CRUD

## Descrição

Este é um projeto simples de um CRUD (Create, Read, Update, Delete) para gerenciar uma biblioteca de jogos e uma lista de desejos (wishlist), simulando um launcher de jogos como o Steam. A aplicação é escrita em Python e armazena os dados em um arquivo JSON local.

## Funcionalidades

- **Adicionar Jogo**: Permite adicionar jogos à biblioteca (com horas jogadas) ou à wishlist (com preço).
- **Ver Biblioteca/Wishlist**: Lista todos os jogos na categoria escolhida.
- **Atualizar Jogo**: Modifica o título e as informações extras de um jogo existente.
- **Remover Jogo**: Exclui um jogo da lista.
- **Menu Principal**: Interface de texto simples para navegar pelas opções.

## Requisitos

- **Python**: Versão 3.6 ou superior

## Instalação

1. Certifique-se de que o Python 3.6 está instalado no seu sistema.
2. Baixe ou clone este repositório.
3. Salve o código fornecido em um arquivo chamado `mini_steam.py`

## Como Usar

1. Abra um terminal ou prompt de comando.
2. Navegue até o diretório onde o arquivo `mini_steam.py` está localizado.
3. Execute o script com o comando:
   ```
   python mini_steam.py
   ```
4. Siga as instruções no menu para adicionar, listar, atualizar ou remover jogos.

### Exemplo de Uso

- Ao executar, você verá o menu principal.
- Escolha "1" para adicionar um jogo: selecione a categoria (biblioteca ou wishlist), insira o título e as informações extras.
- Escolha "2" para listar jogos: selecione a categoria e veja a lista.
- Os dados são salvos automaticamente em `jogos.json`.

## Estrutura do Código

O código é organizado em funções:

- `menu()`: Exibe o menu principal.
- `escolher_grupo()`: Permite escolher entre biblioteca e wishlist.
- `ler_dados()`: Carrega os dados do arquivo JSON.
- `salvar_dados()`: Salva os dados no arquivo JSON.
- `adicionar()`: Adiciona um novo jogo.
- `listar()`: Lista os jogos de uma categoria.
- `atualizar()`: Atualiza um jogo existente.
- `deletar()`: Remove um jogo.
- `main()`: Loop principal da aplicação.

## Dados Armazenados

Os dados são armazenados em um arquivo `jogos.json` no mesmo diretório do script. A estrutura é:

```json
{
  "biblioteca": [
    {"titulo": "Nome do Jogo", "horas_jogadas": "120h"}
  ],
  "wishlist": [
    {"titulo": "Nome do Jogo", "preco": "R$ 199,90"}
  ]
}
```