from create_user import create_user
from read_users import read_users
from update_user import update_user
from delete_user import delete_user

def menu():
    while True:
        print("\n=== CRUD TERMINAL ===")
        print("1. Criar usuário")
        print("2. Listar usuários")
        print("3. Atualizar usuário")
        print("4. Excluir usuário")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            create_user()
        elif choice == '2':
            read_users()
        elif choice == '3':
            update_user()
        elif choice == '4':
            delete_user()
        elif choice == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
