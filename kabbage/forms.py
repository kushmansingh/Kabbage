from wtforms import Form, StringField, IntegerField, SelectField
from wtforms import validators as FV

BUSINESS_TYPES = [
    ('Accounting','Accounting'),
    ('Amusement','Amusement'),
    ('AutoRepair','AutoRepair'),
    ('BusinessServices','BusinessServices'),
    ('Catering','Catering'),
    ('ChildCare','ChildCare'),
    ('ComputerServices','ComputerServices'),
    ('ConsumerGoodsRetailStore','ConsumerGoodsRetailStore'),
    ('ConsumerGoodsOnlineStore','ConsumerGoodsOnlineStore'),
    ('ConsumerGoodsOnlineAndOffline','ConsumerGoodsOnlineAndOffline'),
    ('Construction','Construction'),
    ('Dentists','Dentists'),
    ('DryCleaning','DryCleaning'),
    ('Equipment','Equipment'),
    ('FoodService','FoodService'),
    ('Grocery','Grocery'),
    ('Health','Health'),
    ('HomeRepair','HomeRepair'),
    ('Hotels','Hotels'),
    ('Insurance','Insurance'),
    ('Janitorial','Janitorial'),
    ('Landscape','Landscape'),
    ('Optometrists','Optometrists'),
    ('Physicians','Physicians'),
    ('Restaurants','Restaurants'),
    ('Salons','Salons'),
    ('Taxis','Taxis'),
    ('Trucking','Trucking'),
    ('Veterinarians','Veterinarians')]

class PrequalForm(Form):
    firstName = StringField('First Name', [FV.input_required()])
    lastName = StringField('Last Name', [FV.input_required()])
    emailAddress = StringField('Email', [FV.input_required(), FV.Email()])
    businessName = StringField('Business Name', [FV.input_required()])
    phoneNumber = StringField('Phone Number', [FV.input_required()])
    yearStarted = IntegerField('Year Started', [FV.input_required(), FV.NumberRange(min=0, max=9999)])
    estimatedFICO = IntegerField('Estimated Fico', [FV.input_required()])
    estimatedAnnualRevenue = IntegerField('Estimated revenue', [FV.input_required()])
    grossPercentageFromCards = IntegerField('Gross from credit cards',
        [FV.input_required(), FV.NumberRange(min=0, max=100)])
    typeOfBusiness = SelectField('Business Type', choices=BUSINESS_TYPES)
