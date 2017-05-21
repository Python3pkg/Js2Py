from ..base import *
# python 3 support
import six
if six.PY3:
    chr = chr

@Js
def fromCharCode():
    args = arguments.to_list()
    res = ''
    for e in args:
        res +=chr(e.to_uint16())
    return this.Js(res)

fromCharCode.own['length']['value'] = Js(1)

String.define_own_property('fromCharCode', {'value': fromCharCode,
                                         'enumerable': False,
                                         'writable': True,
                                         'configurable': True})

String.define_own_property('prototype', {'value': StringPrototype,
                                         'enumerable': False,
                                         'writable': False,
                                         'configurable': False})

StringPrototype.define_own_property('constructor', {'value': String,
                                                    'enumerable': False,
                                                    'writable': True,
                                                    'configurable': True})