from flask import Flask, request, redirect, url_for
import html_generator as h

app = Flask (__name__)

@app.route("/")
def get_root():
    print(request)
    return h.make_body("titteli", h.form())

@app.route("/", methods = ['POST'])
def post_test():
    value = request['fname']
    return redirect(url_for("/"))



