from dataclasses import dataclass


@dataclass
class BuildPlan:
    BuildPlanID: int
    Description: str
    Notes: str
    IsLegacy: bool
    IsActive: bool
    DateCreated: str
    DateUpdated: str

    def __init__(self):
        pass


@dataclass
class Build:
    BuildID: int
    BuildPlanID: int
    Description: str
    VerisonNumber: str
    Notes: str
    IsLegacy: bool
    IsActive: bool
    DateCreated: str
    DateUpdated: str

    def __init__(self):
        pass

@dataclass
class BuildDetail:
    BuildDetailID: int
    ClanID: int
    PrimaryTraitID: int
    SecondaryTraitID: int
    TaiStyleOneID: int
    TaiStyleTwoID: int
    ProfesssionOneID: int
    ProfesssionTwoID: int
    TransformationID: int
    LegendarySwordID: int
    Description: str
    Physical: int
    Capacity: int
    Control: int
    IsProfessional: bool
    Notes: str
    IsActive: bool
    DateCreated: str
    DateUpdated: str

    def __init__(self):
        pass



