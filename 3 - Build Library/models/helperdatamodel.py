
import database.database as __database

def run_startup() -> list:
    result = []
    
    for table in table_dict:
        if(__database.table_exists(table_dict[table]["name"]) == False):
            __database.table_create(table_dict[table]["sql_create"])
            if(__database.table_exists(table_dict[table]["name"]) == False): 
                result.append("Table Creation - Failed")
            else:
                result.append("Table Created")
        else:
            result.append("True")

    return result

def verify_values_new(table_name: str, value_list: list):
    pass

def verify_values_update(table_name: str, value_list: list):
    pass

def values_add(table_name: str, value_list: list):
    pass

def values_edit(table_name: str, value_list: list):
    pass


def table_list() -> list:
    result = []
    i = 0
    for table in table_dict:
        result.append(table_dict[table]["name"])
        i = i + 1

    return result
    
table_dict = {
    "TagT":{
        "name":"TagT",
        "values":["ID","Description","Notes","IsCategory","IsLegacy","IsActive"],
        "values_required":["Description","Notes","IsCategory","IsLegacy"],
        "sql_create":"CREATE TABLE TagT (ID INTEGER PRIMARY KEY UNIQUE, Description TEXT, Notes TEXT, IsCategory BOOLEAN DEFAULT 0, IsLegacy BOOLEAN DEFAULT 1, IsActive BOOLEAN DEFAULT 1)",
        "sql_add":["INSERT INTO TagT (Description, Notes, IsCategory) VALUES (?, ?, ?)"],
    }, 
    "VillageT":{
        "name":"VillageT",
        "values":["ID","VillageName","IsLegacy","IsActive"],
        "values_required":["VillageName","IsLegacy"],
        "sql_create":"CREATE TABLE VillageT (ID INTEGER PRIMARY KEY UNIQUE, VillageName TEXT, IsLegacy BOOLEAN DEFAULT 0, IsActive BOOLEAN DEFAULT 1)",
        "sql_add":["INSERT INTO TagT (Description, Notes, IsCategory) VALUES (?, ?)"],
    },
    "ClanT":{
        "name":"ClanT",
        "values":["ID","VillageID","ClanName","IsBasic","IsLegacy","IsActive"],
        "values_required":["VillageID","ClanName","IsBasic","IsLegacy"],
        "sql_create":"CREATE TABLE ClanT (ID INTEGER PRIMARY KEY UNIQUE, VillageID INTEGER, ClanName TEXT, IsBasic BOOLEAN DEFAULT 0, IsLegacy BOOLEAN DEFAULT 0, IsActive BOOLEAN DEFAULT 1, FOREIGN KEY(VillageID) REFERENCES VillageT(ID))",
        "sql_add":["VillageID","ClanName","IsBasic","IsLegacy"],        
    },
    "TraitT":{
        "name":"TraitT",
        "values":["ID","Description","IsPrimary","IsSecondary","IsLegendary","IsLegacy","IsActive"],
        "values_required":["Description","IsPrimary","IsSecondary","IsLegendary","IsLegacy"],
        "sql_create":"CREATE TABLE TraitT (ID INTEGER PRIMARY KEY UNIQUE, Description TEXT, IsPrimary BOOLEAN DEFAULT 0, IsSecondary BOOLEAN DEFAULT 0, IsLegendary BOOLEAN DEFAULT 0, IsLegacy BOOLEAN DEFAULT 0, IsActive BOOLEAN DEFAULT 1)",
        "sql_add":["Description","IsPrimary","IsSecondary","IsLegendary","IsLegacy"],
    },
    "TaiStyleT":{
        "name":"TaiStyleT",
        "values":["ID","Description","IsLegacy","IsActive"],
        "values_required":["Description","IsLegacy"],
        "sql_create":"CREATE TABLE TaiStyleT (ID INTEGER PRIMARY KEY UNIQUE, Description TEXT, IsLegacy BOOLEAN DEFAULT 0, IsActive BOOLEAN DEFAULT 1)",
        "sql_add":["Description","IsLegacy"],
    },
    "ElementT":{
        "name":"ElementT",
        "values":["ID","ElementName","IsFusion","IsLegacy","IsActive"],
        "values_required":["ElementName","IsFusion","IsLegacy"],
        "sql_create":"CREATE TABLE ElementT (ID INTEGER PRIMARY KEY UNIQUE, ElementName TEXT, IsFusion BOOLEAN DEFAULT 0, IsLegacy BOOLEAN DEFAULT 0, IsActive BOOLEAN DEFAULT 1)",
        "sql_add":["ElementName","IsFusion","IsLegacy"],
    },
    "ProfessionT":{
        "name":"ProfessionT",
        "values":["ID","Description","Notes","IsLegacy","IsActive"],
        "values_required":["Description","Notes","IsLegacy"],
        "sql_create":"CREATE TABLE ProfessionT (ID INTEGER PRIMARY KEY UNIQUE, Description TEXT, IsLegacy BOOLEAN DEFAULT 0, IsActive BOOLEAN DEFAULT 1)",
        "sql_add":["Description","Notes","IsLegacy"],
    },
    "TransformationT":{
        "name":"TransformationT",
        "values":["ID","Description","Notes","IsLegacy","IsActive"],
        "values_required":["Description","Notes","IsLegacy"],
        "sql_create":"CREATE TABLE TransformationT (ID INTEGER PRIMARY KEY UNIQUE, Description TEXT, IsLegacy BOOLEAN DEFAULT 0, IsActive BOOLEAN DEFAULT 1)",
        "sql_add":["Description","Notes","IsLegacy"],
    },
    "LegendarySwordT":{
        "name":"LegendarySwordT",
        "values":["ID","Description","Notes","IsLegacy","IsActive"],
        "values_required":["Description","Notes","IsLegacy"],
        "sql_create":"CREATE TABLE LegendarySwordT (ID INTEGER PRIMARY KEY UNIQUE, Description TEXT, IsLegacy BOOLEAN DEFAULT 0, IsActive BOOLEAN DEFAULT 1)",
        "sql_add":["Description","Notes","IsLegacy"],
    },
}

