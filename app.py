from flask import Flask
from flask_migrate import Migrate

from config import database, schema
from modules.country.controller import country_bp
from modules.dni_type.controller import dni_type_bp
from modules.gender.controller import gender_bp
from modules.province.controller import province_bp
from modules.user_type.controller import user_type_bp
from modules.locations.controller import locations_bp
from modules.person.controller import person_bp
from modules.user.controller import user_bp
import os

app = Flask(__name__)
# app.config['MYSQL_HOST'] = '143.198.156.171'
# app.config['MYSQL_USER'] = 'BD2021'
# app.config['MYSQL_PASSWORD'] = 'BD2021itec'
# app.config['MYSQL_DB'] = 'python_efi_mar_pal_sch'
MYSQL_HOST = os.environ.get('MYSQL_HOST', '143.198.156.171') 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://BD2021:BD2021itec@'+MYSQL_HOST+'/python_efi_mar_pal_sch'
app.config["SECRET_KEY"] = "acalepongoloquequiera"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["pydev_do_not_trace"] = True

database.init_app(app)
schema.init_app(app)

migrate = Migrate(app, database.db)
from modules.country.model import CountryModel
from modules.dni_type.model import DniTypeModel
from modules.gender.model import GenderModel
from modules.province.model import ProvinceModel
from modules.user_type.model import UserTypeModel
from modules.locations.model import LocationsModel
from modules.person.model import PersonModel
from modules.user.model import UserModel

# Register blueprints
app.register_blueprint(country_bp, url_prefix="/countries")
app.register_blueprint(dni_type_bp, url_prefix="/dni_type")
app.register_blueprint(gender_bp, url_prefix="/gender")
app.register_blueprint(province_bp, url_prefix="/province")
app.register_blueprint(user_type_bp, url_prefix="/user_type")
app.register_blueprint(locations_bp, url_prefix="/locations")
app.register_blueprint(person_bp, url_prefix="/person")
app.register_blueprint(user_bp, url_prefix="/user")

if __name__ == "__main":
    app.run(debug=True)
