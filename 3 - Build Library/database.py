import sqlite3

def table_create(SQL: str) -> bool:
    con = sqlite3.connect(r"noAI-Guides\3 - Build Library\main.db")
    cur = con.cursor()

    try: 
        cur.execute(SQL)
    except:
        return False
    else:
        con.commit()
        return True
    finally:
        con.close()

# FIXME - This is currently returning all True values lol
def table_exists(SQL: str, data) -> bool:
    con = sqlite3.connect(r"noAI-Guides\3 - Build Library\main.db")
    cur = con.cursor()

    try: 
       result = cur.execute(SQL, data[0])
       result.fetchone()
    except:
        return False
    else:
        if result == None: 
            return False
        else:
            return True
    finally:
        con.close()

def record_add(SQL: str, data) -> bool:
    con = sqlite3.connect(r"noAI-Guides\3 - Build Library\main.db")
    cur = con.cursor()

    try: 
        cur.execute(SQL, data[0])
    except:
        return False
    else:
        con.commit()
        return True
    finally:
        con.close()

def record_edit(SQL: str, data) -> bool:
    con = sqlite3.connect(r"noAI-Guides\3 - Build Library\main.db")
    cur = con.cursor()

    try: 
        cur.execute(SQL, data[0])
    except:
        return False
    else:
        con.commit()
        return True
    finally:
        con.close()

def record_delete(SQL: str, data) -> bool:
    con = sqlite3.connect(r"noAI-Guides\3 - Build Library\main.db")
    cur = con.cursor()

    try: 
        con.execute(SQL, data[0])
    except:
        return False
    else:
        con.commit()
        return True
    finally:
        con.close()

def record_fetch(SQL: str, data) -> list:
    con = sqlite3.connect(r"noAI-Guides\3 - Build Library\main.db")
    cur = con.cursor()

    try:
        result = cur.execute(SQL, data[0])
    except:
        result = None
    else:
        result.fetchone()
    finally:
        con.close()
        return result

def record_fetch_all(SQL: str, data) -> list:
    con = sqlite3.connect(r"noAI-Guides\3 - Build Library\main.db")
    cur = con.cursor()

    try:
        result = cur.execute(SQL, data)
    except:
        result = None
    else:
        result.fetchall()
    finally:
        con.close()
        return result
