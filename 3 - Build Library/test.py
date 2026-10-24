
import sqlite3
import database.schema as schema

#SQL = """CREATE TABLE TagT 
#        (ID INTEGER PRIMARY KEY, 
#        Description TEXT, Note TEXT, 
#        IsCategory BOOLEAN DEFAULT 0, 
#        IsLegacy BOOLEAN DEFAULT 0,
#        IsActive BOOLEAN DEFAULT 1
#        )"""

#def table_exists(SQL: str, data: tuple) -> bool:
#    con = sqlite3.connect(r"noAI-Guides\3 - Build Library\main.db")
#    cur = con.cursor()
#
#    result = cur.execute(SQL, data)
#    result_peek = result.fetchone()
#    if result_peek is None:
#        con.close()
#        return False
#    else:
#        con.close()
#        return True


#SQL = "SELECT name FROM sqlite_master WHERE name=(?)"
#data = [("gravyT",),("TagT",),("asdasdasdasd",)]
#result = []

#i = 0
#for item in data:
#    result.append(table_exists(SQL, data[i]))
#    i = i + 1

#i = 0
#for item in result:
#    print(result[i])
#    i = i + 1



table_name = "test"
test_dict = {"hello":54}
test_dict["world"] = 666

#SQL = ""
#SQL_insert = "INSERT INTO "

#SQL = SQL_insert
#SQL = SQL + table_name + " ("

#loop_stop = len(test_dict)
#i = 1
#for table in test_dict:
#    if i < loop_stop:
#        SQL = SQL + table + ", "
#    else:
#        SQL = SQL + table + ") "
#    i = i + 1

#SQL = SQL + "VALUES ("

#i = 1
#for table in test_dict:
#    if i < loop_stop:
#        SQL = SQL + str(test_dict[table]) + ", "
#    else:
#       SQL = SQL + str(test_dict[table]) + ") "
#    i = i + 1


#print(SQL)

print(schema.BUILDT_CREATE)







