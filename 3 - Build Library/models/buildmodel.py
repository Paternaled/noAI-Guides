
import database.database as __database
import database.schema as __schema

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
        "sql_create":__schema.BUILDPLANT_CREATE_Q,
        "sql_add": __schema.BUILDPLANT_ADD_Q,
    }, 
    "BuildT":{
        "name":"BuildT",
        "values":["ID","BuildPlanID","Description","VerisonNumber","Notes","IsLegacy","IsActive","DateCreated","DateUpdated"],
        "values_required":["BuildPlanID","Description","VerisonNumber","Notes","IsLegacy","IsActive","DateUpdated"],
        "sql_create":__schema.BUILDT_CREATE_Q,
        "sql_add":__schema.BUILDT_ADD_Q,
    },
    "BuildDetailT":{
        "name":"BuildDetailT",
        "values":["ID","ClanID","PrimaryTraitID","SecondaryTraitID","TaiStyleOneID","TaiStyleTwoID","ProfessionOneID","ProfessionTwoID","TransformationID","LegendarySwordID","Description","Physical","Capacity","Control","Notes","IsProfessional","IsLegacy","IsActive","DateCreated","DateUpdated"],
        "values_required":["ClanID","PrimaryTraitID","SecondaryTraitID","TaiStyleOneID","TaiStyleTwoID","ProfessionOneID","ProfessionTwoID","TransformationID","LegendarySwordID","Description","Physical","Capacity","Control","Notes","IsProfessional","IsLegacy","IsActive","DateUpdated"],
        "sql_create":__schema.BUILDDETAILT_CREATE_Q,       
        "sql_add":__schema.BUILDDETAILT_ADD_Q,
    },
}