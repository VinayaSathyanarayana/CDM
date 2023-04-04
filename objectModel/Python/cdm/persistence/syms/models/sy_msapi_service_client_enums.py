# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class DDLType(Enum):

    create = "CREATE"
    alter = "ALTER"
    drop = "DROP"


class SASEntityType(Enum):

    database = "DATABASE"
    table = "TABLE"
    schema = "SCHEMA"
    view = "VIEW"
    function = "FUNCTION"
    partitioninfo = "PARTITIONINFO"
    relationship = "RELATIONSHIP"


class SortOrder(Enum):

    desc = "DESC"
    asc = "ASC"


class PublishStatus(Enum):

    published = "PUBLISHED"


class RelationshipType(Enum):

    onetoone = "ONETOONE"
    onetomany = "ONETOMANY"
    manytoone = "MANYTOONE"
    manytomany = "MANYTOMANY"


class TableType(Enum):

    managed = "MANAGED"
    external = "EXTERNAL"


class ValidationType(Enum):

    idw_validation = "IDWValidation"


class ValidationStatus(Enum):

    valid = "VALID"
    invalid = "INVALID"