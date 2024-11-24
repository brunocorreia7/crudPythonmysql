from database import get_db_connection

def delete_user():
    db = get_db_connection()
    cursor = db.cursor()

    user_id = input("Digite o ID do usuário que deseja excluir: ")

    try:
        cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
        db.commit()

        if cursor.rowcount > 0:
            print("Usuário excluído com sucesso!")
        else:
            print("Usuário não encontrado.")
    except Exception as e:
        print(f"Erro ao excluir usuário: {e}")
    finally:
        cursor.close()
        db.close()
