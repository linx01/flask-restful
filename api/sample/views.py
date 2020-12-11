from flask import jsonify,request
from . import sample_api
from func.sample import book,hero



@sample_api.route('/book', methods=["GET", "POST", "PUT", "DELETE"])
def func_views():
    # restful接口
    ret = book()
    return ret

@sample_api.route('/hero', methods=["GET", "POST", "PUT", "DELETE"])
def hero_views():
    # restful接口
    ret = hero()
    return ret