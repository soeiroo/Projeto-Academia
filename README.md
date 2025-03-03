# Projeto Academia

Este é um projeto básico para gestão de usuários em uma academia, facilitando o controle de membros e otimizando o gerenciamento. O sistema permite o cadastro de novos usuários, armazenando informações como nome e idade, além de fornecer uma listagem rápida dos membros registrados. Ideal para pequenas academias que buscam organizar seus dados de maneira simples e eficiente.

## Funcionalidades

- **Cadastro de Usuários**: Permite o registro de novos usuários com nome completo e idade.
- **Listagem de Usuários**: Exibe uma lista de todos os usuários cadastrados.
- **Armazenamento de Dados**: Os dados dos usuários são armazenados em um arquivo `users.json` no formato JSON.

## Pré-requisitos

- Python 3.x instalado.

## Como Executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/soeiroo/Projeto-Academia.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd Projeto-Academia
   ```

3. Execute o script principal:

   ```bash
   python main.py
   ```

## Estrutura do Projeto

- `main.py`: Script principal que contém as funcionalidades de cadastro e listagem de usuários.
- `users.json`: Arquivo gerado após a execução do programa, contendo os dados dos usuários cadastrados.

## Como Usar

1. Ao executar o `main.py`, o sistema exibirá um menu com algumas dessas seguintes opções:

   ```
   1 - Cadastrar novo usuário
   2 - Listar usuários
   3 - Sair
   ```

2. Selecione a opção desejada digitando o número correspondente e pressionando Enter.

3. Para cadastrar um novo usuário, escolha a opção 1 e forneça as informações solicitadas.

4. Para listar os usuários cadastrados, escolha a opção 2.

5. Para encerrar o programa, escolha a opção 3.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
