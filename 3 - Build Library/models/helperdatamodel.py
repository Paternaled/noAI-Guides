import database.database as __database

def run_startup() -> list:
    result = []

    # TODO - Testing table_exists is done, now I need to create a function that...
    # ...creates a table when it doesn't exist.
    
    for table in table_dict:
        if(__database.table_exists(table_dict[table]["name"]) == False):
            __database.table_create(table_dict[table]["create"])
            if(__database.table_exists(table_dict[table]["name"]) == False): 
                result.append("Table creation - Failed")
            else:
                result.append("Table Created")
        else:
            result.append("True")

    return result


table_dict = {
    "TagT":{
        "name":"TagT",
        "create":"CREATE TABLE TagT (ID INTEGER PRIMARY KEY UNIQUE, Description TEXT, Notes TEXT, IsCategory BOOLEAN DEFAULT 0, IsLegacy BOOLEAN DEFAULT 1, IsActive BOOLEAN DEFAULT 1)",
        "values":["ID","Description","Notes","IsCategory","IsLegacy","IsActive"],
    }, 
    "VillageT":{
        "name":"VillageT",
        "create":"CREATE TABLE VillageT (ID INTEGER PRIMARY KEY UNIQUE, VillageName TEXT, IsLegacy BOOLEAN DEFAULT 0, IsActive BOOLEAN DEFAULT 1)",
        "values":["ID","VillageName","IsLegacy","IsActive"],
    },
    "ClanT":{
        "name":"ClanT",
        "create":"CREATE TABLE ClanT (ID INTEGER PRIMARY KEY UNIQUE, VillageID INTEGER, ClanName TEXT, IsBasic BOOLEAN DEFAULT 0, IsLegacy BOOLEAN DEFAULT 0, IsActive BOOLEAN DEFAULT 1, FOREIGN KEY(VillageID) REFERENCES VillageT(ID))",
        "values":["ID","VillageID","ClanName","IsBasic","IsLegacy","IsActive"],
    },
    "TraitT":{
        "name":"TraitT",
        "create":"CREATE TABLE TraitT (ID INTEGER PRIMARY KEY UNIQUE, Description TEXT, IsPrimary BOOLEAN DEFAULT 0, IsSecondary BOOLEAN DEFAULT 0, IsLegendary BOOLEAN DEFAULT 0, IsLegacy BOOLEAN DEFAULT 0, IsActive BOOLEAN DEFAULT 1)",
        "values":["ID","Description","IsPrimary","IsSecondary","IsLegendary","IsLegacy","IsActive"],
    },
    "TaiStyleT":{
        "name":"TaiStyleT",
        "create":"CREATE TABLE TaiStyleT (ID INTEGER PRIMARY KEY UNIQUE, Description TEXT, IsLegacy BOOLEAN DEFAULT 0, IsActive BOOLEAN DEFAULT 1)",
        "values":["ID","Description","IsLegacy","IsActive"],
    },
    "ElementT":{
        "name":"ElementT",
        "create":"CREATE TABLE ElementT (ID INTEGER PRIMARY KEY UNIQUE, ElementName TEXT, IsFusion BOOLEAN DEFAULT 0, IsLegacy BOOLEAN DEFAULT 0, IsActive BOOLEAN DEFAULT 1)",
        "values":["ID","ElementName","IsFusion","IsLegacy","IsActive"],
    },
    "ProfessionT":{
        "name":"ProfessionT",
        "create":"CREATE TABLE ProfessionT (ID INTEGER PRIMARY KEY UNIQUE, Description TEXT, IsLegacy BOOLEAN DEFAULT 0, IsActive BOOLEAN DEFAULT 1)",
        "values":["ID","Description","Notes","IsLegacy","IsActive"],
    },
    "TransformationT":{
        "name":"TransformationT",
        "create":"CREATE TABLE TransformationT (ID INTEGER PRIMARY KEY UNIQUE, Description TEXT, IsLegacy BOOLEAN DEFAULT 0, IsActive BOOLEAN DEFAULT 1)",
        "values":["ID","Description","Notes","IsLegacy","IsActive"],
    },
    "LegendarySwordT":{
        "name":"LegendarySwordT",
        "create":"CREATE TABLE LegendarySwordT (ID INTEGER PRIMARY KEY UNIQUE, Description TEXT, IsLegacy BOOLEAN DEFAULT 0, IsActive BOOLEAN DEFAULT 1)",
        "values":["ID","Description","Notes","IsLegacy","IsActive"],
    },
}

