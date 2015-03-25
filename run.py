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

dirs = {'tops':'tmall/data/tops/','shoes':'tmall/data/shoes/','pants':'tmall/data/pants/'}
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

    

def load_data(rank, clothing_type):
    print 'load data, rank:', rank
    data = {}
    for site in os.listdir(dirs[clothing_type]):
        one_site = []
        for jsonfile in os.listdir(dirs[clothing_type]+ site + "/"):
            f = open(dirs[clothing_type]+  site + '/' + jsonfile, 'r')
            d = json.load(f)
            f.close()
            for ele in d:
                ele['trade_num_val'] = trade_num_to_int(ele['trade_num'])
            if rank:
                d=sorted(d, key=lambda ele:ele['trade_num_val'], reverse=True)
            one_site.extend(d)
 #       for ele in one_site:
  #          print ele['trade_num_val'], 

        data[site] = one_site
 #   print 'load_data'
    return data

#clothing_data = load_data()

def random_x(clothing_data, num):
    #print 'random_x'
    tm = clothing_data['tm']
    number = len(tm)
    sel = []
    while len(sel) < num:
        sel.append(tm[random.randint(0,number - 1)])
 #   print sel
    return sel

#def encode_tm(sel):
#    ret = []
#    for good in sel:
#        try:
#            good['trade_num'] = good['trade_num'][0].encode('utf-8')
#        except Exception, e:
#            good['trade_num'] = u'未知'
#        try:
#            good['title'] = good['title'][0].encode('utf-8')
#        except Exception, e:
#            good['title'] = ''
#        ret.append(good)
##    print ret
#    return ret
#
def rank_se(clothing_data, start, end):
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
        return render_template('index.html', sel=random_x(load_data(False,'tops'), 16));
    except Exception, e:
        return "Error."

@app.route('/show/')
def show():
    clothing_type = request.args.get('type')
    by_random = request.args.get('random')
    try:
        now_pg=int(request.args.get('page'))
    except Exception, e:
        now_pg = 1
    if now_pg <= 0:
        now_pg = 1

    if by_random == None or by_random == '1':
        return render_template('show.html', sel=random_x(load_data(False,clothing_type), 16),clothing_type=clothing_type,now_pg=now_pg, rand='1')
    else:
        start_page = now_pg * 16 - 16
        return render_template('show.html', sel=rank_se(load_data(True,clothing_type), start_page, start_page + 16),clothing_type=clothing_type,now_pg=now_pg,rand='0')

tips_dir='./tmall/data/tips/'
def load_tips():
    ret = []
    for fl in os.listdir(tips_dir):
        f = open(tips_dir + fl)
        tip_json = json.load(f)
        ret.extend(tip_json)
    return ret
tips_data = load_tips()

def get_tips():
    return tips_data[0:4]

@app.route('/tips/')
def tips():
    tips_to_show=get_tips()
    return render_template('tip.html', sel=tips_to_show)


if __name__=='__main__':
    port = int(os.environ.get("PORT", 5300))
    app.run(host='0.0.0.0', port=port, debug=True)



