def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('course', '/courses')
    config.add_route('professor', '/professors')
    config.add_route('section', '/sections')

