import database as __database

def run_startup() -> list:
    tables = table_list()
    SQL: str = "SELECT name FROM sqlite_master WHERE name=(?)"
    result = []

    i = 0
    for table in tables:
        result.append(__database.table_exists(SQL, tables[i]))
        i = i + 1
        
    return result


def table_list():
    tables = []

    tables.append("TagT")
    tables.append("ClanT")
    tables.append("VillageT")
    tables.append("TraitT")
    tables.append("TaiStyleT")
    tables.append("ElementT")
    tables.append("ClanT")

    return tables
