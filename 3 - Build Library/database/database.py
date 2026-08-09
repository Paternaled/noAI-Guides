import sqlite3
import utility.utility as utility

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

def table_exists(table_name: str) -> bool:
    con = sqlite3.connect(r"noAI-Guides\3 - Build Library\main.db")
    cur = con.cursor()

    table_name_converted: tuple = utility.convert_tuple(table_name)
    SQL = "SELECT name FROM sqlite_master WHERE name=(?)"

    try: 
       result = cur.execute(SQL, table_name_converted)
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

def record_add(SQL: str, data: list) -> bool:
    con = sqlite3.connect(r"noAI-Guides\3 - Build Library\main.db")
    cur = con.cursor()

    data_converted: tuple = utility.convert_tuple_many(data)

    try: 
        cur.execute(SQL, data_converted)
    except:
        return False
    else:
        con.commit()
        return True
    finally:
        con.close()

def record_edit(SQL: str, data: list) -> bool:
    con = sqlite3.connect(r"noAI-Guides\3 - Build Library\main.db")
    cur = con.cursor()

    data_converted: tuple = utility.convert_tuple_many(data)

    try: 
        cur.execute(SQL, data_converted)
    except:
        return False
    else:
        con.commit()
        return True
    finally:
        con.close()

def record_delete(SQL: str, data: str) -> bool:
    con = sqlite3.connect(r"noAI-Guides\3 - Build Library\main.db")
    cur = con.cursor()

    data_converted: tuple = utility.convert_tuple(data)

    try: 
        con.execute(SQL, data_converted)
    except:
        return False
    else:
        con.commit()
        return True
    finally:
        con.close()

def record_fetch(SQL: str, data: str) -> list:
    con = sqlite3.connect(r"noAI-Guides\3 - Build Library\main.db")
    cur = con.cursor()

    data_converted: tuple = utility.convert_tuple(data)

    try:
        result = cur.execute(SQL, data_converted)
    except:
        result = None
    else:
        result_peek = result.fetchone()
    finally:
        con.close()
        return result_peek

def record_fetch_all(SQL: str, data: str) -> list:
    con = sqlite3.connect(r"noAI-Guides\3 - Build Library\main.db")
    cur = con.cursor()

    data_converted: tuple = utility.convert_tuple(data)

    try:
        result = cur.execute(SQL, data_converted)
    except:
        result = None
    else:
        result_peek = result.fetchall()
    finally:
        con.close()
        return result_peek
