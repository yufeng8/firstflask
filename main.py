from flask import Flask, request, url_for, redirect, render_template
app = Flask(__name__)

@app.route('/')
def index():
    #return redirect(url_for('cool_form'))
    return render_template('index.html')

@app.route('/cool_form')
def cool_form():
    
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        #return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('cool_form.html')
 
if __name__ == '__main__':
    app.run(debug=True)

# @app.route('/')
# def index():
#     return 'Index Page'

# @app.route('/hello')
# def hello():
#     return 'Hello, World'

# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % username

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return 'Subpath %s' % subpath

# @app.route('/projects/')
# def projects():
#     return 'The project page'

# @app.route('/about')
# def about():
#     return 'The about page'



