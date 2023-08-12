from collections import namedtuple
import typing
from datetime import date
import dataclasses
from dataclasses import dataclass, field
import csv
from dis import dis

rocketScheme = namedtuple(
    'Rocket', 'name number launch_date', defaults=['Rocket_', 0, 2020])
newRocketScheme = typing.NamedTuple(
    'NewRocket', [('Organization', str), ('Number', int), ('Launch_date', int)])


class Rocket(rocketScheme):
    @property
    def organization(self):
        return 'ASI' if self.launch_date < 2019 else 'ASIv2'

    def __repr__(self):
        return f"{self.name} {self.number} {self.launch_date} - organized by {self.organization}"

    def check_if_in_db(self):
        if (self.launch_date >= 2020):
            print('Inserting into db')


def read_csv():
    with open("employees.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        Employee = namedtuple("Employee", next(reader), rename=True)
        for row in reader:
            employee = Employee(*row)
            print(employee.name, employee.job, employee.email)


class AstronoutScheme(typing.NamedTuple):
    name: str
    age: int
    married: bool = False

    def __str__(self):
        return f"{self.name} is going to the moon, he/she is {'' if self.married else 'not'} married."


@dataclass
class OrganizationScheme:
    name: str
    established_date: str
    # does not expose field creation because it depends on parameter types, deault_fac provides initial value
    subsidaries: list[str] = field(default_factory=list, repr=False)
    # The default_factory parameter lets you provide a function, class, or any other callable,
    # which will be invoked with zero arguments to build a default value each time an instance of the data class is created.
    # This way, each instance of ClubMember will have its own list—instead of all instances sharing the same list from the class,
    # which is rarely what we want and is often a bug.
    # BUT DATACLASS WILL ONLY THROUGH A ERROR BC OF DEFAULT MUTABLE VALUE FOR LIST,SET,DICT. Anything else should be handled individually.

    def __str__(self):
        return f"{self.name} organization (est. {self.established_date})"


@dataclass
class Visitable_Planet:
    name: str
    size: float
    universe: dataclasses.InitVar(str)
    resources: typing.ClassVar[dict[str, int]] = {}
    # Here ClassVar is a special class defined by the typing module
    # that indicates to the static type checker that this variable should not be set on instances.

    def __post_init__(self, universe):
        print(universe)


class ImmutablePoint:
    x: typing.Final[int]
    y: typing.Final[int]  # Error: final attribute without an initializer

    def __init__(self) -> None:
        self.x = 1  # Good
        self.y = 1  # Good


if __name__ == "__main__":
    astronout1 = AstronoutScheme('Steve', 23, True)
    org_asa = OrganizationScheme('ASA sp. zoo', "2020")
    print(astronout1)
    # astronout1.name = 'Davide' #immutable, namedtuple as well
    print(astronout1._asdict())
    print([f.name for f in dataclasses.fields(OrganizationScheme)])
    print([f.default for f in dataclasses.fields(OrganizationScheme)])
    print("Steve has went through a divorce and came back as a new man/instance")
    astronout11 = astronout1._replace(married=False)
    print(astronout11, astronout11 == astronout1)
    print(typing.get_type_hints(AstronoutScheme))
    print(typing.get_type_hints(astronout11))
    print(
        f"{astronout11.name} second value on the id is {astronout11._fields[1]} and value: {astronout11[1]}")
    incoming_resume = ['Davide', 44]
    print(f'Considering new astronout... {incoming_resume[0]}')
    astronout2 = AstronoutScheme('Davide', 44)
    # rocket = rocketScheme._make(['Rocket ABC'])
    # astronout2 = AstronoutScheme._make(incoming_resume) #defaults do not work with _make from iterables
    print(rocketScheme._field_defaults)
    print("""\nThe difference between creating attributes in classes vs NamedTuple is the annotations creation aspect. 
          In NamedTuple the annotation without the default value is still a gettable attribute of the class - tuplegetter which is a descriptor
          so you can retrieve it without calling (). Interesting enough - describing attribute without the type makes it a plain class attr so its
          not needed when creating an instance. 
          
          For dataclasses it does not create a descriptor for annotation without default value when instantiving a new instance. ANd
          bc its a mutable instance  - regular instances can have their own attributes that don’t appear in the class and changing their class attr
          does not override the general class attribute.\n""")

    ImmutablePoint.x = 2
    p1 = ImmutablePoint()
    print(ImmutablePoint.__dict__)
    print("\n")
    p1.x = 4
    print(p1.__dict__)

    print("\n")
    vp1 = Visitable_Planet('Venus', 123.444, 'Milky Way')
    vp1.resources['food'] = 1000
    Visitable_Planet.resources['water'] = 3000
    for k, v in vp1.resources.items():
        # raw string, formatted using the __repr__ function
        print(f"{k!r} - {v!r}")

    addedRocket = Rocket('Adonis', 1212, 2021)
    addedRocket2 = Rocket('Adonis', 1212, 2021)
    addedRocket.check_if_in_db()
    print(addedRocket == addedRocket2)
    print(dis(addedRocket.check_if_in_db))
