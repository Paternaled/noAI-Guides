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


table_dict = {
    "BuildPlanT":{
        "name":"BuildPlanT",
        "values":["ID","Description","Notes","IsLegacy","IsActive","DateCreated","DateUpdated"],
        "values_required":["Description","Notes","IsLegacy","IsActive","DateUpdated"],
        "sql_create":("""CREATE TABLE BuildPlanT (
                    ID INTEGER PRIMARY KEY UNIQUE, 
                    Description TEXT, 
                    Notes TEXT,
                    IsLegacy BOOLEAN DEFAULT 0,
                    IsActive BOOLEAN DEFAULT 1,
                    DateCreated TEXT DEFAULT CURRENT_TIMESTAMP,
                    DateUpdated TEXT DEFAULT CURRENT_TIMESTAMP)
                """),
        "sql_add":["""INSERT INTO BuildPlanT (
                    Description, 
                    Notes) VALUES (?, ?)"""],
    }, 
    "BuildT":{
        "name":"BuildT",
        "values":["ID","BuildPlanID","Description","VerisonNumber","Notes","IsLegacy","IsActive","DateCreated","DateUpdated"],
        "values_required":["BuildPlanID","Description","VerisonNumber","Notes","IsLegacy","IsActive","DateUpdated"],
        "sql_create":("""CREATE TABLE BuildT (
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
        "sql_add":["""INSERT INTO BuildT (
                    BuildPlanID, 
                    Description, 
                    VerisonNumber, 
                    Notes) VALUES (?, ?, ?, ?)"""],
    },
    "BuildDetailT":{
        "name":"BuildDetailT",
        "values":["ID","ClanID","PrimaryTraitID","SecondaryTraitID","TaiStyleOneID","TaiStyleTwoID","ProfessionOneID","ProfessionTwoID","TransformationID","LegendarySwordID","Description","Physical","Capacity","Control","Notes","IsProfessional","IsLegacy","IsActive","DateCreated","DateUpdated"],
        "values_required":["ClanID","PrimaryTraitID","SecondaryTraitID","TaiStyleOneID","TaiStyleTwoID","ProfessionOneID","ProfessionTwoID","TransformationID","LegendarySwordID","Description","Physical","Capacity","Control","Notes","IsProfessional","IsLegacy","IsActive","DateUpdated"],
        "sql_create":("""CREATE TABLE BuildDetailT (
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
        "sql_add":["""INSERT INTO BuildDetailT (
                    BuildID,
                    ClanID,
                    PrimaryTraitID,
                    SecondaryTraitID,
                    TaiStyleOneID,
                    TaiStyleTwoID,
                    ProfessionOneID,
                    ProfessionTwoID,
                    TransformationID, 
                    LegendarySwordID, 
                    Description,
                    Physical,
                    Capacity,
                    Control, 
                    Notes,
                    IsProfessional) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""],
    },
}