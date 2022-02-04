import mariadb as db
import dbcreds


def connect_db():
    conn = None
    cursor = None
    try:
        conn = db.connect(user=dbcreds.user, password=dbcreds.password,
                          host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
    except db.OperationalError:
        print("Something is wrong with the DB, please try again in 5 minutes")
    except:
        print("Something went wrong!")
    return conn, cursor


def disconnect_db(conn, cursor):
    try:
        cursor.close()
    except:
        print("The issue with cursor")
    try:
        conn.close()
    except:
        print("The issue with connection")


def attempt_login(username, password):
    user = None
    conn, cursor = connect_db()
    try:
        cursor.execute(
            "select id from owner where username= ? and password= ?", [username, password])
        user = cursor.fetchone()
    except db.OperationalError:
        print("Something is wrong with the DB, please try again in 5 minutes")
    except db.ProgrammingError:
        print("Error running DB query, please file bug report")
    except:
        print("Something went wrong!")
    disconnect_db(conn, cursor)

    if(user == None):
        return False, None
    else:
        return True, user[0]


def list_your_dogs(user_id):
    dogs = []
    conn, cursor = connect_db()
    try:
        cursor.execute(
            "select id, name, description from dog where owner_id=?", [user_id])
        print("Here are your dogs:")
        dogs = cursor.fetchall()
    except db.OperationalError:
        print("Something is wrong with the DB, please try again in 5 minutes")
    except db.ProgrammingError:
        print("Error running DB query, please file bug report")
    except:
        print("Something went wrong!")
    disconnect_db(conn, cursor)
    return dogs
