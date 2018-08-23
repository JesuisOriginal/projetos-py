

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


wrd = input('profess me something, oh godly being \n')


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

    nome = ''
    cpf = ''
    senha = ''
    login = ''
    client_id = cliente_pos

    def set_nome(self):
        self.nome = input('Spell thy name mortal')

    def set_cpf(self):
        self.cpf = input('Spell thy ID u pleasant')

    def set_senha(self):
        self.senha = input('what shall by thy entrance code?')

    def set_login(self):
        self.login = input('tell who thou art')


def cria_cliente():
    nonlocal novo_cliente
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
    logged = cliente_seguro(hash(unsafe_login) + hash(unsafe_senha))
    if logged:
        print('is logged')
    # TODO code for login here


def logged(cliente):
    print('thou are now inside a limbo of mind')


def game_on():
    print('Hello my Mastah, sho me da wey')
    print('i shall hide thy words!!')
    print()

