#!/usr/bin/python
# coding=utf-8
from flask import Flask, redirect, url_for, render_template, request, g, _app_ctx_stack, make_response
import os
import json
import random
app = Flask(__name__)

data_dir = 'tmall/data/'
def load_data():
    data = {}
    for site in os.listdir(data_dir):
        one_site = []
        for jsonfile in os.listdir(data_dir + site + "/"):
            f = open(jsonfile, 'r')
            d = json.load(f)
            f.close()
            one_site.extend(d)
        data[site] = one_site
    return data

clothing_data = load_data()

def random_x(num):
    tm = clothing_data['tm']
    number = len(tm)
    sel = []
    while len(sel) < num:
        sel.append(tm[random.randint(0,number)])
    return sel

def rank_se(start, end):
    tm = clothing_data['tm']
    return tm[start:end]

@app.route('/')
def index():
    return render_template('index.html', random_x(16));

@app.route('/clothes/'):
    by_random = request.args.get('random')
    if by_random == None or by_random == '1':
        return render_template('show.html', random_x(16))
    else:
        return render_template('show.html', rank_se(0, 16))


if __name__=='__main__':
    port = int(os.environ.get("PORT", 5300))
    app.run(host='0.0.0.0', port=port)



