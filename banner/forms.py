from wtforms import Form, StringField, TextAreaField, validators
from wtforms import IntegerField
from wtforms.widgets import HiddenInput

strip_filter = lambda x: x.strip() if x else None


class CreateCourse(Form):
    course_name = StringField('Enter Course Name:', [validators.length(min=1, max=255)])


class CreateProf(Form):
    professor_name = StringField('Enter Professors Name:', [validators.length(min=3, max=15)])


class CreateSection(Form):
    section_number = StringField('Enter section number',[validators.length(min=2, max=4)])
