import os
import random
from datetime import datetime
import time

lista_de_funcionarios = []  # Lista para armazenar os funcionários

matricula_aleatoria = random.randint(1000, 5000)  # Gera uma matrícula aleatória

try:
    while True:
        matricula_aleatoria = random.randint(1000, 5000)  # Gera uma nova matrícula aleatória
        _funcionarios_ordenados_ = {}  # Dicionário para armazenar informações do funcionário atual
        data_atual = datetime.now()  # Obtém a data e hora atual
        data = data_atual.strftime('%d/%m/%Y %H:%M')  # Formata a data e hora atual em uma string

        print('Selecione uma opção')
        pergunta = input('[i]nserir [a]pagar [l]istar [o]rdenar: ')

        time.sleep(1)  # Espera por 1 segundo

        if pergunta.lower() == 'i':
            # Opção para inserir um novo funcionário
            inserir_nome = input('Digite o nome do funcionário: ')
            time.sleep(0.5)  # Espera por 0.5 segundos

            while True:
                # Obtém o CPF do funcionário com validação
                inserir_cpf = input('Digite o CPF do funcionário: ')
                if len(inserir_cpf) != 14:
                    print('CPF inválido!')
                    continue
                else:
                    break

            time.sleep(0.5)  # Espera por 0.5 segundos

            cpf_existe = False
            for cpf_verificador in lista_de_funcionarios:
                if cpf_verificador.get("cpf") == inserir_cpf:
                    cpf_existe = True
                    break

            if cpf_existe:
                print('CPF já cadastrado. Tente novamente.')
                continue

            inserir_data_nascimento = input('Digite a data de Nascimento do funcionário: ')
            time.sleep(0.5)  # Espera por 0.5 segundos

            _funcionarios_ordenados_["nome"] = inserir_nome
            _funcionarios_ordenados_["cpf"] = inserir_cpf
            _funcionarios_ordenados_["nascimento"] = inserir_data_nascimento
            _funcionarios_ordenados_["matricula"] = matricula_aleatoria

            matricula_existe = False
            for matricula_verificador in lista_de_funcionarios:
                if matricula_verificador.get("matricula") == _funcionarios_ordenados_['matricula']:
                    matricula_existe = True
                    break

                while matricula_existe:
                    matricula_aleatoria = random.randint(1000, 5000)
                    _funcionarios_ordenados_['matricula'] = matricula_aleatoria
                    matricula_existe = False

                    for matricula_verificador in lista_de_funcionarios:
                        if matricula_verificador.get("matricula") == _funcionarios_ordenados_['matricula']:
                            matricula_existe = True
                            break

            _funcionarios_ordenados_["data"] = data

            lista_de_funcionarios.append(_funcionarios_ordenados_)

            print(f'Funcionário {_funcionarios_ordenados_["nome"]}, no CPF: {_funcionarios_ordenados_["cpf"]}, nascido na data de {_funcionarios_ordenados_["nascimento"]}, registrado na matrícula: {_funcionarios_ordenados_["matricula"]} na data de {_funcionarios_ordenados_["data"]}')

            continue

        elif pergunta.lower() == 'a':
            # Opção para apagar um funcionário
            time.sleep(1)  # Espera por 1 segundo
            apagar = int(input('Escolha o índice do funcionário para apagar iniciando pelo 0'))

            if not lista_de_funcionarios == []:
                lista_de_funcionarios.pop(apagar)
                print('Funcionário apagado')
            else:
                print('Não há nada para apagar')

        elif pergunta.lower() == 'l':
            # Opção para listar os funcionários
            if not lista_de_funcionarios == []:
                print('LISTA DE FUNCIONÁRIOS EM ORDEM CRESCENTE')
                for nume_, funcio_ in enumerate(lista_de_funcionarios):
                    print(nume_, funcio_)
            else:
                print('Não há nada para listar')
                continue

        elif pergunta.lower() == 'o':
            # Opção para ordenar os funcionários por matrícula
            lista_ordenada = sorted(lista_de_funcionarios, key=lambda x: x["matricula"])
            for _funcionarios_ordenados_ in lista_ordenada:
                print(f'Matrícula: {_funcionarios_ordenados_["matricula"]}, Nome: {_funcionarios_ordenados_["nome"]}, CPF: {_funcionarios_ordenados_["cpf"]}, Nascimento: {_funcionarios_ordenados_["nascimento"]}, Data de Cadastro: {_funcionarios_ordenados_["data"]}')

        else:
            print('Opção inválida')
            continue

except Exception as e:
    # Trata exceções genéricas
    os.system('cls')  # Limpa a tela do console (para Windows)
    print('Ocorreu um erro, entre em contato com os desenvolvedores')
    print(f'Erro ocorrido: {e}')
    exit()
