from flask_modals import render_template_modal

@app.route('/', methods=['GET', 'POST'])
def index():

    ajax = '_ajax' in request.form  # Add this line
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data != 'test' or form.password.data != 'pass':
            flash('Invalid username or password', 'danger')
            return redirect(url_for('index'))

        if ajax:        # Add these
            return ''   # two lines
        login_user(user, remember=form.remember_me.data)

        flash('You have logged in!', 'success')
        return redirect(url_for('home'))

    # Add this line
    return render_template_modal('index.html', form=form)
