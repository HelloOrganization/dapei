#!/usr/bin/python
# coding=utf-8
from flask import Flask, redirect, url_for, render_template, request, g, _app_ctx_stack, make_response
import os
import re
import json
import random
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)

data_dir = 'tmall/data/tops/'

def trade_num_to_int(tr_num):
    if type(tr_num) is list and len(tr_num) > 0:
        pat=u'([0-9\.]+)(万)?'
        m = re.match(pat,tr_num[0])
        if m.group(2) != None:
            return 10000 * float(m.group(1))
        else:
            return int(m.group(1))
    else:
        return 0

    

def load_data():
    print 'load_data'
    data = {}
    for site in os.listdir(data_dir):
        one_site = []
        for jsonfile in os.listdir(data_dir + site + "/"):
            f = open(data_dir +  site + '/' + jsonfile, 'r')
            d = json.load(f)
            f.close()
            for ele in d:
                ele['trade_num_val'] = trade_num_to_int(ele['trade_num'])
            d=sorted(d, key=lambda ele:ele['trade_num_val'], reverse=True)
            one_site.extend(d)
        for ele in one_site:
            print ele['trade_num_val'], 

        data[site] = one_site
    print 'load_data'
    return data

clothing_data = load_data()

def random_x(num):
    print 'random_x'
    tm = clothing_data['tm']
    number = len(tm)
    sel = []
    while len(sel) < num:
        sel.append(tm[random.randint(0,number - 1)])
    print sel
    return sel

def encode_tm(sel):
    ret = []
    for good in sel:
        try:
            good['trade_num'] = good['trade_num'][0].encode('utf-8')
        except Exception, e:
            good['trade_num'] = u'未知'
        try:
            good['title'] = good['title'][0].encode('utf-8')
        except Exception, e:
            good['title'] = ''
        ret.append(good)
    print ret
    return ret

def rank_se(start, end):
    tm = clothing_data['tm']
    number = len(tm)
    if start >= number:
        start = number - 16
        end = start + 16
    elif number < end:
        end = number
    return tm[start:end]

@app.route('/')
def index():
    #sel=[{'image_urls':'http://gi3.mlist.alicdn.com/bao/uploaded/i3/TB1hd4tHpXXXXXgXXXXXXXXXXXX_!!0-item_pic.jpg_b.jpg'}, {'image_urls':'http://gi3.mlist.alicdn.com/bao/uploaded/i3/TB1hd4tHpXXXXXgXXXXXXXXXXXX_!!0-item_pic.jpg_b.jpg'}]
    #return 'sa'
    try:
        return render_template('index.html', sel=random_x(16));
    except Exception, e:
        return "Error."

@app.route('/show/')
def show():
    clothing_type = request.args.get('type')
    by_random = request.args.get('random')
    if by_random == None or by_random == '1':
        return render_template('show.html', sel=random_x(16))
    else:
        try:
            start_page = int(request.args.get('page')) * 16 - 16
        except Exception, e:
            start_page = 0
        if start_page < 0:
            start_page = 0
        return render_template('show.html', sel=rank_se(start_page, start_page + 16))

if __name__=='__main__':
    port = int(os.environ.get("PORT", 5300))
    app.run(host='0.0.0.0', port=port, debug=True)



