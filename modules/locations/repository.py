"""Module for create repository for the dni type table."""
from config.database import db
from modules.locations.model import LocationsModel
from modules.locations.schema import (
    LocationsSchema,
)
from modules.province.model import ProvinceModel
from modules.country.model import CountryModel


def find_locations():
    """Function to find all locations."""
    query = (
        db.session.query(
            LocationsModel.name,
            LocationsModel.id,
            LocationsModel.idProvince,
            ProvinceModel.name.label("province_name"),
            CountryModel.name.label("country_name"),
            CountryModel.id.label("idCountry"),
        )
        .join(ProvinceModel, ProvinceModel.id == LocationsModel.idProvince)
        .join(CountryModel, CountryModel.id == ProvinceModel.idCountry)
        .all()
    )
    schema = LocationsSchema().dump(query, many=True)
    return schema


def find_location(id: str, idProvince: str) -> dict:
    """Function to find a localidad."""
    query = (
        db.session.query(
            LocationsModel.name,
            LocationsModel.id,
            LocationsModel.idProvince,
            ProvinceModel.name.label("province_name"),
            CountryModel.name.label("country_name"),
            CountryModel.id.label("idCountry"),
        )
        .join(ProvinceModel, ProvinceModel.id == LocationsModel.idProvince)
        .join(CountryModel, CountryModel.id == ProvinceModel.idCountry)
        .filter(
            LocationsModel.id == id,
            LocationsModel.idProvince == idProvince,
        )
        .first()
    )
    print(query)
    schema = LocationsSchema().dump(query, many=False)
    return schema


def find_exists_location(id: str, idProvince: str) -> dict:
    """Function to find if exists localidad."""
    query = (
        db.session.query(LocationsModel)
        .filter(
            LocationsModel.id == id,
            LocationsModel.idProvince == idProvince,
        )
        .count()
    )
    return query
