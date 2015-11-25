from django.apps import AppConfig

from netfields.fields import CidrAddressField, InetAddressField
from netfields.lookups import NetContained, NetContains, NetContainedOrEqual, NetContainsOrEquals, InvalidLookup, Family
from netfields.lookups import EndsWith, IEndsWith, StartsWith, IStartsWith, Regex, IRegex


class NetfieldsConfig(AppConfig):
    name = 'netfields'

    try:
        # Django Pre-1.9 stored a list of lookups in default_lookups
        from django.db.models.lookups import default_lookups
        lookups = default_lookups.keys()
    except ImportError:
        # In Django 1.9, these were moved to a series of register function calls on the Field class
        from django.db.models import Field
        lookups = Field.class_lookups.keys()

    for lookup in lookups:
        if lookup not in ['contains', 'startswith', 'endswith', 'icontains', 'istartswith', 'iendswith', 'isnull', 'in',
                         'exact', 'iexact', 'regex', 'iregex', 'lt', 'lte', 'gt', 'gte', 'equals', 'iequals', 'range']:
            invalid_lookup = InvalidLookup
            invalid_lookup.lookup_name = lookup
            CidrAddressField.register_lookup(invalid_lookup)
            InetAddressField.register_lookup(invalid_lookup)

    CidrAddressField.register_lookup(EndsWith)
    CidrAddressField.register_lookup(IEndsWith)
    CidrAddressField.register_lookup(StartsWith)
    CidrAddressField.register_lookup(IStartsWith)
    CidrAddressField.register_lookup(Regex)
    CidrAddressField.register_lookup(IRegex)
    CidrAddressField.register_lookup(NetContained)
    CidrAddressField.register_lookup(NetContains)
    CidrAddressField.register_lookup(NetContainedOrEqual)
    CidrAddressField.register_lookup(NetContainsOrEquals)
    CidrAddressField.register_lookup(Family)

    InetAddressField.register_lookup(EndsWith)
    InetAddressField.register_lookup(IEndsWith)
    InetAddressField.register_lookup(StartsWith)
    InetAddressField.register_lookup(IStartsWith)
    InetAddressField.register_lookup(Regex)
    InetAddressField.register_lookup(IRegex)
    InetAddressField.register_lookup(NetContained)
    InetAddressField.register_lookup(NetContains)
    InetAddressField.register_lookup(NetContainedOrEqual)
    InetAddressField.register_lookup(NetContainsOrEquals)
    InetAddressField.register_lookup(Family)

