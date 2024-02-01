def visualizar_contatos(contatos):
  print("Lista de Contatos:")
  for indice, contato in enumerate(contatos, start=1):
    favorito = "\u2764\ufe0f" if contato["favorito"] == True else " "
    nome_contato = contato["nome"]
    tel_contato = contato["telefone"]
    email_contato = contato["email"]
    print(f"\n{indice}. [{favorito} ] {nome_contato} - {tel_contato} - {email_contato}\n")
  return  