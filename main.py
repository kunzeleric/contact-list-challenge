from menu import menu
from adicionar_contato import adicionar_contato
from visualizar_contatos import visualizar_contatos

def main():
  contatos = []
  while True:
    menu_option = menu()

    match menu_option:
      case 1:
        print("\nVamos adicionar um novo contato!\n")
        contato = adicionar_contato()
        contatos.append(contato)
      case 2:
        visualizar_contatos(contatos)
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

main()