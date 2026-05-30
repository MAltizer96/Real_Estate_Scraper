class DataModel():
    zpid: int
    name: str
    value: float
    def __init__(self, id: int, name: str, value: float):
        self.id = id
        self.name = name
        self.value = value

class PropertyIdentity():
    zpid: int
    address: str
    city: str
    state: str
    zip_code: str
    def __init__(self, zpid: int, address: str, city: str, state: str, zip_code: str):
        self.zpid = zpid
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code

class PropertyDetails():
    zpid: int
    status: str
    year_built: int
    lot_size_sqft: int
    finished_sqft: int
    bathrooms: float
    bedrooms: int
    def __init__(self, zpid: int, year_built: int, lot_size_sqft: int, finished_sqft: int, bathrooms: float, bedrooms: int, status: str):
        self.zpid = zpid
        self.status = status
        self.year_built = year_built
        self.lot_size_sqft = lot_size_sqft
        self.finished_sqft = finished_sqft
        self.bathrooms = bathrooms
        self.bedrooms = bedrooms

class PropertyValuation():
    zpid: int
    estimated_value: float
    last_valuation_date: str
    tax_assessment: float
    def __init__(self, zpid: int, estimated_value: float, last_valuation_date: str, tax_assessment: float):
        self.zpid = zpid
        self.tax_assessment = tax_assessment
        self.estimated_value = estimated_value
        self.last_valuation_date = last_valuation_date


