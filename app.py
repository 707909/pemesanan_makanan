from flask import Flask, render_template, request, redirect, url_for
from data_menu import menu_makanan

app = Flask (__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html', menu = menu_makanan)

if __name__ == '__main__':
    app.run(debug=True, port=5001)







