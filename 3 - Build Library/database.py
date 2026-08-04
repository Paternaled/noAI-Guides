import sqlite3

def table_create(SQL: str) -> bool:
    con = sqlite3.connect(r"noAI-Guides\3 - Build Library\main.db")
    cursor = con.cursor()

    try: 
        con.execute(SQL)
    except:
        return False
    else:
        return True
    finally:
        cursor.close

def record_add(SQL: str) -> bool:
    con = sqlite3.connect(r"noAI-Guides\3 - Build Library\main.db")
    cursor = con.cursor()

    try: 
        con.execute(SQL)
    except:
        return False
    else:
        return True
    finally:
        cursor.close

def record_edit(SQL: str, item) -> bool:
    con = sqlite3.connect(r"noAI-Guides\3 - Build Library\main.db")
    cursor = con.cursor()

    try: 
        con.execute(SQL, item)
    except:
        return False
    else:
        return True
    finally:
        cursor.close

def record_delete(SQL: str, item: str) -> bool:
    con = sqlite3.connect(r"noAI-Guides\3 - Build Library\main.db")
    cursor = con.cursor()

    try: 
        con.execute(SQL, item)
    except:
        return False
    else:
        return True
    finally:
        cursor.close

def record_lookup(SQL: str, item) -> list:
    con = sqlite3.connect(r"noAI-Guides\3 - Build Library\main.db")
    cursor = con.cursor()

    try:
        result = cursor.execute(SQL, item)

    except:
        result = None
    else:
        result.fetchall()
    finally:
        con.close()
        return result    
