### Importante
#### O arquivo responsável por executar o Projeto é Main.py.
# Sobre o Projeto
## Este projeto é uma aplicação GUI (Interface Gráfica do Usuário) desenvolvida em Python para gerenciar dados de pesquisa armazenados em um arquivo CSV. Utiliza a biblioteca PySimpleGUI para criar a interface e a biblioteca csv para ler e escrever no arquivo CSV. A aplicação permite ao usuário carregar, visualizar, atualizar, deletar e criar novos registros de dados. Além disso, inclui uma tela de login simples para acessar a funcionalidade principal.

### Pré-requisitos
#### Instalar PySimpleGUI: Abra o terminal ou prompt de comando e execute o seguinte comando para instalar a biblioteca PySimpleGUI:
#### pip install PySimpleGUI

### Preparar o Arquivo CSV: 
#### Certifique-se de que o arquivo Dados de pesquisa.csv esteja no mesmo diretório do script Python. Este arquivo contém os dados de pesquisa que serão gerenciados pela aplicação. Os dados usados no arquivo CSV foram coletados através de alguns usuários que visualizaram um protótipo do layout do site em desenvolvimento e depois responderam às perguntas.

### Funcionalidades: 

#### Tela de Login: A aplicação iniciará com uma tela de login. Insira um email e senha para acessar a funcionalidade principal.

#### Menu Principal: Após o login bem-sucedido, você verá um menu com opções para visualizar, atualizar, deletar e criar novos registros de dados.

### Gerenciamento de Dados:

#### Visualizar Dados: Selecione esta opção para visualizar todos os registros de dados.
#### Atualizar Dados: Selecione esta opção para atualizar um registro de dados existente.
#### Deletar Dados: Selecione esta opção para deletar um registro de dados.
#### Criar Dados: Selecione esta opção para criar um novo registro de dados.
#### Sair: Para sair da aplicação, selecione a opção "Exit" no menu principal.
### Tratamentos de Erros e Validações
#### O projeto implementa tratamento de erros nas operações de leitura e escrita do arquivo CSV, bem como na interface gráfica do usuário (GUI). Por exemplo, ao tentar carregar o arquivo CSV, se o arquivo não for encontrado ou houver um erro durante a leitura, o código captura a exceção FileNotFoundError e Exception geral, imprimindo mensagens de erro apropriadas.

### Validações de Login
#### A validação de login é realizada na função login_gui. Esta função verifica se o campo de email e senha estão preenchidos e se o email está no formato correto. Utiliza expressões regulares para validar o formato do email, verificando se começa com pelo menos três caracteres alfabéticos, contém um '@', e termina com '.com' ou '.br'. Além disso, verifica se a senha tem pelo menos 6 caracteres. Se alguma dessas condições não for atendida, um pop-up de erro é exibido ao usuário.

### Validações na CRUD
#### A validação na CRUD é realizada principalmente nas funções que lidam com a entrada do usuário, como create_gui e update_gui. Por exemplo, na função create_gui, o código verifica se o título da nova pergunta e o valor inseridos são válidos antes de criar um novo registro de dados. Se o título não for fornecido ou o valor não for um número, um pop-up de erro é exibido ao usuário.

### Conclusão
#### Este projeto demonstra uma aplicação GUI para gerenciar dados em um arquivo CSV usando Python e PySimpleGUI. Ele fornece uma solução prática para visualizar, atualizar, deletar e criar novos registros de dados, facilitando a gestão de dados de pesquisa. O projeto também implementa tratamentos de erros e validações importantes para garantir uma experiência de usuário suave e segura.

