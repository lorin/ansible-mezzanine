#!/usr/bin/env python
# http://stackoverflow.com/a/15515929/742


def surround_by_quote(a_list):
    return ['"%s"' % an_element for an_element in a_list]


class FilterModule(object):
    def filters(self):
        return {'surround_by_quote': surround_by_quote}
