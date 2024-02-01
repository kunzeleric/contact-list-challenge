def remover_contato(contatos, indice):
  indice_ajustado = indice - 1
  if indice_ajustado >= 0 or indice_ajustado >= len(contatos) or not isinstance(indice_ajustado, int):
    contatos.pop(indice_ajustado)
    print("\nContato removido!")
  else:
    print("\nContato inválido! Tente novamente.")