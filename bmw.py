from flask import Flask
lexus = Flask(__name__)

@lexus.route('/')
def home():
    return('hello')





posts = [
    {
        'title':'Uganda Crowned Miss World!',
        'author':'Walimuchan Phiona',
        'content':'First post',
        'date':'Jan 25,2019'
    },

    {
        'title':'City on Fire!',
        'author':'Samuel Ogol',
        'content':'Second post',
        'date':'Jan 31,2019'
    }
]

@lexus.route("/")
@lexus.route("/home")
def home():
    return render_template('home.html', posts=posts)


@lexus.route("/about")
def about():
    return render_template('about.html', title='About')

@lexus.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm( )
    if form.validate_on_submit():
       flash('Your account has been sucessfully created!', 'success')
       return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@lexus.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
       flash('sucessfully logged in!')
       return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)




if __name__ == '__main__':
    app.run(debug=True)