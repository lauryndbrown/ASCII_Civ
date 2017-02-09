import unittest
from civ_game.civ_display import *
from civ_game.civ_game import *

class CitizenTestCase(unittest.TestCase):
    def setUp(self):
        pass
    def test_init(self):
        citizen = Citizen(50, 50)
        self.assertEqual(citizen.happiness, 50, "initialization not working")
        self.assertEqual(citizen.health, 50, "initialization not working")

class BuildingTestCase(unittest.TestCase):
    def setUp(self):
        self.building = Building("building")
    def test_init(self):
        name = "building_test"
        building = Building(name)
        self.assertEqual(building.name, name, "initialization not working")
        self.assertEqual(building.building_type, Building.SAMPLE_TYPE, "initialization not working")
    def test_get_type_cost(self):
        res = Building.get_type_cost(Building.RESIDENTIAL)
        food = Building.get_type_cost(Building.FOOD)
        equipment = Building.get_type_cost(Building.EQUIPMENT)
        community = Building.get_type_cost(Building.COMMUNITY)
        self.assertEqual(isinstance(res, int), True)
        self.assertEqual(isinstance(food, int), True)
        self.assertEqual(isinstance(equipment, int), True)
        self.assertEqual(isinstance(community, int), True)
    def test_invalid_get_type_cost(self):
        with self.assertRaises(ValueError):
            Building.get_type_cost("xyz")
        
class CityTestCase(unittest.TestCase):
    def setUp(self):
        self.citizens_ary = [Citizen() for _dummy in range(100)]
        self.buildings_ary = [Building(str(i)) for i in range(10)]
        self.city = City("Name",self.citizens_ary,self.buildings_ary)
    def test_init(self):
        self.assertEqual(self.city.name,"Name")
        self.assertEqual(self.city.citizens,self.citizens_ary)
        self.assertEqual(self.city.buildings,self.buildings_ary)
    def test_add_citizen(self):
        citizen = Citizen(25, 25)
        self.assertEqual(citizen in self.city.citizens, False)
        self.city.add_citizen(citizen)
        self.assertEqual(citizen in self.city.citizens, True)
        self.city.add_citizen(citizen)
        #Check there are no duplicates
        self.assertEqual(len(self.city.citizens),len(set(self.city.citizens)))

    def test_remove_citizens(self):
        citizen = Citizen(25, 25)
        self.city.add_citizen(citizen)
        self.assertEqual(citizen in self.city.citizens, True, "Could not add citizen")
        self.city.remove_citizen(citizen)
        self.assertEqual(citizen in self.city.citizens, False, "Citizen removal did not work")
        self.city.remove_citizen(citizen)
        self.assertEqual(citizen in self.city.citizens, False, "Citizen removal did not work")

    def test_add_building(self):
        building = Building(str(len(self.city.buildings)))
        self.assertEqual(building in self.city.buildings, False)
        self.city.add_building(building)
        self.assertEqual(building in self.city.buildings, True)
        self.city.add_citizen(building)
        #Check there are no duplicates
        self.assertEqual(len(self.city.buildings),len(set(self.city.buildings)))
        
    def test_remove_buildings(self):
        building = Building(str(len(self.city.buildings)))
        self.city.add_building(building)
        self.assertEqual(building in self.city.buildings, True, "Could not add builing")
        self.city.remove_building(building)
        self.assertEqual(building in self.city.buildings, False, "Building removal did not work")
        self.city.remove_building(building)
        self.assertEqual(building in self.city.buildings, False, "Building removal did not work")

class NationTestCase(unittest.TestCase):
    def setUp(self):
        self.cities = [City("city1"), City("city2"), City("city3")]
        self.nation = Nation("Nation", 100, self.cities)
    def test_init(self):
        name = "name"
        wealth = 100
        cities = [City("city1"), City("city2")]
        nation = Nation(name,wealth,cities)
        self.assertEqual(name, nation.name)
        self.assertEqual(wealth, nation.wealth)
        self.assertEqual(cities, nation.cities)
    def test_add_building(self):
        nation = Nation("nation", 1000)
        city = City("city")
        nation.cities.append(city)
        nation.add_building(city, Building.FOOD)
        nation.add_building(city, Building.RESIDENTIAL)
        nation.add_building(city, Building.EQUIPMENT)
        nation.add_building(city, Building.COMMUNITY)
        
        self.assertEqual(city.buildings[0].building_type, Building.FOOD)
        self.assertEqual(city.buildings[1].building_type, Building.RESIDENTIAL)
        self.assertEqual(city.buildings[2].building_type, Building.EQUIPMENT)
        self.assertEqual(city.buildings[3].building_type, Building.COMMUNITY)

    def test_add_building_funds(self):
        nation = Nation("nation", 100)
        city = City("city")
        nation.cities.append(city)
        nation.add_building(city, Building.FOOD)
        
        self.assertEqual(100 > nation.wealth, True)
    
    def test_add_building_insufficent(self):
        cost = Building.get_type_cost(Building.COMMUNITY)
        nation = Nation("nation", cost)
        city = City("city")
        nation.cities.append(city)
        result1 = nation.add_building(city, Building.COMMUNITY)
        self.assertEqual(result1, True)
        self.assertEqual(nation.wealth, 0)
        result2 = nation.add_building(city, Building.COMMUNITY)
        self.assertEqual(result2, False)
        
        
class CivPlayerTestCase(unittest.TestCase):
    def setUp(self):
        pass
    def test_init(self):
        self.assertEqual(True, True, "IDEK")

class CivGameTestCase(unittest.TestCase):
    def setUp(self):
        pass
    def test_init(self):
        self.assertEqual(True, True, "IDEK")
