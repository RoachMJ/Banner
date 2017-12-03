def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    # this was added from https://docs.pylonsproject.org/projects/pyramid/en/latest/tutorials/wiki2/definingviews.html
    # to understand how routes are mapped to views
    # note the order must be this way to enable editing we must first allow add page
    config.add_route('banner', '/')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('course', '/courses')
    config.add_route('create_course', '/course/create_course')
    config.add_route('professor', '/professor')
    config.add_route('create_professor', '/professor/create_professor')
    config.add_route('section', '/section')
    config.add_route('create_section', '/section/create_section')
# TODO we changed this file to show the reflected routes we would need