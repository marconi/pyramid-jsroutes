# Pyramid JSRoutes

A pyramid routes composer for javascript.

## Installation

    pip install -U pyramid-jsroutes

## Usage

Include the package in your Pyramid app's main function:

    def main():
        ...
        config.include('jsroutes')
        ...
        return config.make_wsgi_app()

this will make `jsroutes` available to all your template context, then you can use it like:

    <script type="text/javascript">${jsroutes|n}</script>

then you can start composing your Pyramid routes from javascript like:

    JSROUTES.blog_post(1)  // /posts/1

### Note

Each time your modify your Pyramid routes, you need to refresh your page to refetch the updated routes.
