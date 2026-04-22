from db.db_connect import cursor, conn

def save_to_db(name, age, gender, symptoms, prediction):
    query = """
    INSERT INTO user_data (name, age, gender, symptoms, prediction)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (name, age, gender, str(symptoms), str(prediction)))
    conn.commit()