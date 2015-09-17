import re
import os
import os.path as op

from flask import Flask, render_template, request, redirect, url_for, flash, send_file, Response
from flask.ext.admin import BaseView
from flask.ext.login import LoginManager
from wtforms import form, fields, validators, TextField, TextAreaField, SubmitField
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_admin.contrib import sqla
import flask_login as login
from flask_admin import helpers, expose
import flask_admin as admin

from jinja2 import Markup

from download_and_save_flie import download_file_all
from Kosher_apps import pharser_app








# Creates a Flask app and reads the settings from a
# configuration file. We then connect to the database specified
# in the settings file

app = Flask(__name__)
app.config.from_pyfile('app.cfg')
file_path = op.join(op.dirname(__file__), 'files')
try:
    os.mkdir(file_path)
except OSError:
    pass
db = SQLAlchemy(app)


def init_login():
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)


'''
הוספת צפייה לנתונים ממסד נתונים
'''


class MyModelView(sqla.ModelView):
    def is_accessible(self):
        return login.current_user.is_authenticated()
        # can_create = False
        # column_list = ('login', 'email')
        # form_overrides = dict(status=SelectField)
        # form_args = dict(
        #     # Pass the choices to the `SelectField`
        #     status=dict(
        #         choices=[(0, 'waiting'), (1, 'in_progress'), (2, 'finished')]
        #     ))
        # def _handle_view(self, name, **kwargs):
        #     if not self.is_accessible():
        #         return redirect(url_for('show_all', next=request.url))


