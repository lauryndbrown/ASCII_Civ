class Citizen:
    """
    Class representing people in a city    
    """
    def __init__(self, happiness=100, health=100):
        self.happiness = happiness
        self.health = health
class Building:
    """
    Class representing buildings in a city
    """
    SAMPLE_TYPE = "sample"
    RESIDENTIAL = "residential"
    FOOD = "food"
    EQUIPMENT = "equipment"
    COMMUNITY = "community"
    def __init__(self, name, building_type=None):
        self.name = name
        if building_type is None:
            self.building_type = Building.SAMPLE_TYPE
        else:
            self.building_type = building_type
class City:
    """
    Class representing cities
    """
    def __init__(self, name, citizens=[], buildings=[]):
        self.name = name
        self.citizens = citizens
        self.buildings = buildings
    def add_citizen(self, citizen):
        if citizen not in self.citizens:
            self.citizens.append(citizen)
    def remove_citizen(self, citizen):
        if citizen in self.citizens:
            self.citizens.remove(citizen)
    def add_building(self, building):
        if building not in self.buildings:
            self.buildings.append(building)
    def remove_building(self, building):
        if building in self.buildings:
            self.buildings.remove(building)
    def num_buildings(self, building_type=None):
        if building_type is None:
            return len(self.buildings)
        count = 0
        for building in self.buildings:
            if building.building_type==building_type:
                count+=1
        return count
class Nation:
    """
    Class representing Nations 
    """
    def __init__(self, name, wealth=100, cities=[]):
        self.name = name
        self.wealth = wealth
        self.cities = cities
    def add_city(self, city):
        if city not in self.cities:
            self.cities.append(city)
    def remove_city(self, city):
        if city in self.city:
            self.cities.remove(city)
    def cities_names(self):
        return [city.name for city in self.cities]
    def __str__(self):
        return "Name: "+self.name+" Wealth:"+str(self.wealth)+"\nCities:"+str(self.cities_names())
