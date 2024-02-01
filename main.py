from menu import menu
from adicionar_contato import adicionar_contato
from visualizar_contatos import visualizar_contatos
from editar_contato import editar_contato
from favoritar_contato import favoritar_contato
from remover_contato import remover_contato

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
        visualizar_contatos(contatos)
        indice = int(input("\nSelecione o contato que deseja editar:\n"))
        editar_contato(contatos, indice)
      case 4:
        visualizar_contatos(contatos)
        indice = int(input("\nSelecione o contato que deseja favoritar:\n"))
        favoritar_contato(contatos, indice)
      case 5:
        visualizar_contatos(contatos)
        indice = int(input("\nSelecione o contato que deseja remover:\n"))
        remover_contato(contatos, indice)
      case 6:
        break
      case _:
        print("Opção inválida! Tente novamente.")
        print("\n // ---------------------------------------------- //")

main()