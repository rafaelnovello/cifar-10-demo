from pyramid.config import Configurator

import cloudinary


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()
    if 'cloudinary_api_key' in settings:
        cloudinary.config(
            cloud_name=settings['cloudinary_cloud_name'],
            api_key=settings['cloudinary_api_key'],
            api_secret=settings['cloudinary_api_secret']
        )
    return config.make_wsgi_app()
