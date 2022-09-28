# question 1
import requests
from PIL import Image
import flask
from flask import Flask, render_template, make_response

try:
    a = 1 / 0
except BaseException as e:
    print(str(e) + " : division by zero is not possible ")

    # question 2 - the expression is legal but not so informative in case of failure
    # because you  continue without handling the error
try:
    x = 1
finally:
    print("xasdasd")

# # question 3  - this handler is  not informative and can potentially match any error

# except:
#     print("found an error")

# # question 4 - not relate to any excepetion , no handling of the error

# QUESTION 5 A) -IOError RAISED WHEN FILE NOT EXIST
#           B) - dIVISIONBYZERO WILL BE RAISED WHEN PREFORMING ILLEGAL DIVISION (A/0)

# QUESTION 6 :

file1 = open("exer6.tx", 'w+')
file1.write("eran")
file1.close()

# QUESTION 7  :
file1 = open("exer6.txt", 'r')
print(file1.read())
file1.close()

# QUESTION  8 :
file2 = open("exer6.txt", 'a+', encoding='utf-8')
file2.write("ערן")
print(file2.read())
file2.close()

# question  9 - flask


webapp = Flask("my app")


@webapp.route('/content')
def content_page():
    file_route = 'a1234.txt'
    with open(file_route, 'r+', encoding='utf-8') as f:
        response = make_response(render_template('content.html', text=f.read()), 200)
    return response


@webapp.route('/register')
def register_page():
    with open('testFile1.txt', 'a+', encoding='utf-8') as f:
        f.write('Hello\n')
        status_code = flask.Response(status=201)
        message = 'success '
        return message + status_code.status


webapp.run(port=30000)

#  10 - challenge - added ability to add url

url = 'https://images.pexels.com/photos/235621/pexels-photo-235621.jpeg'
img = Image.open(requests.get(url, stream=True).raw)
img.show()
