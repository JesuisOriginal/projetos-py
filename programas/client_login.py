import json
import os

cliente_pos = 0
client_list = []
# hasheando na mao, pode ser feito tambem pela hashlib builtin


def encrypt(word):
    golden_speach = []
    final_speach = []
    for i in range(len(word)):

        safe = (ord(word[i]) + 10)

        if safe > 126:
            safe = safe % 126
            if safe < 32:
                safe += 32

        golden_speach.insert(i, safe)
        final_speach.append((chr(golden_speach[i])))

    # print(' '.join(final_speach)) printa bunnitinho o que o usuario digitou
    return final_speach


#  TODO fazer o que o professor pedui aqui, eplicarei  depois como reduzir o tempo de exec
# Ex de coiso que lek pode ter pedido


def protejer_info_clientes(nome, cpf, senha, login):
    # cria um hashcode que tera o cliente em forma de um codgo hash em outras palavras um HASHCODE OwO
    hash_nome = encrypt(nome)
    hash_cpf = encrypt(cpf)
    hash_senha = encrypt(senha)
    hash_login = encrypt(login)
    global hashcode
    hashcode = hash_nome + hash_cpf + hash_login + hash_senha
    return hash_nome + hash_cpf + hash_login + hash_senha


def is_safe(hash_gerado, hashcode):
    if hashcode is hash_gerado:
        return True
    else:
        return False


# declaracao aleatoria pra demo, ele ira gerar um dependo do que o usuario
# digitar na tentativa de login e comparar se eh igual ao hashcode ja salvo na memoria
hash_gerado_pela_entrada = 'daosbdojasjdaslkd'


class Cliente:
    # general code shall ve the index of the cliente in the list of clients
    code = {}
    nome = ''
    cpf = ''
    senha = ''
    login = ''
    pos = {}
    client_id = cliente_pos

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_cpf(self, cpf):
        self.cpf = cpf

    def set_senha(self, senha):
        self.senha = senha

    def set_login(self, login):
        self.login = login

    Client_data = {
        "Nome": nome,
        "code": code,
        "pos": pos
    }


novo_cliente = Cliente


def cria_cliente():
    global novo_cliente
    novo_cliente = Cliente
    novo_cliente.set_nome()
    novo_cliente.set_cpf()
    novo_cliente.set_login()
    novo_cliente.set_senha()
    print('thou shall be not forgotten')
    global client_list
    client_list.append(hash(novo_cliente.login) + hash(novo_cliente.senha))
    global cliente_pos
    cliente_pos += 1


def client_list_update(cliente_novo):
    global client_list
    client_list = []
    for i in range(cliente_pos):
        client_list.append(cliente_novo)


def cliente_seguro(hash_gerado_pela_entrada2):
    # ira verificar se os dados do cliente nao foram alterados e retornar True se sim
    if is_safe(hash_gerado_pela_entrada2, hashcode):
        print('client data is secure')
        return True
    else:
        return False


def hash_client(cliente):
    print('thou are now the unseen')
    hash_code = hash(cliente.login) + hash(cliente.senha)
    return hash_code


def login():
    print('sho me ur guts')
    unsafe_login = input('sho me ur guts')
    unsafe_senha = input('tell me the secret code')
    hash_test = cliente_seguro(hash(unsafe_login) + hash(unsafe_senha))
    if hash_test == client_list[find_account(hash_test)].code:
        print('U HAVE LIGMA')


def find_account(code):
    for client in client_list:
        if client.code == code:
            return client.pos
            break


def persist_data():
    with open("data_file.json", "a") as write_file:
        json.dump(client_list, write_file)


def save_on_file(data):
    with open("data_test.json", "w") as write_file:
        json.dump(data, write_file)


def read():
    with open('data_file.txt') as json_file:
        return json.load(json_file)


def game_on():
    print('Hello my Mastah, sho me da wey')
    print('i shall hide thy words!!')
    print('do u hev the word? Yes/No')
    response = input('ur response')
    if response == "Yes":
        login()
    elif response == "No":
        awnser = input('thou wish to create a persona? Yes/No')
        if awnser == "Yes":
            cria_cliente()
        elif awnser == "No":
            print('farewell')
            exit(0)
    else:
        print('invalid awnser PEASANTRY')
        exit(0)


client_test = Cliente
client_test.set_nome(client_test,"name")
client_test.set_login(client_test, 'login')
client_test.set_senha(client_test, 'senha')
client_test.set_cpf(client_test, '111.222.333-44')

save_on_file(client_test.Client_data)

# def test_file():
#     save_on_file("test")
#
#
# test_file()
