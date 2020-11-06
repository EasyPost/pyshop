# -*- coding: utf-8 -*-
"""
PyShop Views
"""
from .base import View, RedirectView


class Index(RedirectView):
    """
    PyShop index view.
    """
    redirect_route = u'list_package'


class Health(View):
    def render(self):
        return {'ok': True}