# We are defining a 'Comments' model to store the comments the user
# enters via the form.
class apps_kosher(db.Model):
    # Setting the table name and
    # creating columns for various fields
    __tablename__ = 'kosher app'
    id = db.Column('app_id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True)
    Description = db.Column(db.String)
    PEGI = db.Column(db.String(20))
    Img1 = db.Column(db.String)
    Img2 = db.Column(db.String)
    Img3 = db.Column(db.String)
    Img4 = db.Column(db.String)
    Url_video = db.Column(db.String)
    Link_downland = db.Column(db.String)
    id_google_play = db.Column(db.String)
    # pub_date = db.Column(db.DateTime)


    def __init__(self, name, Description, PEGI, Img, Img2, Img3, Img4, Url_video, Link_downland, id_google_play):
        # Initializes the fields with entered data
        # and sets the published date to the current time
        self.name = name
        self.Description = Description
        self.PEGI = PEGI
        self.Img1 = Img
        self.Img2 = Img2
        self.Img3 = Img3
        self.Img4 = Img4
        self.Url_video = Url_video
        self.Link_downland = Link_downland
        self.id_google_play = id_google_play
        # self.pub_date = datetime.now()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    login = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String(64))

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    # Required for administrative interface
    def __unicode__(self):
        return self.username


class LoginForm(form.Form):
    login = fields.TextField(validators=[validators.required()])
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError('Invalid user')

        # we're comparing the plaintext pw with the the hash from the db
        if not check_password_hash(user.password, self.password.data):
            # to compare plain text passwords use
            # if user.password != self.password.data:
            raise validators.ValidationError('Invalid password')

    def get_user(self):
        return db.session.query(User).filter_by(login=self.login.data).first()


class RegistrationForm(form.Form):
    login = fields.TextField(validators=[validators.required()])
    email = fields.TextField()
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        if db.session.query(User).filter_by(login=self.login.data).count() > 0:
            raise validators.ValidationError('Duplicate username')


def is_email_address_valid(email):
    """Validate email address using regular expression."""
    if not re.match("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$", email):
        return False
    return True


class MyAdminIndexView(admin.AdminIndexView):
    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated():
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        # handle user login
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login.login_user(user)

        if login.current_user.is_authenticated():
            return redirect(url_for('.index'))
        # link = '<p>Don\'t have an account? <a href="' + url_for('.register_view') + '">Click here to register.</a></p>'
        link = '<p>Don\'t have an account? <a href="' + '">Click here to register.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()

    # @expose('/register/', methods=('GET', 'POST'))
    # # # def is_accessible(self):
    # # #     return login.current_user.is_authenticated()
    # #
    # def register_view(self):
    #     return ''

    #     form = RegistrationForm(request.form)
    #     if helpers.validate_form_on_submit(form):
    #         user = User()
    #
    #         form.populate_obj(user)
    #
    #         # we hash the users password to avoid saving it as plaintext in the db,
    #         # remove to use plain text:
    #         user.password = generate_password_hash(form.password.data)
    #
    #         db.session.add(user)
    #         db.session.commit()
    #
    #         login.login_user(user)
    #         return redirect(url_for('.index'))
    #     link = '<p>Already have an account? <a href="' + url_for('.login_view') + '">Click here to log in.</a></p>'
    #     self._template_args['form'] = form
    #     self._template_args['link'] = link
    #     return super(MyAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))


# The default route for the app.
# Displays the list of already entered comments
# We are getting all the comments ordered in
# descending order of pub_date and passing to the
# template via 'comments' variable
@app.route('/')
def show_all():
    # s=select([Comments])
    # a=Comments.query.filter_by(name="Facebook").all()
    # print(a)
    # print(Comments.query.filter(Comments.name.ilike("%Angry Birds%")))
    # return render_template('show_all.html', comments=Comments.query.order_by(Comments.name).all()  )

    return render_template('new_apps.html', comments=apps_kosher.query.order_by(apps_kosher.name).all())


class ImageView(sqla.ModelView):
    def _list_thumbnail(view, context, model, name):
        print(view)
        if not model.path:
            return ''

        return Markup('<img src="%s">' % url_for('static',
                                                 filename=form.thumbgen_filename(model.path)))

    column_formatters = {
        'path': _list_thumbnail
    }

    # Alternative way to contribute field is to override it completely.
    # In this case, Flask-Admin won't attempt to merge various parameters for the field.
    # form_extra_fields = {
    #     'path': form.ImageUploadField('Image',
    #                                   base_path=file_path,
    #                                   thumbnail_size=(100, 100, True))
    # }


class url_Form(form.Form):
    url_my = fields.TextAreaField(validators=[validators.required()])
    # link_downland = fields.TextAreaField()


    # def validate_url(self):
    # if self.validators.URL(require_tld=True, message='sdasda'):
    #     print('y')
    #     raise validators.ValidationError(flash('edasdaskdal'))


def my_trread(url_from_admin):
    return pharser_app('https://play.google.com/store/apps/details?id=%s' % url_from_admin.data)


class MyView(BaseView):
    def is_accessible(self):
        return login.current_user.is_authenticated()

    @expose('/', methods=('GET', 'POST'))
    def index(self):
        form = url_Form(request.form)
        if request.method == 'POST':
            # a=form._url.data
            url_from_admin = form.url_my
            # print(form.link_downland.data)
            # add_url = pharser_app('https://play.google.com/store/apps/details?id=%s' %url_from_admin.data)
            add_url = pharser_app('https://play.google.com/store/apps/details?id=%s' % url_from_admin.data)
            # print('https://play.google.com/store/apps/details?id=%s'%url_from_admin.data)
            print(add_url)
            # if 'Not Found' in add_url:
            #     print('y')
            if db.session.query(apps_kosher).filter_by(id_google_play=url_from_admin.data).count() > 0:
                flash('app exist', category='error')

            elif any('Not Found' in i for i in add_url if i != None):
                flash('Not Found', category='error')

            else:

                apps = apps_kosher(add_url[0], add_url[1], add_url[2], add_url[3], add_url[4], add_url[5], add_url[6],
                                   add_url[7], None, url_from_admin.data)

                db.session.add(apps)
                db.session.commit()
                flash('success', category='success')

        return self.render('add_apps.html', form=form)


class download(form.Form):
    download_app_name = fields.TextAreaField(validators=[validators.required()])
    download_app_id = fields.TextAreaField(validators=[validators.required()])


# download_app = fields.HiddenField(default=True)
# class do():
#
#
#     def dw(self):
#         form = download(request.form)
#         print(form.download_app.data)


@app.route('/description/<app_name>.apk', methods=('GET', 'POST'))
def description(app_name):
    form = download(request.form)
    if request.method == 'POST':
        # print(form.download_app.data)

        print(form.download_app_name.data)
        print(form.download_app_id.data)

        #         headers={
        #     'Content-Disposition': 'attachment; filename=' + stream['filename']
        # }
        #     for header in ('content-type', 'content-length', 'transfer-encoding'):
        #         if header in binary.headers:
        #             headers[header] = binary.headers[header]


        a = download_file_all(form.download_app_name.data, form.download_app_id.data)

        # return send_from_directory
        # print(type(a))
        # file = request.files['data_file']
        # file_contents = a.stream.read().decode("utf-8")
        # print(a.info()['Content-Disposition'])
        # return a.read()
        # return a
        # return a.write(a.read())
        # print(a.info())
        # print(a)
        # return redirect(a,Response=a)
        # return '<ahref=%s> "sdasdas"</a>'%a
        # return Response(a,mimetype='application/vnd.android.package-archive')
        return  send_file(a,mimetype='application/vnd.android.package-archive')
        # print(a)
        return send_file(a, attachment_filename="%s.apk" % form.download_app_name.data,
                         as_attachment=True)
        # location = os.path.abspath("")
        # dump=a
        # with open("{}.apk".format('aaaa'), 'wb+') as location:
        #     aa=shutil.copyfileobj(dump, location)
        # del dump
        # response = make_response(aa.read())

        # return flask.Response(a.raw)
        # # print('aaa')
        # response.headers["Content-Disposition"] = "attachment; filename=result.csv"
        # return response

    return render_template('description.html', form=form,
                           comments=apps_kosher.query.filter(apps_kosher.name == app_name).all())


# def dwon_app(methods=('POST')):
#         form = download(request.form)
#         print(form.download_app.data)


# def download():
#     # download_app = fields.TextAreaField(validators=[validators.required()])
#     print(request.form)




class add_user_from(form.Form):
    username = fields.TextAreaField(validators=[validators.required()])
    email = fields.TextAreaField()
    password = fields.PasswordField()

    def validate_username(self, field):
        # print(db.session.query(User).filter_by(first_name=22).count() > 0)
        if db.session.query(User).filter_by(first_name=self.username.data).count() > 0:
            # flash('Duplicate username',category='error')
            raise validators.ValidationError(flash('Duplicate username', category='error'))


class ContactForm(form.Form):
    name = TextField("Name", [validators.Required("Please enter your name.")])
    email = TextField("Email", [validators.Required("Please enter your email address."),
                                validators.Email("Please enter your email address.")])
    subject = TextField("Subject", [validators.Required("Please enter a subject.")])
    message = TextAreaField("Message", [validators.Required("Please enter a message.")])
    submit = SubmitField("Send")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            return 'Form posted.'

    elif request.method == 'GET':
        return render_template('contact.html', form=form)


class addUser(admin.BaseView):
    def is_accessible(self):
        return login.current_user.is_authenticated()

    @expose('/', methods=('GET', 'POST'))
    def register_view(self):
        form = add_user_from(request.form)

        if request.method == 'POST':
            if form.validate():
                user = User()

                form.populate_obj(user)
                user.first_name = form.username.data

                user.login = user.first_name
                user.email = form.email.data

                user.password = generate_password_hash('{}'.format(form.password.data))
                # if not db.session.query(User).filter_by(first_name=user.first_name).count() > 0:

                db.session.add(user)
                db.session.commit()
                flash('User was successfully submitted', category='success')

                # else:
                #     flash('Duplicate username')

        return self.render('register.html', form=form)

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))


