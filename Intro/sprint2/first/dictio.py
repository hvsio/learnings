from collections import defaultdict, ChainMap
import string
from types import MappingProxyType

data = {
    'chair': {
        'material': 'wood',
        'color': 'brown',
        'price': 89.99,
        'dimensions': {
            'height': 90,
            'width': 60,
            'depth': 50
        }
    },
    'table': {
        'material': 'glass',
        'color': 'transparent',
        'price': 199.99,
        'dimensions': {
            'height': 75,
            'width': 120,
            'depth': 80
        }
    },
    'sofa': {
        'material': 'leather',
        'color': 'black',
        'price': 599.99,
        'dimensions': {
            'height': 85,
            'width': 200,
            'depth': 90
        }
    }
}

furniture_dict = {
    'chair': {
        'material': 'aint wood',
    },
}

class Furniture:
    def __init__(self, name='', type='', brand=''):
        self.name = name
        self.type = type
        self.brand = brand

class Utils:
    d1 = data
    region = 'Sweden'

    @classmethod
    def update(cls, d2): #overriding the entires value no matter if its a nested dict
        return cls.d1 | d2
    
    @classmethod
    def get_details(cls):
        match cls.d1:
            case {'chair': {'material': 'wood', **dims}}:
                print(dims)

    @classmethod
    def pop_newest_product(cls):
        prods_reversed = cls.d1.__reversed__()
        print(prods_reversed)
        return next(prods_reversed)
    
    @classmethod
    def import_item(cls, item):
        match item:
            case {'bed': {'collection': 'aloha', **dims}}:
                cls.d1.__setitem__(list(item.keys())[0], list(item.values())[0]) #A view object is a dynamic proxy

    @classmethod
    def introduce_prototype(cls, name, launch_date):
        cls.d1.setdefault(name, []).append(launch_date)
        print(cls.d1)

    @classmethod
    def merge_warehouses(cls, d2, appendix):
        merged_db = ChainMap({}, d2)
        match cls.region:
            case 'Sweden':
                print('Setting up subcontext to Sweden')
                merged_db = merged_db.new_child(cls.d1)
                print(merged_db)
            case _:
                #updating does not respect prioritizing dicts, the new one always prevails
                merged_db.update(cls.d1)
                print('Updating the furniture with other warehouses\nDropping the mutable one as its handled in Sweden')
                merged_db = merged_db.parents()
                print(merged_db)

        if "manual changes":
            lists = merged_db.maps
            print(lists)
            print(f'Furniture bound to change/mutable vars: {lists[0]}')
            lists.append({'fixed_furniture': appendix})
            print(merged_db)
        return merged_db.maps[0] #return the first one/mutable one
    
    @classmethod
    def create_warehouse_config(cls):
        defaults = {'latitude': (111,222), 'headquarters': 'Malmo, sweden'}
        d = MappingProxyType(defaults)
        if "latitude seems correct":
            print(f"Sending location: {d['headquarters']}")
        if "there is more to it":
            defaults['ceo'] = "somebody"
            #cannot modify the proxy but u can the underlying structure, ref
            print(f"Updating the db with new info about ceo: {d['ceo']}")



    
        


if __name__ == '__main__':
    utils = Utils
    print(Utils.update(furniture_dict))
    Utils.get_details()
    x = {'a': 'a', 'b': 'b', 'c': 'c'}.fromkeys(['key1', 'key2'], 1)
    # calling from keys on dict does not respect neither key, values or length of the dict object being called on
    print(x)
    print(f"The newest model in Ikea is {Utils.pop_newest_product()}")
    Utils.import_item({'bed': {
        'material': 'wood',
        'color': 'black',
        'price': 599.99,
        'dimensions': {
            'height': 85,
            'width': 200,
            'depth': 90
        },
        'collection': 'aloha',

    }})
    Utils.introduce_prototype('Armchair', 'TBC 12.12.2028')

    print("Presenting what can be bought from upcoming catalog by months")
    catalog = defaultdict(Furniture)
    catalog['03'] = Furniture('SKOVV', 'bedside table', 'IKEA')
    print(catalog['03'])
    cm = ChainMap(data, furniture_dict, catalog)
    print(cm['03'])
    Utils.merge_warehouses(catalog, 'some stool')
    conversation = "I would like to buy $furniture made out of $material, do you have it in $country?"
    template = string.Template(conversation)
    template.substitute(furniture="bed", material="wood", country="Denmark")
    print(template)
    Utils.create_warehouse_config()
