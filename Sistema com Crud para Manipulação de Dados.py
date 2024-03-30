import PySimpleGUI as sg
import csv
import re

def load_csv_to_list():
    try:
        with open('Dados de pesquisa.csv', 'r', encoding='utf-8') as f:
            dict_reader = csv.DictReader(f)
            list_of_dict = list(dict_reader)
        return list_of_dict
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return []
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}")
        return []
    finally:
        print("Tentativa de carregar o arquivo concluída.")

def update_data(data, question, new_value):
    try:
        for item in data:
            if item['Pergunta'] == question:
                item['Quantidade'] = new_value
                break
        save_data_to_csv(data)
    except Exception as e:
        print(f"Erro ao atualizar os dados: {e}")
    finally:
        print("Tentativa de atualização concluída.")

def delete_data(data, question):
    try:
        for item in data:
            if item['Pergunta'] == question:
                data.remove(item)
                break
        save_data_to_csv(data)
    except Exception as e:
        print(f"Erro ao deletar os dados: {e}")
    finally:
        print("Tentativa de deleção concluída.")

def create_data(data, question, value):
    try:
        data.append({'Pergunta': question, 'Resposta': '', 'Quantidade': value})
        save_data_to_csv(data)
    except Exception as e:
        print(f"Erro ao criar os dados: {e}")
    finally:
        print("Tentativa de criação concluída.")

def save_data_to_csv(data):
    try:
        with open('Dados de pesquisa.csv', 'w', newline='', encoding='utf-8') as f:
            fieldnames = ['Pergunta', 'Resposta', 'Quantidade']
            dict_writer = csv.DictWriter(f, fieldnames=fieldnames)
            dict_writer.writeheader()
            dict_writer.writerows(data)
    except Exception as e:
        print(f"Erro ao salvar os dados no arquivo: {e}")
    finally:
        print("Tentativa de salvar os dados concluída.")

def view_data(data):
    layout = []
    for item in data:
        layout.append([sg.Text(f"{item['Pergunta']}: {item['Resposta']} - {item['Quantidade']}")])
    layout.append([sg.Button("Voltar")])
    window = sg.Window("Visualizar Dados", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Voltar":
            break

    window.close()

def update_gui(data):
    layout = [[sg.Text("Selecione uma pergunta para atualizar:")]]
    for item in data:
        layout.append([sg.Button(item['Pergunta'], key=item['Pergunta'])])
    layout.append([sg.Button("Voltar")])
    window = sg.Window("Atualizar Dados", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Voltar":
            break
        elif event in [item['Pergunta'] for item in data]:
            window.close()
            new_value = sg.popup_get_text("Digite o novo valor:", title="Atualizar Valor", default_text="")
            if new_value.isdigit():
                update_data(data, event, new_value)
                sg.popup("Valor atualizado com sucesso!")
            else:
                sg.popup_error("Por favor, insira um número válido.")
            break

    window.close()

def delete_gui(data):
    layout = [[sg.Text("Selecione uma pergunta para deletar:")]]
    for item in data:
        layout.append([sg.Button(item['Pergunta'], key=item['Pergunta'])])
    layout.append([sg.Button("Voltar")])
    window = sg.Window("Deletar Dados", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Voltar":
            break
        elif event in [item['Pergunta'] for item in data]:
            window.close()
            if sg.popup_yes_no("Tem certeza de que deseja deletar esta pergunta?") == "Yes":
                delete_data(data, event)
                sg.popup("Pergunta deletada com sucesso!")
            break

    window.close()

def create_gui(data):
    layout = [[sg.Text("Digite o título da nova pergunta:")],
              [sg.InputText(key='-QUESTION-')],
              [sg.Text("Digite o valor para a nova pergunta:")],
              [sg.InputText(key='-VALUE-', size=(8, 1))],
              [sg.Button("Criar"), sg.Button("Voltar")]]
    window = sg.Window("Criar Dados", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Voltar":
            break
        elif event == "Criar":
            new_question = values['-QUESTION-']
            new_value = values['-VALUE-']
            if new_question and new_value.isdigit():
                create_data(data, new_question, new_value)
                sg.popup("Pergunta criada com sucesso!")
            else:
                sg.popup_error("Por favor, insira um título válido e um número para o valor.")
            break

    window.close()

def login_gui():
    layout = [
        [sg.Text("Email"), sg.InputText(key='-EMAIL-')],
        [sg.Text("Senha"), sg.InputText(key='-SENHA-', password_char='*')],
        [sg.Button('Entrar'), sg.Button('Cancelar')]
    ]

    window = sg.Window("Login", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break
        elif event == 'Entrar':
            email = values['-EMAIL-']
            senha = values['-SENHA-']
            
            if not email and not senha:
                sg.popup_error("Por favor, insira algo no campo de email e/ou senha.")
            elif not email:
                sg.popup_error("Por favor, insira seu email.")
            elif not senha:
                sg.popup_error("Por favor, insira sua senha.")
            elif not re.match(r'^[a-zA-Z]{3,}', email):
                sg.popup_error("Email inválido. O email deve começar com seu nome.")
            elif '@' not in email:
                sg.popup_error("Email inválido. Faltando '@' ou o email está incompleto.")
            elif not re.search(r'\.com$|\.br$', email):
                sg.popup_error("Email inválido. Faltando '.com' ou '.br' no final.")
            elif len(senha) < 6:
                sg.popup_error("Senha inválida. A senha deve ter pelo menos 6 caracteres.")
            else:
                sg.popup("Login bem-sucedido!")
                window.close()
                crud_gui()
                break

    window.close()

def crud_gui():
    data = load_csv_to_list()
    menu_layout = [
        [sg.Button("View"), sg.Button("Delete"), sg.Button("Create"), sg.Button("Update")],
        [sg.Button("Exit")]
    ]

    menu_window = sg.Window("Menu", menu_layout)

    while True:
        event, values = menu_window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            save_data_to_csv(data)
            break
        elif event == "View":
            view_data(data)
        elif event == "Delete":
            delete_gui(data)
        elif event == "Create":
            create_gui(data)
        elif event == "Update":
            update_gui(data)

    menu_window.close()

if __name__ == "__main__":
    login_gui()
