from database import get_db_connection

def read_users():
    db = get_db_connection()
    cursor = db.cursor()

    try:
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()

        print("\nID | Nome | Email | Telefone")
        print("-" * 30)
        for user in results:
            print(f"{user[0]} | {user[1]} | {user[2]} | {user[3]}")
    except Exception as e:
        print(f"Erro ao listar usuários: {e}")
    finally:
        cursor.close()
        db.close()
