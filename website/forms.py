from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, DecimalField, SelectField, validators

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[validators.DataRequired()])
    password = PasswordField("Password", validators=[validators.DataRequired()])

# Capsules

# Cores

# Launches

# Launchpads

# Payloads

# Rockets
class RocketForm(FlaskForm):
    rocket_id = StringField
    name = StringField
    type = StringField
    active = SelectField
    country = StringField
    company = StringField
class RocketD1Form(FlaskForm):
    rocket_id = StringField
    stages = IntegerField
    boosters = IntegerField
    cost_per_launch = IntegerField
    landing_legs_number = IntegerField
    landing_legs_material = StringField
    engine_isp_sea_level = IntegerField
    engine_isp_vacuum = IntegerField
    engine_thrust_sea_level_kN = IntegerField
    engine_thrust_sea_level_lbf = IntegerField
    engine_thrust_vacuum_kN = IntegerField
    engine_thrust_lbf = IntegerField
    engine_number = IntegerField
    engine_type = StringField
    engine_version = StringField
    engine_layout = StringField
    engine_loss_max = IntegerField
    engine_propellant_1 = StringField
    engine_propellant_2 = StringField
    engine_thrust_to_weight = DecimalField
class RocketD2Form(FlaskForm):
    rocket_id = StringField
    height_mt = DecimalField
    height_ft = DecimalField
    diameter_mt = DecimalField
    diameter_ft = DecimalField
    mass_kg = IntegerField
    mass_lb = IntegerField

# Ships

