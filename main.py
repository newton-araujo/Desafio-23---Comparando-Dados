'''
Para este desafio, vamos criar dois conjuntos, cada um contendo 5 nomes.

Requisitos:
- Verificar quais nomes, tem em ambos conjuntos.

Saida:
- Imprimir o resultado.

'''
#Lista de clientes
clientes = ['Pedro','Ana','Carlos','Maria','Antonio']

#lista de pendências
pendencia = ['Pedro','Flavio', 'Maria', 'Claudio','Laura']

#Verificando através do SET os nomes que estão presente nas duas listas.
verificar = set(clientes).intersection(set(pendencia))

#saida
for nome in list(verificar):
    print(nome)
