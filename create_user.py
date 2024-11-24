from database import get_db_connection

def create_user():
    db = get_db_connection()
    cursor = db.cursor()

    name = input("Digite o nome: ")
    email = input("Digite o email: ")
    phone = input("Digite o telefone: ")

    try:
        cursor.execute(
            "INSERT INTO users (name, email, phone) VALUES (%s, %s, %s)",
            (name, email, phone)
        )
        db.commit()
        print("Usuário criado com sucesso!")
    except Exception as e:
        print(f"Erro ao criar usuário: {e}")
    finally:
        cursor.close()
        db.close()
