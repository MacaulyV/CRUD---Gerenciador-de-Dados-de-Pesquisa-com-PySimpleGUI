from Crud import crud_gui
from Dependencias import sg, re

# Função para criar a interface gráfica do usuário (GUI) de login
def login_gui():
    # Definindo o layout da janela de login com campos para email e senha, e botões para entrar ou cancelar
    layout = [
        [sg.Text("Email"), sg.InputText(key='-EMAIL-')],
        [sg.Text("Senha"), sg.InputText(key='-SENHA-', password_char='*')],
        [sg.Button('Entrar'), sg.Button('Cancelar')]
    ]

    # Criando a janela de login com o layout definido
    window = sg.Window("Login", layout)

    # Loop para ler os eventos da janela e processar as entradas do usuário
    while True:
        event, values = window.read()
        # Se a janela for fechada ou o botão 'Cancelar' for pressionado, encerra o loop
        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break
        # Se o botão 'Entrar' for pressionado, verifica as credenciais do usuário
        elif event == 'Entrar':
            email = values['-EMAIL-']
            senha = values['-SENHA-']
            
            # Verifica se os campos de email e senha estão preenchidos
            if not email and not senha:
                sg.popup_error("Por favor, insira algo no campo de email e/ou senha.")
            elif not email:
                sg.popup_error("Por favor, insira seu email.")
            elif not senha:
                sg.popup_error("Por favor, insira sua senha.")
            # Verifica se o email está no formato correto
            elif not re.match(r'^[a-zA-Z]{3,}', email):
                sg.popup_error("Email inválido. O email deve começar com seu nome.")
            elif '@' not in email:
                sg.popup_error("Email inválido. Faltando '@' ou o email está incompleto.")
            elif not re.search(r'\.com$|\.br$', email):
                sg.popup_error("Email inválido. Faltando '.com' ou '.br' no final.")
            # Verifica se a senha tem pelo menos 6 caracteres
            elif len(senha) < 6:
                sg.popup_error("Senha inválida. A senha deve ter pelo menos 6 caracteres.")
            else:
                # Se todas as verificações passarem, exibe uma mensagem de sucesso e chama a função de CRUD
                sg.popup("Login bem-sucedido!")
                window.close()
                crud_gui()
                break

    # Fecha a janela de login
    window.close()
