from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, DecimalField, SelectField, RadioField, FileField, validators, DateField, TimeField

class SignupForm(FlaskForm):
    username = StringField(validators=[validators.DataRequired()])
    password = PasswordField(validators=[validators.DataRequired()])
    superfan = RadioField(choices=[("True", "Yes"), ("False", "No")], validators=[validators.DataRequired()])

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[validators.DataRequired()])
    password = PasswordField("Password", validators=[validators.DataRequired()])

# Capsules

# Cores
class CoresForm(FlaskForm):
    core_id = StringField()
    serial = StringField()
    status = StringField()
    reuse_count = IntegerField()
    block = IntegerField()
    rtls_attempts = IntegerField()
    rtls_landings = IntegerField()
    asds_attempts = IntegerField()
    asds_landings = IntegerField()

# Launches
class LaunchForm(FlaskForm):
    launch_id = StringField()
    name = StringField()
    date = DateField()
    time = TimeField()
    rocket_id = StringField()
    launchpad_id = StringField()
    success = SelectField(choices=[("True", "Yes"), ("False", "No")])
    failure_reason = StringField()
    ship = StringField()
    capsules = StringField()
# Launchpads

# Payloads
class PayloadForm(FlaskForm):
    payload_id = StringField()
    name = StringField()
    type = StringField()
    reused = SelectField(choices=[("True", "Yes"), ("False", "No")])
    manufacturers = StringField()
    mass_kg = IntegerField()
    mass_lb = IntegerField()
    orbit = StringField()
    reference_system = StringField()
    regime = StringField()
# Rockets
class RocketForm(FlaskForm):
    rocket_id = StringField()
    name = StringField()
    type = StringField()
    active = SelectField(choices=[("True", "Active"), ("False", "Decommissioned")])
    country = StringField()
    company = StringField()
class RocketD1Form(FlaskForm):
    rocket_id = StringField()
    stages = IntegerField(validators=[validators.DataRequired()])
    boosters = IntegerField(validators=[validators.DataRequired()])
    cost_per_launch = IntegerField(validators=[validators.DataRequired()])
    landing_legs_number = IntegerField(validators=[validators.DataRequired()])
    landing_legs_material = StringField()
    engine_isp_sea_level = IntegerField(validators=[validators.DataRequired()])
    engine_isp_vacuum = IntegerField(validators=[validators.DataRequired()])
    engine_thrust_sea_level_kN = IntegerField(validators=[validators.DataRequired()])
    engine_thrust_sea_level_lbf = IntegerField(validators=[validators.DataRequired()])
    engine_thrust_vacuum_kN = IntegerField(validators=[validators.DataRequired()])
    engine_thrust_lbf = IntegerField(validators=[validators.DataRequired()])
    engine_number = IntegerField(validators=[validators.DataRequired()])
    engine_type = StringField()
    engine_version = StringField()
    engine_layout = StringField()
    engine_loss_max = IntegerField(validators=[validators.DataRequired()])
    engine_propellant_1 = StringField()
    engine_propellant_2 = StringField()
    engine_thrust_to_weight = DecimalField(validators=[validators.DataRequired()])
class RocketD2Form(FlaskForm):
    rocket_id = StringField()
    height_mt = DecimalField(validators=[validators.DataRequired()])
    height_ft = DecimalField(validators=[validators.DataRequired()])
    diameter_mt = DecimalField(validators=[validators.DataRequired()])
    diameter_ft = DecimalField(validators=[validators.DataRequired()])
    mass_kg = IntegerField(validators=[validators.DataRequired()])
    mass_lb = IntegerField(validators=[validators.DataRequired()])
class RocketImageForm(FlaskForm):
    rocket_id = StringField()
    rocket_image = FileField(validators=[validators.DataRequired()])

# Ships
class ShipForm(FlaskForm):
    ship_id = StringField()
    name = StringField()
    type = StringField()
    active = SelectField(choices=[("True", "Active"),("False", "Deactive")])

class ShipD1Form(FlaskForm):
    ship_id = StringField()
    model = StringField()
    roles = StringField()
    imo = IntegerField()
    mmsi = IntegerField()
    abs = IntegerField()   

class ShipD2Form(FlaskForm):
    ship_id = StringField()
    class_ = DecimalField()
    mass_kg = IntegerField()
    mass_lb = IntegerField()
    year_built = IntegerField()
    home_port = IntegerField()