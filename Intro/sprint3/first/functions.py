import dis
import functools
import json
from operator import mul, itemgetter, attrgetter, add
from collections import namedtuple
import unicodedata


def factorial(n):
    return functools.reduce(mul, range(1, n + 1))


def get_second_cookie(data):
    return sorted(data['cookies'], key=itemgetter(1))


def indexed_hashes(data):
    return [itemgetter(1, 2)(x) for x in data['cookies']]


def get_nested_https_setting(obj):
    return [attrgetter('cookie', 'domain')(obj.schema)]


nfc = functools.partial(unicodedata.normalize, 'NFC')


class ClearCache:
    def __init__(self, data):
        self.data = dict({'previous_session': data, 'cookies': list()})

    def __call__(self):
        WebSchema = namedtuple('WebSchema', 'domain cookie ttl')
        self.data['previous_session'] = {}
        self.webhook = True
        self.cached = 'version1'
        self.schema = WebSchema('google.com', 'googlecookie', 400)

    def set_custom_cookies(self, domain, *cookies, TTL, **misc):
        self.data['domain'] = domain
        self.data['TTL'] = TTL
        for c in cookies:
            self.data['cookies'].append(c)
        for k, v in misc.items():
            self.data[k] = v

    def set_cookies_http(self, domain, *, TTL):
        self.data['insecure_domain'] = domain
        self.data['insecure_TTL'] = TTL

    def add_sequential(self, device, location, TTL, /, misc):
        self.data['device'] = device
        self.data['location'] = location
        self.data['TTL'] = TTL
        self.data['misc'] = misc


def return_summed_damage():
    return functools.reduce(lambda x, y: x + y, [100, 200, 300])


cat = ['soup', 'lays', 'on', 'my', 'chest']
reverse_cat = sorted(cat, key=lambda x: x[::-1])
for cat in reverse_cat:
    print('Loading next entry to the function: ', cat)

summed_damage = functools.reduce(add, [100, 200, 300])
print(summed_damage)
print(dis.dis(return_summed_damage))

cc = ClearCache(
    {
        'domain': 'example.com',
        'cookies': [
            {
                'name': 'session_id',
                'value': 'abc123',
                'path': '/',
                'expiration': '2023-08-31T23:59:59Z',
                'secure': True,
                'httpOnly': True,
            },
            {
                'name': 'user_id',
                'value': '456',
                'path': '/dashboard',
                'expiration': '2023-09-15T12:00:00Z',
                'secure': True,
                'httpOnly': True,
            },
            {
                'name': 'preferences',
                'value': '{"theme": "dark", "language": "en"}',
                'path': '/',
                'expiration': '2024-06-30T23:59:59Z',
                'secure': True,
                'httpOnly': True,
            },
        ],
    }
)
print(cc.data, callable(cc))
cc()
print(cc.data)
cc.set_custom_cookies(
    'Zalando.dk',
    (1, 'GT4', 65432),
    (2, 'LoggedUser456', 65432),
    (3, 'BasketCookie', 234),
    TTL=40000,
    https=True,
    host='zalando.dk',
)
cc.set_cookies_http('fakezalando.dk', TTL=400)
cc.add_sequential('MacOS Macbook M1', 'DK, CPH', 4000, misc='idk')
print(json.dumps(cc.data, indent=4))
print(factorial(5))
print(get_second_cookie(cc.data))
print(indexed_hashes(cc.data))
print(get_nested_https_setting(cc))
triple = functools.partial(mul, 3)
print(triple(9))
