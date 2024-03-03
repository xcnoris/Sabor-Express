pessoa = {
    'nome': 'Augusto',
    'idade' : 18,
    'nacionalidade' : 'Brasileiro'
}

# Alterando tabelas e adicionando tabelas ao dicionario
pessoa.update({'nome':'Gabriel'})
pessoa.update({'profissao':'Desenvolvedor'})
pessoa.update({'A':2})
pessoa.update({'B':10})

# Removendo um item do dicionario
del pessoa['A']
pessoa.pop('B')


print(pessoa)

