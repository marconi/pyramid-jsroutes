import re
from mako.template import Template

from pyramid.interfaces import IRoutesMapper
from pyramid.threadlocal import get_current_request

from .utils import asbool


def inspect_routes(event):
    """ Fetch all routes, normalize, render then attach to request. """

    # retrieve cached routes from registry and depending
    # on the settings, reload the routes.
    registry = event.request.registry
    reload_routes = asbool(registry.settings.get('jsroutes.reload_routes', False))
    routes = getattr(event.request.registry, '_routes', None)
    if routes and not reload_routes:
        return

    mapper = registry.queryUtility(IRoutesMapper)
    routes = {}
    for route in mapper.get_routes():
        args = []

        # all patterns should start with /
        pattern = route.pattern if route.pattern[0] == '/' else '/%s' % route.pattern

        # look for {...}
        for arg in re.findall(r'\{(.+?)\}', pattern):
            arg_name = arg.split(':')[0]
            pattern = pattern.replace(arg, arg_name)
            args.append(arg_name)

        # look for *...
        for arg in re.findall(r'(\*.+)', pattern):
            arg_name = arg.split('*')[1]
            pattern = pattern.replace(arg, '{%s}' % arg_name)
            args.append(arg_name)

        # fix __static/ and alike
        route_name = re.sub(r'\/|__', '', route.name)
        routes[route_name] = [pattern, args]

    context = {'routes': routes}
    template = Template("""
        var JSROUTES = {
            % for route_name, pattern in routes.items():
                "${route_name}": function() {
                    var pattern = "${pattern[0]}"
                    % if pattern[1]:
                        , patterArgs = ${pattern[1]};
                    for (var i=0; i<arguments.length; i++) {
                        pattern = pattern.replace("{" + patterArgs[i] + "}", arguments[i] || "");
                    }
                    % else:
                    ;
                    % endif
                    return pattern;
                }${',' if not loop.last else ''}
            % endfor
        };
    """)
    registry._routes = template.render(**context)


def attach_routes(event):
    """ Set the template global `jsroutes`. """
    request = event.get('request')
    if request is None:
        request = get_current_request()

    routes = getattr(request.registry, '_routes', '')
    event.update({'jsroutes': routes})
