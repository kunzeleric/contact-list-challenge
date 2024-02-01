def editar_contato(contatos, indice):
  indice_ajustado = indice - 1
  if indice_ajustado >= 0 or indice_ajustado >= len(contatos) or not isinstance(indice_ajustado, int):
    contatos[indice_ajustado]["nome"]=input("Digite o novo nome do contato: ")
    contatos[indice_ajustado]["telefone"]=input("Digite o novo telefone do contato: ")
    contatos[indice_ajustado]["email"]=input("Digite o novo email do contato: ")
  else:
    print("\nContato inválido! Tente novamente.")	
