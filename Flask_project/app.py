# from flask import Flask
#
#
# #create flask application
# app=Flask(__name__)# entry point
#
# @app.route("/")
# def myfirst_app():
#     return "good morning "
#
# @app.route("/hite")
# def mySecond_app():
#     return " hello guys how are you "
#
#
# if __name__=="__main__":
#     app.run(debug=True) #flask provide itself server/portal
#
# ############################################################################################################
# # from flask import Flask,redirect,url_for
# # app=Flask(__name__)
# #
# # @app.route('/admin')
# # def hello_admin():
# #     return "hello admin "
# #
# # @app.route('/guest/<guest>')
# # def hello_guest(guest):
# #     return "hello %s as guest "%guest
# #
# # @app.route('/user/<name>')
# # def hello_user(name):
# #     if name=='admin':
# #         return redirect(url_for('hello_admin'))
# #     else:
# #         return redirect(url_for('hello_guest',guest=name))
# #
# # if __name__=="__main__":
# #     app.run(debug=True) #flask provide itself server/portal
# #
# ###########################################################################################################
# #
from flask import Flask,redirect,url_for
app=Flask(__name__)

@app.route('/admin')
def hello_admin():
    return "<html><body><h2>hello website first wesite</h2></body></html>"

if __name__=="__main__":
    app.run(debug=True) #flask provide itself server/portal
#
# ###########################################################################################################
# #Flask uses jinja2 template engine.
#
# # {% ... %} for statements
# # {{ ... }} for expression to the template output
# # {# ... #} for commnets not included in the template output
# #  # ... ## for  line statemnet
#
# from flask import Flask,render_template
# app=Flask(__name__)
#
# @app.route('/hello/<user>')
# def hello_name(user):
#     return render_template('hello.html',name=user)
#
# if __name__=="__main__":
#     app.run(debug=True) #flask provide itself server/portal
#
