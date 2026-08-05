import sqlite3

def table_create(SQL: str) -> bool:
    con = sqlite3.connect(r"noAI-Guides\3 - Build Library\main.db")
    cur = con.cursor()

    try: 
        cur.execute(SQL)
    except:
        return False
    else:
        return True
    finally:
        con.close()

def table_exists(SQL: str, data: tuple) -> bool:
    con = sqlite3.connect(r"noAI-Guides\3 - Build Library\main.db")
    cur = con.cursor()

    try: 
       result = cur.execute(SQL, data)
       result_peek = result.fetchone()
    except:
        return False
    else:
        if result_peek is None: 
            return False
        else:
            return True
    finally:
        con.close()

def record_add(SQL: str, data: tuple) -> bool:
    con = sqlite3.connect(r"noAI-Guides\3 - Build Library\main.db")
    cur = con.cursor()

    try: 
        cur.execute(SQL, data)
    except:
        return False
    else:
        con.commit()
        return True
    finally:
        con.close()

def record_edit(SQL: str, data: tuple) -> bool:
    con = sqlite3.connect(r"noAI-Guides\3 - Build Library\main.db")
    cur = con.cursor()

    try: 
        cur.execute(SQL, data)
    except:
        return False
    else:
        con.commit()
        return True
    finally:
        con.close()

def record_delete(SQL: str, data: tuple) -> bool:
    con = sqlite3.connect(r"noAI-Guides\3 - Build Library\main.db")
    cur = con.cursor()

    try: 
        con.execute(SQL, data)
    except:
        return False
    else:
        con.commit()
        return True
    finally:
        con.close()

def record_fetch(SQL: str, data: tuple) -> list:
    con = sqlite3.connect(r"noAI-Guides\3 - Build Library\main.db")
    cur = con.cursor()

    try:
        result = cur.execute(SQL, data)
    except:
        result = None
    else:
        result_peek = result.fetchone()
    finally:
        con.close()
        return result_peek

def record_fetch_all(SQL: str, data: tuple) -> list:
    con = sqlite3.connect(r"noAI-Guides\3 - Build Library\main.db")
    cur = con.cursor()

    try:
        result = cur.execute(SQL, data)
    except:
        result = None
    else:
        result_peek = result.fetchall()
    finally:
        con.close()
        return result_peek