init_login()

admin = admin.Admin(app, 'Example: Auth', index_view=MyAdminIndexView(), base_template='my_master.html')
# admin.add_view(MyView(name='Hello 2', endpoint='register', category='Test'))
admin.add_view(MyView(name='add apps', category='apps', url='and apps'))
admin.add_view(MyModelView(User, db.session, category='user'))
admin.add_view(MyModelView(apps_kosher, db.session, category='apps'))
admin.add_view(addUser(name='add user', category='user'))


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        if not request.form['search']:

            return redirect(url_for('show_all'))
        else:
            # query = Comments.query.filter(Comments.name == request.form['search']).all()

            # query=Comments.query.filter(func.lower(Comments.name)==func.lower(request.form['search'])).all()
            query = apps_kosher.query.filter(apps_kosher.name.ilike("%{}%".format(request.form['search']))).all()

            return render_template('search.html', comments=query)

    return render_template('new_apps.html', comments=apps_kosher.query.order_by(apps_kosher.name).all())
    # return render_template('search.html',comments=Comments.query.order_by(Comments.name).all())


# @app.route('/user/<username>')
# def show_user(username)
#     show_user=U

# This view method responds to the URL /new for the methods GET and POST
# @app.route('/admin', methods=['GET', 'POST'])
# def new():
#     if request.method == 'POST':
#         # The request is POST with some data, get POST data and validate it.
#         # The form data is available in request.form dictionary.
#         # Check if all the fields are entered. If not, raise an error
#         if not request.form['name'] or not request.form['Img'] or not request.form['Link']:
#             flash('Please enter all the fields', 'error')
#
#         # Check if the email address is valid. If not, raise an error
#         # elif not is_email_address_valid(request.form['email']):
#         #     flash('Please enter a valid email address', 'error')
#
#         else:
#             # The data is valid. So create a new 'Comments' object
#             # to save to the database
#             comment = Comments(request.form['name'],
#                                None, None,
#                                request.form['Img'],
#                                request.form['Link'])
#
#             # Add it to the SQLAlchemy session and commit it to
#             # save it to the database
#             db.session.add(comment)
#             db.session.commit()
#
#             # Flash a success message
#             flash('Comment was successfully submitted')
#
#             # Redirect to the view showing all the comments
#             return redirect(url_for('show_all'))
#
#     # Render the form template if the request is a GET request or
#     # the form validation failed
#     return render_template('new.html')


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'GET':
#         return render_template('login3.html')
#     elif request.method == 'POST':
#         if not request.form['username'] or not request.form['password']:
#             flash('Please enter all the fields', 'error')
#             return redirect(url_for('show_all'))
#         else:
#             return redirect(url_for('show_all'))
#         # username = request.form['username']
#         # password = request.form['password']
#         # print(username, password)
#         return redirect(url_for('new'))

