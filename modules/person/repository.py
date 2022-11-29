from config.database import db
from modules.country.model import CountryModel
from modules.dni_type.model import DniTypeModel
from modules.gender.model import GenderModel
from modules.locations.model import LocationsModel
from modules.person.model import PersonModel
from modules.person.schema import PersonSchema
from modules.province.model import ProvinceModel


def find_persons():
    """Function to find all person."""
    query = (
        db.session.query(
            PersonModel.name,
            PersonModel.id,
            PersonModel.dni,
            PersonModel.address,
            PersonModel.born,
            PersonModel.phone,
            PersonModel.mail,
            PersonModel.uploadDate,
            PersonModel.active,
            DniTypeModel.name.label("dni_type_name"),
            DniTypeModel.id.label("id_dni_type"),
            GenderModel.id.label("id_gender"),
            GenderModel.name.label("gender_name"),
            LocationsModel.id.label("id_location"),
            LocationsModel.name.label("location_name"),
            ProvinceModel.id.label("id_province"),
            ProvinceModel.name.label("province_name"),
            CountryModel.id.label("id_country"),
            CountryModel.name.label("country_name"),
        )
        .join(DniTypeModel, DniTypeModel.id == PersonModel.idDniTypeUser)
        .join(LocationsModel, LocationsModel.id == PersonModel.idLocation)
        .join(ProvinceModel, ProvinceModel.id == LocationsModel.idProvince)
        .join(CountryModel, CountryModel.id == ProvinceModel.idCountry)
        .join(GenderModel, GenderModel.id == PersonModel.idGender)
        .all()
    )
    schema = PersonSchema().dump(query, many=True)
    return schema


def find_person(id: str) -> dict:
    """Function to find a person."""
    query = (
        db.session.query(
            PersonModel.name,
            PersonModel.id,
            PersonModel.dni,
            PersonModel.address,
            PersonModel.born,
            PersonModel.phone,
            PersonModel.mail,
            PersonModel.uploadDate,
            PersonModel.active,
            DniTypeModel.name.label("dni_type_name"),
            DniTypeModel.id.label("id_dni_type"),
            GenderModel.id.label("id_gender"),
            GenderModel.name.label("gender_name"),
            LocationsModel.id.label("id_location"),
            LocationsModel.name.label("location_name"),
            ProvinceModel.id.label("id_province"),
            ProvinceModel.name.label("province_name"),
            CountryModel.id.label("id_country"),
            CountryModel.name.label("country_name"),
        )
        .join(DniTypeModel, DniTypeModel.id == PersonModel.idDniTypeUser)
        .join(LocationsModel, LocationsModel.id == PersonModel.idLocation)
        .join(ProvinceModel, ProvinceModel.id == LocationsModel.idProvince)
        .join(CountryModel, CountryModel.id == ProvinceModel.idCountry)
        .join(GenderModel, GenderModel.id == PersonModel.idGender)
        .first()
    )
    schema = PersonSchema().dump(query, many=False)
    return schema


def find_exists_person(id: str) -> dict:
    """Function to find if exists person."""
    query = (
        db.session.query(PersonModel).filter(PersonModel.id == id).count()
    )
    return query
