def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('view_wiki', '/')
    # this was added from https://docs.pylonsproject.org/projects/pyramid/en/latest/tutorials/wiki2/definingviews.html
    # to understand how routes are mapped to views
    # note the order must be this way to enable editing we must first allow add page
    config.add_route('view_page', '/{pagename}')
    config.add_route('add_page', '/add_page/{pagename}')
    config.add_route('edit_page', '/{pagename}/edit_page')
    # these are the routes I think I need for the banner system based on my banner_models.py
    #config.add_route('course', '/courses')
    #config.add_route('professor', '/professors')
    #config.add_route('section', '/sections')

