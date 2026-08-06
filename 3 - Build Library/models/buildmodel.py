import database.database as __database

def run_startup() -> list:
    result = []

    # TODO - Testing table_exists is done, now I need to create a function that...
    # ...creates a table when it doesn't exist.
    
    for table in table_dict:
        if(__database.table_exists(table_dict[table]["name"]) == False):
            __database.table_create(table_dict[table]["create"])
            if(__database.table_exists(table_dict[table]["name"]) == False): 
                result.append("Table Creation - Failed")
            else:
                result.append("Table Created")
        else:
            result.append("True")

    return result


table_dict = {
    "BuildPlanT":{
        "name":"BuildPlanT",
        "create":("""CREATE TABLE BuildPlanT (
                    ID INTEGER PRIMARY KEY UNIQUE, 
                    Description TEXT, 
                    Notes TEXT,
                    IsLegacy BOOLEAN DEFAULT 0,
                    IsActive BOOLEAN DEFAULT 1,
                    DateCreated TEXT DEFAULT CURRENT_TIMESTAMP,
                    DateUpdated TEXT DEFAULT CURRENT_TIMESTAMP)
                """),
        "values":["ID","Description","Notes","IsLegacy","IsActive","DateCreated","DateUpdated"],
    }, 
    "BuildT":{
        "name":"BuildT",
        "create":("""CREATE TABLE BuildT (
                    ID INTEGER PRIMARY KEY UNIQUE,
                    BuildPlanID INTEGER, 
                    Description TEXT, 
                    VerisonNumber INTEGER UNIQUE,
                    Notes TEXT,
                    IsLegacy BOOLEAN DEFAULT 0,
                    IsActive BOOLEAN DEFAULT 1,
                    DateCreated TEXT DEFAULT CURRENT_TIMESTAMP,
                    DateUpdated TEXT DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY(BuildPlanID) REFERENCES BuildPlanT(ID))
                """),
        "values":["ID","BuildPlanID","Description","VerisonNumber","Notes","IsLegacy","IsActive","DateCreated","DateUpdated"],
    },
    "BuildDetailT":{
        "name":"BuildDetailT",
        "create":("""CREATE TABLE BuildDetailT (
                    ID INTEGER PRIMARY KEY UNIQUE,
                    BuildID INTEGER,
                    ClanID INTEGER,
                    PrimaryTraitID INTEGER,
                    SecondaryTraitID INTEGER,
                    TaiStyleOneID INTEGER,
                    TaiStyleTwoID INTEGER,
                    ProfessionOneID INTEGER,
                    ProfessionTwoID INTEGER,
                    TransformationID INTEGER, 
                    LegendarySwordID INTEGER, 
                    Description TEXT,
                    Physical INTEGER,
                    Capacity INTEGER,
                    Control INTEGER, 
                    Notes TEXT,
                    IsProfessional BOOLEAN DEFAULT 0,
                    IsLegacy BOOLEAN DEFAULT 0,
                    IsActive BOOLEAN DEFAULT 1,
                    DateCreated TEXT DEFAULT CURRENT_TIMESTAMP,
                    DateUpdated TEXT DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY(BuildID) REFERENCES BuildT(ID),
                    FOREIGN KEY(ClanID) REFERENCES ClanT(ID),
                    FOREIGN KEY(PrimaryTraitID) REFERENCES TraitT(ID),
                    FOREIGN KEY(SecondaryTraitID) REFERENCES TraitT(ID),
                    FOREIGN KEY(TaiStyleOneID) REFERENCES TaiStyleT(ID),
                    FOREIGN KEY(TaiStyleTwoID) REFERENCES TaiStyleT(ID),
                    FOREIGN KEY(ProfessionOneID) REFERENCES ProfessionT(ID),
                    FOREIGN KEY(ProfessionTwoID) REFERENCES ProfessionT(ID),
                    FOREIGN KEY(TransformationID) REFERENCES TransformationT(ID),
                    FOREIGN KEY(LegendarySwordID) REFERENCES LegendarySwordT(ID))
                 """),
        "values":["ID","ClanID","PrimaryTraitID","SecondaryTraitID","TaiStyleOneID","TaiStyleTwoID","ProfessionOneID","ProfessionTwoID","TransformationID","LegendarySwordID","Description","Physical","Capacity","Control","Notes","IsProfessional","IsLegacy","IsActive","DateCreated","DateUpdated"],
    },
}