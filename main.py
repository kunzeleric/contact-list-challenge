from menu import menu


def main():
  contatos = []
  while True:
    menu_option = menu()

    match menu_option:
      case 1:
        print("Vamos adicionar um novo contato!\n")
        contato = adicionar_contato()
        contatos.append(contato)
      case 2:
        listar_contatos()
      case 3:
        editar_contato()
      case 4:
        favoritar_contato()
      case 5:
        excluir_contato()
      case 6:
        sair()
      case _:
        print("Opção inválida! Tente novamente.")
        print("\n // ---------------------------------------------- //")

    return

main()