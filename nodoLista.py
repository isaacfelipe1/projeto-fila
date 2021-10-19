
#inserir=input("Digite um valor \n")
#depois=input("Digite outro valorz\n")
class NodoLista:
    """ Esta classe representa um nodo de uma Lista Encadeada"""
    def __init__(self,dado=0, proximo_nodo=None):
        self.dado=dado
        self.proximo=proximo_nodo
    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)
class ListaEncadeada:
    """ esta classe Representa uma lista encadeada"""
    def __init__(self):
        self.cabeca=None
    def __repr__(self):
        return "[" + str(self.cabeca) + "]"
def insere_no_inicio(lista,novo_dado):
    # 1) Crie um novo nodo com o dado a ser armazernado.
    novo_nodo=NodoLista(novo_dado)
    #2) Faz com que o novo nodo seja a cabeça da Lista
    novo_nodo.proximo=lista.cabeca
    #3) Faz com que a cabeça da lista referencie o novo nodo.
    lista.cabeca=novo_nodo
def insere_depois(lista,nodo_anterior, novo_dado):
    assert nodo_anterior, "Nodo anterior precisa existir na lista"
    #cria um novo nodo com o dado desejado.
    novo_nodo=NodoLista(novo_dado)
    #Faz o próximo do novo nodo ser o próximo do nodo anterior.
    novo_nodo.proximo=nodo_anterior.proximo
    #Faz com que o novo nodo seja o próximo do nodo anterior.
    nodo_anterior.proximo=novo_nodo
def busca(lista, valor):
    corrente = lista.cabeca
    while corrente and corrente.dado != valor:
        corrente = corrente.proximo
    return corrente
lista=ListaEncadeada()
for i in range(8):
    insere_no_inicio(lista, i)
print("Lista:", lista)
for i in range(8,-4,-2):
    elemento = busca(lista, i)
    if elemento:
        print("Elemento {0} presente na lista!".format(i))
    else:
        print("Elemento {0} não encontrado.".format(i))





#print("Lista Vazia : ", lista)
#insere_no_inicio(lista, inserir)
#print("Lista contém um ùnico ELemento : ", lista)
#nodo_anterior=lista.cabeca
#insere_depois(lista,nodo_anterior,depois)
#print("Inserido um novo elemento depois de um outro :",lista)
