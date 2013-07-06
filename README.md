Pyramid JSRoutes
================

A pyramid routes composer for javascript.

Installation
------------

    pip install -U pyramid-jsroutes

Usage
-----

Include the package in your Pyramid app's main function:

```python
def main():
    ...
    config.include('jsroutes')
    ...
    return config.make_wsgi_app()
```

this will make `jsroutes` available to all your template context, then you can use it like:

    <script type="text/javascript">${jsroutes|n}</script>

then you can start composing your Pyramid routes from javascript like:

```javascript
JSROUTES.blog_post(1)  // /posts/1
```

Settings
--------

By default it'll only collect the routes once and store it in the registry but you can force reloading everytime for development by settings the following settings:

    jsroutes.reload_routes = true

Note
----

Each time your modify your Pyramid routes, you need to refresh your page to refetch the updated routes.
