import PySimpleGUI as sg
import csv
import re

# Função para carregar os dados do arquivo CSV em uma lista de dicionários
def load_csv_to_list():
    try:
        # Abre o arquivo CSV em modo de leitura com codificação UTF-8
        with open('Dados de pesquisa.csv', 'r', encoding='utf-8') as f:
            # Cria um DictReader para ler o arquivo CSV como um dicionário
            dict_reader = csv.DictReader(f)
            # Converte o DictReader em uma lista de dicionários
            list_of_dict = list(dict_reader)
        # Retorna a lista de dicionários
        return list_of_dict
    except FileNotFoundError:
        # Caso o arquivo não seja encontrado, imprime uma mensagem e retorna uma lista vazia
        print("Arquivo não encontrado.")
        return []
    except Exception as e:
        # Caso ocorra algum outro erro, imprime a mensagem de erro e retorna uma lista vazia
        print(f"Erro ao carregar o arquivo: {e}")
        return []
    finally:
        # Imprime uma mensagem indicando que a tentativa de carregar o arquivo foi concluída
        print("Tentativa de carregar o arquivo concluída.")

# Função para salvar os dados em um arquivo CSV
def save_data_to_csv(data):
    try:
        # Abre o arquivo CSV em modo de escrita com codificação UTF-8
        with open('Dados de pesquisa.csv', 'w', newline='', encoding='utf-8') as f:
            # Define os nomes das colunas para o arquivo CSV
            fieldnames = ['Pergunta', 'Resposta', 'Quantidade']
            # Cria um DictWriter para escrever os dados no arquivo CSV
            dict_writer = csv.DictWriter(f, fieldnames=fieldnames)
            # Escreve o cabeçalho no arquivo CSV
            dict_writer.writeheader()
            # Escreve as linhas de dados no arquivo CSV
            dict_writer.writerows(data)
    except Exception as e:
        # Caso ocorra algum erro, imprime a mensagem de erro
        print(f"Erro ao salvar os dados no arquivo: {e}")
    finally:
        # Imprime uma mensagem indicando que a tentativa de salvar os dados foi concluída
        print("Tentativa de salvar os dados concluída.")

