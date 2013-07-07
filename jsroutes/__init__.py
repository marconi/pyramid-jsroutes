# -*- coding: utf-8 -*-

__title__ = 'jsroutes'
__version__ = '0.1.2'
__author__ = 'Marconi Moreto'


def includeme(config):
    from pyramid.events import NewRequest, BeforeRender
    from .subscribers import inspect_routes, attach_routes

    config.add_subscriber(inspect_routes, NewRequest)
    config.add_subscriber(attach_routes, BeforeRender)
