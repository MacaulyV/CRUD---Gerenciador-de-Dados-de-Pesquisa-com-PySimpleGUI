from Dependencias import sg, csv, save_data_to_csv, load_csv_to_list

# Função para atualizar dados existentes
def update_data(data, question, new_value):
    try:
        # Itera sobre os dados para encontrar a pergunta correspondente
        for item in data:
            if item['Pergunta'] == question:
                # Atualiza o valor da pergunta encontrada
                item['Quantidade'] = new_value
                break
        # Salva os dados atualizados no CSV
        save_data_to_csv(data)
    except Exception as e:
        # Imprime mensagem de erro caso ocorra uma exceção
        print(f"Erro ao atualizar os dados: {e}")
    finally:
        # Mensagem de conclusão da tentativa de atualização
        print("Tentativa de atualização concluída.")

# Função para deletar dados existentes
def delete_data(data, question):
    try:
        # Itera sobre os dados para encontrar a pergunta correspondente
        for item in data:
            if item['Pergunta'] == question:
                # Remove a pergunta encontrada dos dados
                data.remove(item)
                break
        # Salva os dados atualizados no CSV
        save_data_to_csv(data)
    except Exception as e:
        # Imprime mensagem de erro caso ocorra uma exceção
        print(f"Erro ao deletar os dados: {e}")
    finally:
        # Mensagem de conclusão da tentativa de deleção
        print("Tentativa de deleção concluída.")

# Função para criar novos dados
def create_data(data, question, value):
    try:
        # Adiciona um novo item aos dados com a pergunta e valor fornecidos
        data.append({'Pergunta': question, 'Resposta': '', 'Quantidade': value})
        # Salva os dados atualizados no CSV
        save_data_to_csv(data)
    except Exception as e:
        # Imprime mensagem de erro caso ocorra uma exceção
        print(f"Erro ao criar os dados: {e}")
    finally:
        # Mensagem de conclusão da tentativa de criação
        print("Tentativa de criação concluída.")

# Função para visualizar dados existentes
def view_data(data):
    # Cria um layout para exibir os dados
    layout = []
    for item in data:
        layout.append([sg.Text(f"{item['Pergunta']}: {item['Resposta']} - {item['Quantidade']}")])
    layout.append([sg.Button("Voltar")])
    # Cria uma janela para exibir os dados
    window = sg.Window("Visualizar Dados", layout)

    # Loop para manter a janela aberta até que o usuário feche ou clique em "Voltar"
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Voltar":
            break

    window.close()

# Função para atualizar dados através da GUI
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

# Função para deletar dados através da GUI
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

# Função para criar novos dados através da GUI
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

# Função principal para iniciar a GUI
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
