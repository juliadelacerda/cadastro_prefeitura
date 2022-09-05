# Criar lista para somar os impostos
# Associar melhor a prefeitura com as empresas e o prefeito

import string

class Empresa:
    def __init__(self, nome, cnpj, media_funcionarios, media_lucro_mensal):
        self.nome = nome
        self.cnpj = cnpj
        self.media_funcionarios = media_funcionarios
        self.media_lucro_mensal = media_lucro_mensal
        self.cidade = Prefeitura
        self.impostos_a_pagar = 0



    # Adicionará o valor de impostos que a empresa terá de pagar sabendo que o valor será 1,6% de seu lucro mensal 
    def set_impostos(self):
        self.impostos_a_pagar += self.media_lucro_mensal * 0.016 # cálculo dos impostos

        return self.impostos_a_pagar



class Prefeitura:
    def __init__(self, cidade):
        self.prefeito = Prefeito
        self.cidade = cidade
        self.valor_total_impostos = 0



    # Adicionará o valor que a empresa pagou ao valor total dos impostos que a prefeitura irá receber
    def set_valor_total_impostos (self):
        self.valor_total_impostos = 0
        return self.valor_total_impostos




class Prefeito:
    def __init__(self, nome_prefeito, cpf, formacao, cidade):
        self.nome_prefeito = nome_prefeito
        self.cpf = cpf
        self.formacao = formacao
        self.cidade = cidade



empresaX = Empresa('', '', 0, 0)
prefeituraX = Prefeitura('')
prefeitoX = Prefeito('', '', '', '')



# Mensagem de Boas-vindas
print(' \n \n--------- BEM-VINDO AO SISTEMA DE TRIBUTOS ---------')
print('Aqui você poderá consultar e cadastrar empresas, suas respectivas cidades e o prefeito de cada cidade!')


msg = ''
empresas_cadastradas = []




# cria um sistema que o usuário pode cadastrar quantas empresas, prefeituras e prefeitos quiser
while (msg != 'sair'):
    # Recebe o que o usuário que fazer no sistema: cadastrar uma empresa, cadastrar uma prefeitura ou cadastrar um prefeito
    msg = (input('- Para cadastrar uma nova empresa, aperte 1;\n- Para cadastrar uma nova prefeitura, aperte 2;\n- Para cadastrar um novo prefeito, aperte 3; \n- Para consultar as empresas cadastradas, aperte 4;\n- Para consultar a prefeitura cadastrada, aperte 5;\n- Para sair, digite "sair".\n'))

    cadastro_empresa = '1'
    cadastro_prefeitura = '2'
    cadastro_prefeito = '3'
    consulta_empresas = '4'
    consulta_prefeitura = '5'



    # Verifica o número digitado pelo usuário para exercer a função solicitada
    # Cadastra uma nova empresa
    if (msg == cadastro_empresa): 
        empresaX.nome = input('\nDigite o nome da empresa: \n')
        empresaX.cnpj = input('Digite o CNPJ da empresa: \n')
        empresaX.media_funcionarios = input('Digite uma média de quantos funcionários essa empresa tem: \n')
        empresaX.media_lucro_mensal = float(input('Digite a média de lucro mensal da empresa: \n'))
        

        
        # Mensagem 
        print(f'\nCadastro da empresa {string.capwords(empresaX.nome)} concluído com sucesso!')
        print(f'- Nome: {string.capwords(empresaX.nome)}\n- CNPJ: {empresaX.cnpj}\n- Média de funcionários: {empresaX.media_funcionarios}\n- Média de lucro mensal: R${empresaX.media_lucro_mensal} \n')
        

        print(f'A empresa {string.capwords(empresaX.nome)} deve pagar R${empresaX.set_impostos()} em impostos \n\n') #Exibe os impostos que a empresa deve pagar



        # Adiciona a empresa digitada à uma lista
        empresas_cadastradas.append(empresaX.nome)
        print(f'Essas são as empresas já cadastradas: {empresas_cadastradas} \n \n')

        # Adiciona os impostos a uma lista
        prefeituraX.valor_total_impostos += empresaX.impostos_a_pagar




    # Cadastra uma prefeitura
    elif (msg == cadastro_prefeitura): 
        prefeituraX.cidade = input('\nDigite a cidade da prefeitura: \n')
        prefeituraX.prefeito = input('Digite o nome do prefeito da cidade: \n')

        # Mensagem de ëxito no cadastro
        print(f'Prefeitura de {string.capwords(prefeituraX.cidade)} cadastrada com sucesso!\n')

        if len(empresas_cadastradas) > 0:
            print(f'Empresas cadastradas nessa cidade: {empresas_cadastradas}\n')

            # Exibe o valor total de impostos que a prefeitura tem a receber em impostos
            print(f'A prefeitura de {prefeituraX.cidade} deve receber R${prefeituraX.valor_total_impostos} em impostos\n')
            
        else: 
            print('Não há nenhuma empresa cadastrada nessa cidade!\n')


    # Cadastra o prefeito
    elif (msg == cadastro_prefeito): 
        prefeitoX.nome_prefeito = input('Digite o nome e sobrenome do prefeito: \n')
        prefeitoX.cpf = input('Digite o CPF do prefeito: \n')
        prefeitoX.formacao = input('Digite a formação do prefeito: \n')
        
        # Mensagem de êxito no cadastro
        print(f'Prefeito {prefeitoX.nome_prefeito} cadastrado com sucesso!\n')

        print(f'- Nome: {prefeitoX.nome_prefeito} \n- CPF: {prefeitoX.cpf}\n- Formação: {prefeitoX.formacao}\n- Cidade: {prefeituraX.cidade}\n\n')
        


    elif (msg == consulta_empresas):
        # Confere se já tem alguma empresa cadastrada
        if len(empresas_cadastradas) > 0:
            for i in range(len(empresas_cadastradas)):
                print(f'\nEssas são as empresas que você cadastrou: {empresas_cadastradas}\n')

        # Se não tiver nenhuma empresa cadastrada, aparece a mensagem de aviso
        else:
            print('\n\nVocê não cadastrou nenhuma empresa!\n\n')


    elif msg == consulta_prefeitura:
        if prefeituraX.cidade != '':
            print(f'A prefeitura que você tem cadastrada é a de {string.capwords(prefeituraX.cidade)}\nEla deve receber cerca de R${prefeituraX.valor_total_impostos} em impostos')
            print('Você só pode cadastrar uma prefeitura!\n')
        else: 
            print('Você não cadastrou nenhuma prefeitura!')


    elif (msg == 'sair'):
        print('Você saiu do sistema com sucesso! Volte sempre!')



    else: 
        print('Número inválido, tente novamente!')



print('----------------------------------------------------')

