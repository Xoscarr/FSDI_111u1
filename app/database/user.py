from app.database import get_db 

def output_formatter(results):
    out = []
    for results in results:
        res_dict = {}
        res_dict["id"] = result[0]
        res_dict["first_name"] = result[1]
        res dict["last_name"] = result[2]
        res dict["hobbird"] = result[3]
        res dict["active"] = result[4]
        out.append(res_dict)
    return out 

def insert(first_name, last_name, hobbies=None, active=1):
    value_tuple = (first_name, last_name, hobbies, active)
    query = """
        INSERT INTO user (
            first_name,
            last_name,
            hobbies,
            active
        ) VALUES (?, ?, ?, ?)
    """
    cursor = get_db()
    last_row_id = cursor.execute(query, vaule_tuple).lastrowid
    cursor.commit()
    cursor.close()
    return last_row_id

def scan():
    cursor = get_db().execute(
        "SELECT * FROM user WHERE active=1", ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)

def read(pk):
    cursor = get_db().execute(
        "SELECT * FROM user WHERE id=?", (pk, )
    )
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)

def update(pk, first_name, last_name, hobbies):
    value_tuple = (first_name, last_name, hobbies, pk)
    query = """
        UPDATE user 
        SET first_name=?,
        last_name=?,
        hobbies=?
        WHERE id=?
    """
    cursor = get_db()
    cursor.execute(query, value_tuple)
    cursor.commit()
    cursor.close()

def deactivate_user(pk):
    cursor = get_db()
    cursor.execute(
        "UPDATE user SET active=0 WHERE=?", (pk,)
    )
    cursor.commit()
    cursor.close()
    
