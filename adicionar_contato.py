def adicionar_contato():
  contato = {}
  contato.update(nome = input("Qual o nome do contato?"))
  contato.update(telefone = input("Qual o telefone do contato?"))
  contato.update(email = input("Qual o email do contato?"))
  contato.update(favorito = False)
  return contato