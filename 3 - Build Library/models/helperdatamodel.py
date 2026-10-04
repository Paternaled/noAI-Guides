
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
        "values_required":__schema.TAGT_REQUIRED_VALUES_LIST,
        "sql_create":__schema.TAGT_CREATE_Q,
        "sql_add":__schema.TAGT_ADD_Q,
    }, 
    "VillageT":{
        "name":"VillageT",
        "values":["ID","VillageName","IsLegacy","IsActive"],
        "values_required":__schema.VILLAGET_REQUIRED_VALUES_LIST,
        "sql_create":__schema.VILLAGET_CREATE_Q,
        "sql_add":__schema.VILLAGET_ADD_Q,
    },
    "ClanT":{
        "name":"ClanT",
        "values":["ID","VillageID","ClanName","IsBasic","IsLegacy","IsActive"],
        "values_required":__schema.CLANT_REQUIRED_VALUES_LIST,
        "sql_create":__schema.CLANT_CREATE_Q,
        "sql_add":__schema.CLANT_ADD_Q,        
    },
    "TraitT":{
        "name":"TraitT",
        "values":["ID","Description","IsPrimary","IsSecondary","IsLegendary","IsLegacy","IsActive"],
        "values_required":__schema.TRAITT_REQUIRED_VALUES_LIST,
        "sql_create":__schema.TRAITT_CREATE_Q,
        "sql_add":__schema.TRAITT_ADD_Q,
    },
    "TaiStyleT":{
        "name":"TaiStyleT",
        "values":["ID","Description","IsLegacy","IsActive"],
        "values_required":__schema.TAISTYLET_REQUIRED_VALUES_LIST,
        "sql_create":__schema.TAISTYLET_CREATE_Q,
        "sql_add":__schema.TAISTYLET_ADD_Q,
    },
    "ElementT":{
        "name":"ElementT",
        "values":["ID","ElementName","IsFusion","IsLegacy","IsActive"],
        "values_required":__schema.ELEMENTT_REQUIRED_VALUES_LIST,
        "sql_create":__schema.ELEMENTT_CREATE_Q,
        "sql_add":__schema.ELEMENTT_ADD_Q,
    },
    "ProfessionT":{
        "name":"ProfessionT",
        "values":["ID","Description","Notes","IsLegacy","IsActive"],
        "values_required":__schema.PROFESSIONT_REQUIRED_VALUES_LIST,
        "sql_create":__schema.PROFESSIONT_CREATE_Q,
        "sql_add":__schema.PROFESSIONT_ADD_Q,
    },
    "TransformationT":{
        "name":"TransformationT",
        "values":["ID","Description","Notes","IsLegacy","IsActive"],
        "values_required":__schema.TRANSFORMATIONT_REQUIRED_VALUES_LIST,
        "sql_create":__schema.TRANSFORMATIONT_CREATE_Q,
        "sql_add":__schema.TRANSFORMATIONT_ADD_Q,
    },
    "LegendarySwordT":{
        "name":"LegendarySwordT",
        "values":["ID","Description","Notes","IsLegacy","IsActive"],
        "values_required":__schema.LENGENDARYSWORDT_REQUIRED_VALUES_LIST,
        "sql_create":__schema.LENGENDARYSWORDT_CREATE_Q,
        "sql_add":__schema.LENGENDARYSWORDT_ADD_Q,
    },
}

