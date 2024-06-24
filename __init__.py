from flask import render_template

def load(app):
    def view_challenges():
        return render_template('page.html', content="<h1>Challenges are currently closed</h1>")

    # The format used by the view_functions dictionary is blueprint.view_function_name
    app.view_functions['challenges.challenges_view'] = view_challenges