def build_sample_db():
    """
    Populate a small db with some example entries.
    """

    # db.drop_all()
    db.create_all()
    # passwords are hashed, to use plaintext passwords instead:
    # test_user = User(login="test", password="test")
    # test_user = User(login="test", password=generate_password_hash("test"))
    # db.session.add(test_user)
    #
    # first_names = [
    #     'Harry', 'Amelia', 'Oliver', 'Jack', 'Isabella', 'Charlie','Sophie', 'Mia',
    #     'Jacob', 'Thomas', 'Emily', 'Lily', 'Ava', 'Isla', 'Alfie', 'Olivia', 'Jessica',
    #     'Riley', 'William', 'James', 'Geoffrey', 'Lisa', 'Benjamin', 'Stacey', 'Lucy'
    # ]
    # last_names = [
    #     'Brown', 'Smith', 'Patel', 'Jones', 'Williams', 'Johnson', 'Taylor', 'Thomas',
    #     'Roberts', 'Khan', 'Lewis', 'Jackson', 'Clarke', 'James', 'Phillips', 'Wilson',
    #     'Ali', 'Mason', 'Mitchell', 'Rose', 'Davis', 'Davies', 'Rodriguez', 'Cox', 'Alexander'
    # ]
    #
    # for i in range(len(first_names)):
    #     user = User()
    #     user.first_name = first_names[i]
    #     user.last_name = last_names[i]
    #     user.login = user.first_name.lower()
    #     user.email = user.login + "@example.com"
    #     user.password = generate_password_hash('1234')
    #     db.session.add(user)
    user = User()
    user.first_name = '5'
    user.last_name = 'bm'
    user.login = user.first_name.lower()
    user.email = user.login + "@example.com"
    user.password = generate_password_hash('5')
    db.session.add(user)
    db.session.commit()
    # images = ["Buffalo", "Elephant", "Leopard", "Lion", "Rhino"]
    # for name in images:
    #     image = Image()
    #     image.name = name
    #     image.path = name.lower() + ".jpg"
    #     db.session.add(image)
    #
    # db.session.commit()
    return


# This is the code that gets executed when the current python file is
# executed.
if __name__ == '__main__':
    # Run the app on all available interfaces on port 80 which is the
    # standard port for HTTP
    app.run(
        host="localhost",

        port=int("80"), debug=True)