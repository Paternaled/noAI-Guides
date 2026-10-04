

BUILDPLANT_CREATE_Q = """CREATE TABLE BuildPlanT (
                    ID INTEGER PRIMARY KEY UNIQUE, 
                    Description TEXT, 
                    Notes TEXT,
                    IsLegacy BOOLEAN DEFAULT 0,
                    IsActive BOOLEAN DEFAULT 1,
                    DateCreated TEXT DEFAULT CURRENT_TIMESTAMP,
                    DateUpdated TEXT DEFAULT CURRENT_TIMESTAMP)
                """
BUILDPLANT_ADD_Q = """INSERT INTO BuildPlanT (
                    Description, 
                    Notes) VALUES (?, ?)"""
BUILDPLANT_REQUIRED_VALUES_Q = ""

BUILDT_CREATE_Q = """CREATE TABLE BuildT (
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
                """
BUILDT_ADD_Q = """INSERT INTO BuildT (
                    BuildPlanID, 
                    Description, 
                    VerisonNumber, 
                    Notes) VALUES (?, ?, ?, ?)"""
BUILDT_REQUIRED_VALUES_Q = ""

BUILDDETAILT_CREATE_Q = """CREATE TABLE BuildDetailT (
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
                 """
BUILDDETAILT_ADD_Q = """INSERT INTO BuildDetailT (
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
                    IsProfessional) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
BUILDDETAILT_REQUIRED_VALUES_Q = ""

TAGT_CREATE_Q = "CREATE TABLE TagT (ID INTEGER PRIMARY KEY UNIQUE, Description TEXT, Notes TEXT, IsCategory BOOLEAN DEFAULT 0, IsLegacy BOOLEAN DEFAULT 1, IsActive BOOLEAN DEFAULT 1)"
TAGT_ADD_Q = "INSERT INTO TagT (Description, Notes, IsCategory) VALUES (?, ?, ?)"
TAGT_REQUIRED_VALUES_LIST = ["Description","Notes","IsCategory","IsLegacy"]

VILLAGET_CREATE_Q = "CREATE TABLE VillageT (ID INTEGER PRIMARY KEY UNIQUE, VillageName TEXT, IsLegacy BOOLEAN DEFAULT 0, IsActive BOOLEAN DEFAULT 1)"
VILLAGET_ADD_Q = "INSERT INTO VillageT (Description, Notes, IsCategory) VALUES (?, ?, ?)"
VILLAGET_REQUIRED_VALUES_LIST = ["VillageName","IsLegacy"]

CLANT_CREATE_Q = "CREATE TABLE ClanT (ID INTEGER PRIMARY KEY UNIQUE, VillageID INTEGER, ClanName TEXT, IsBasic BOOLEAN DEFAULT 0, IsLegacy BOOLEAN DEFAULT 0, IsActive BOOLEAN DEFAULT 1, FOREIGN KEY(VillageID) REFERENCES VillageT(ID))"
CLANT_ADD_Q = "INSERT INTO ClanT (Description, Notes, IsCategory) VALUES (?, ?, ?)"
CLANT_REQUIRED_VALUES_LIST = ["VillageID","ClanName","IsBasic","IsLegacy"]

TRAITT_CREATE_Q = "CREATE TABLE TraitT (ID INTEGER PRIMARY KEY UNIQUE, Description TEXT, IsPrimary BOOLEAN DEFAULT 0, IsSecondary BOOLEAN DEFAULT 0, IsLegendary BOOLEAN DEFAULT 0, IsLegacy BOOLEAN DEFAULT 0, IsActive BOOLEAN DEFAULT 1)"
TRAITT_ADD_Q = "INSERT INTO TraitT (Description, Notes, IsCategory) VALUES (?, ?, ?)"
TRAITT_REQUIRED_VALUES_LIST = ["Description","IsPrimary","IsSecondary","IsLegendary","IsLegacy"]

TAISTYLET_CREATE_Q = "CREATE TABLE TaiStyleT (ID INTEGER PRIMARY KEY UNIQUE, Description TEXT, IsLegacy BOOLEAN DEFAULT 0, IsActive BOOLEAN DEFAULT 1)"
TAISTYLET_ADD_Q = "INSERT INTO TaiStyleT (Description, Notes, IsCategory) VALUES (?, ?, ?)"
TAISTYLET_REQUIRED_VALUES_LIST = ["Description","IsLegacy"]

ELEMENTT_CREATE_Q = "CREATE TABLE ElementT (ID INTEGER PRIMARY KEY UNIQUE, ElementName TEXT, IsFusion BOOLEAN DEFAULT 0, IsLegacy BOOLEAN DEFAULT 0, IsActive BOOLEAN DEFAULT 1)"
ELEMENTT_ADD_Q = "INSERT INTO ElementT (ElementName, IsFusion, IsCategory) VALUES (?, ?, ?)"
ELEMENTT_REQUIRED_VALUES_LIST = ["ElementName","IsFusion","IsLegacy"]

PROFESSIONT_CREATE_Q = "CREATE TABLE ProfessionT (ID INTEGER PRIMARY KEY UNIQUE, Description TEXT, IsLegacy BOOLEAN DEFAULT 0, IsActive BOOLEAN DEFAULT 1)"
PROFESSIONT_ADD_Q = "INSERT INTO ProfessionT (Description) VALUES (?)"
PROFESSIONT_REQUIRED_VALUES_LIST = ["Description"]

TRANSFORMATIONT_CREATE_Q = "CREATE TABLE TransformationT (ID INTEGER PRIMARY KEY UNIQUE, Description TEXT, IsLegacy BOOLEAN DEFAULT 0, IsActive BOOLEAN DEFAULT 1)"
TRANSFORMATIONT_ADD_Q = "INSERT INTO TransformationT (Description) VALUES (?)"
TRANSFORMATIONT_REQUIRED_VALUES_LIST = ["Description"]

LENGENDARYSWORDT_CREATE_Q = "CREATE TABLE LegendarySwordT (ID INTEGER PRIMARY KEY UNIQUE, Description TEXT, IsLegacy BOOLEAN DEFAULT 0, IsActive BOOLEAN DEFAULT 1)"
LENGENDARYSWORDT_ADD_Q = "INSERT INTO LegendarySwordT (Description) VALUES (?)"
LENGENDARYSWORDT_REQUIRED_VALUES_LIST = ["Description"]
