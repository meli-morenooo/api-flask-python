"""Module for create repository for the dni type table."""
from config.database import db
from modules.province.model import ProvinceModel
from modules.province.schema import ProvinceSchema, ProvinceCountrySchema
from modules.country.model import CountryModel


def find_provinces():
    """Function to find all provinces."""
    query = db.session.query(ProvinceModel).all()
    schema = ProvinceSchema().dump(query, many=True)
    return schema


def find_provinces_country():
    """Function to find all provinces."""
    query = (
        db.session.query(
            ProvinceModel.name.label("province_name"),
            ProvinceModel.id.label("idProvince"),
            CountryModel.name.label("country_name"),
            CountryModel.id.label("idCountry"),
        )
        .join(CountryModel, CountryModel.id == ProvinceModel.idCountry)
        .all()
    )
    schema = ProvinceCountrySchema().dump(query, many=True)
    return schema


def find_province(id: str, idCountry: str) -> dict:
    """Function to find a province."""
    query = (
        db.session.query(
            ProvinceModel.name.label("province_name"),
            ProvinceModel.id.label("idProvince"),
            CountryModel.name.label("country_name"),
            CountryModel.id.label("idCountry"),
        )
        .join(CountryModel, CountryModel.id == ProvinceModel.idCountry)
        .filter(ProvinceModel.id == id, ProvinceModel.idCountry == idCountry)
        .first()
    )
    schema = ProvinceCountrySchema().dump(query, many=False)
    return schema


def find_exists_province(id: str, idCountry: str) -> dict:
    """Function to find if exists province."""
    query = (
        db.session.query(ProvinceModel)
        .filter(ProvinceModel.id == id, ProvinceModel.idCountry == idCountry)
        .count()
    )
    print(query)
    return query
