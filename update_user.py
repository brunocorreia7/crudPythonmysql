from database import get_db_connection

def update_user():
    db = get_db_connection()
    cursor = db.cursor()

    user_id = input("Digite o ID do usuário que deseja atualizar: ")
    name = input("Novo nome: ")
    email = input("Novo email: ")
    phone = input("Novo telefone: ")

    try:
        cursor.execute(
            "UPDATE users SET name=%s, email=%s, phone=%s WHERE id=%s",
            (name, email, phone, user_id)
        )
        db.commit()

        if cursor.rowcount > 0:
            print("Usuário atualizado com sucesso!")
        else:
            print("Usuário não encontrado.")
    except Exception as e:
        print(f"Erro ao atualizar usuário: {e}")
    finally:
        cursor.close()
        db.close()
