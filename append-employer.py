import random
from datetime import datetime

lista_de_funcionarios = []
matricula_aleatoria = random.randint(1000, 5000)

while True:
    matricula_aleatoria = random.randint(1000, 5000)
    funcionario = {}
    data_atual = datetime.now()
    data = data_atual.strftime('%d/%m/%Y %H:%M:%S')

    print('Selecione uma opção')
    pergunta = input('[i]nserir [a]pagar [l]istar por ordem crescente : ')
    if pergunta.lower() == 'i':
        inserir_nome = input('Digite o nome do funcionário: ')
        inserir_cpf = input('Digite o CPF do funcionário: ')
        cpf_existe = False
        for cpf_verificador in lista_de_funcionarios:
            if cpf_verificador.get("cpf") == inserir_cpf:
                cpf_existe = True
                break
        if cpf_existe:
            print('CPF já cadastrado. Tente Novamente.')
            continue
        inserir_data_nascimento = input('Digite a data de Nascimento do funcionário: ')

        funcionario["nome"] = inserir_nome
        funcionario["cpf"] = inserir_cpf
        funcionario["nascimento"] = inserir_data_nascimento
        funcionario["matricula"] = matricula_aleatoria
        matricula_existe: False
        for matricula_verificador in lista_de_funcionarios:
            if matricula_verificador.get("matricula") == funcionario['matricula']:
                matricula_existe = True
                break
            while matricula_existe:
                matricula_aleatoria = random.randint(1000, 5000)
                funcionario['matricula'] = matricula_aleatoria
                matricula_existe = False

                for matricula_verificador in lista_de_funcionarios:
                    if matricula_verificador.get("matricula") == funcionario['matricula']:
                        matricula_existe = True
                        break
        lista_de_funcionarios.append(funcionario)

        print(f'Funcionário {funcionario["nome"]}, no CPF: {funcionario["cpf"]}, nascido na data de {funcionario["nascimento"]}, registrado na matrícula: {funcionario["matricula"]} na data de {funcionario["data_admissao"]}')
        continue
    elif pergunta.lower() == 'a':
        apagar = int(input('Escolha o indice para apagar: '))
        if not lista_de_funcionarios == []:
            lista_de_funcionarios.pop(apagar)
            print('funcionário apagado')
        else: 
            print('Não ha nada para apagar')
    elif pergunta.lower() == 'l':
        if not lista_de_funcionarios == []:
            print('LISTA DE FUNCIONÁRIOS EM ORDEM CRESCENTE')
            for numero, produto in enumerate(lista_de_funcionarios, start=1):
                print(numero, produto)
        else:
            print('Não há nada para listar')
            continue
    else: 
        print('Opção invalida')
        continue
