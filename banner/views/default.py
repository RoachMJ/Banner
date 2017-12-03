# this new file also came from https://docs.pylonsproject.org/projects/pyramid/en/latest/tutorials/wiki2/definingviews.html
# we will have to understand the views in order to get banner running

from pyramid.compat import escape
import re
from docutils.core import publish_parts

from pyramid.httpexceptions import (
    HTTPForbidden,
    HTTPFound,
    HTTPNotFound,
    )

from pyramid.view import view_config

#from ..models import Page, User
from ..models import User, Course, Professor, Section
from ..forms import CreateCourse, CreateProf, CreateSection

# regular expression used to find WikiWords


@view_config(route_name='banner', renderer='../templates/banner.jinja2')



@view_config(route_name='course', renderer='../templates/course.jinja2')
def list_course(request):  # view callable function
    course = request.dbsession.query(Course.name).all()
    id = request.dbsession.query(Course).first()
    print(id, course)
    return dict(course=course)


@view_config(route_name='create_course', renderer='../templates/create_course.jinja2')
def create_course1(request):
    form = CreateCourse(request.POST)
    if request.method == 'POST' and form.validate():
        new_course = Course(name=form.course_name.data)
        request.dbsession.add(new_course)
        print ('We have just created a Course')
        return HTTPFound(location=request.route_url('course'))
    return {'form': form}


@view_config(route_name='professor', renderer='../templates/professor.jinja2')
def list_professor(request):  # view callable function
    prof = request.dbsession.query(Professor.name).all()
    id = request.dbsession.query(Professor).first()
    print(id, prof)
    return dict(professor=prof)


@view_config(route_name='create_professor', renderer='../templates/create_professor.jinja2')
def create_professor(request):
    form = CreateProf(request.POST)
    if request.method == 'POST' and form.validate():
        new_professor = Professor(name=form.professor_name.data)
        request.dbsession.add(new_professor)
        print ('We have just created a prof')
        return HTTPFound(location=request.route_url('professor'))
    return {'form': form}


@view_config(route_name='section', renderer='../templates/section.jinja2')
def list_section(request):  # view callable function
    section = request.dbsession.query(Section.number).all()
    id = request.dbsession.query(Section).first()
    print(id, section)
    return dict(section=section,)


@view_config(route_name='create_section', renderer='../templates/create_section.jinja2')
def create_section(request):
    form = CreateSection(request.POST)
    if request.method == 'POST' and form.validate():
        new_section = Section(name=form.section_number.data)
        request.dbsession.add(new_section)
        print ('We have just created a section')
        return HTTPFound(location=request.route_url('section'))
    return {'form': form}
'''
wikiwords = re.compile(r"([A-Z]\w+[A-Z]+\w+)")

@view_config(route_name='view_wiki')
def view_wiki(request):                       # Note each def is a view callable function
    # originally this was view_wiki on the tutorial it has been
    # aptly renamed banner home since it will answer on the root url
    next_url = request.route_url('view_page', pagename='FrontPage')
    return HTTPFound(location=next_url)

@view_config(route_name='view_page', renderer='../templates/view.jinja2')
def view_page(request): # view callable function
    pagename = request.matchdict['pagename']
    page = request.dbsession.query(Page).filter_by(name=pagename).first()
    if page is None:
        raise HTTPNotFound('No such page')

    def add_link(match):
        word = match.group(1)
        exists = request.dbsession.query(Page).filter_by(name=word).all()
        if exists:
            view_url = request.route_url('view_page', pagename=word)
            return '<a href="%s">%s</a>' % (view_url, escape(word))
        else:
            add_url = request.route_url('add_page', pagename=word)
            return '<a href="%s">%s</a>' % (add_url, escape(word))

    content = publish_parts(page.data, writer_name='html')['html_body']
    content = wikiwords.sub(add_link, content)
    edit_url = request.route_url('edit_page', pagename=page.name)
    return dict(page=page, content=content, edit_url=edit_url)

# @view_config(route_name='view_page', renderer='..templates/view.jinja2')
# def my_def(request):
#     user = request.user

@view_config(route_name='edit_page', renderer='../templates/edit.jinja2')
def edit_page(request): # view callable function
    pagename = request.matchdict['pagename']
    page = request.dbsession.query(Page).filter_by(name=pagename).one()
    current_user = request.dbsession.query(User).count()

    if 'form.submitted' in request.params:
        page.data = request.params['body']
        next_url = request.route_url('view_page', pagename=page.name)
        return HTTPFound(location=next_url)
    query = request.session.query(User).order_by(User.id)
    return dict(
        current=query,
        pagename=page.name,
        pagedata=page.data,
        save_url=request.route_url('edit_page', pagename=page.name),
    )


@view_config(route_name='add_page', renderer='../templates/edit.jinja2')
def add_page(request): # view callable function
    user = request.user
    if user is None or user.role not in ('editor', 'basic'):
        raise HTTPForbidden
    pagename = request.matchdict['pagename']
    if request.dbsession.query(Page).filter_by(name=pagename).count() > 0:
        next_url = request.route_url('edit_page', pagename=pagename)
        return HTTPFound(location=next_url)
    if 'form.submitted' in request.params:
        body = request.params['body']
        page = Page(name=pagename, data=body)
        page.creator = request.user
        request.dbsession.add(page) # adds record to database where ?
        next_url = request.route_url('view_page', pagename=pagename)
        return HTTPFound(location=next_url)
    save_url = request.route_url('add_page', pagename=pagename)
    return dict(pagename=pagename, pagedata='', save_url=save_url)
'''
# this registration for a new user came from the register tutorial at
#  https://docs.pylonsproject.org/projects/pyramid-blogr/en/latest/registration.html
# TODO used the link above to sort through course creation.




