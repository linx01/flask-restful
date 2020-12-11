from flask import request,jsonify
import os
import sys
import json

root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(root)

from run import db
from models import BookInfo,PersionInfo

def book():

    '''

    restful风格接口

    GET:查询 
        查询单个 /book?name=xxx
        查询所有 /book

    POST:新增 /book
    post_data:{
        "name":xxx,
        "author":xxx,
        "country":xxx
    }

    PUT:修改 /book
    put_data:{
        "name":xxx, #必须字段
        "author":xxx,
        "country":xxx
    }

    DELETE:删除 /book
    delete_data:{
        "name":xxx # 必须字段
    }

    '''

    if request.method == "GET":
 
        if request.values.get("name", ""):
            db.session.commit() # 查询之前也要提交事务
            res = BookInfo.query.filter_by(name=request.values.get("name")).first()
            if not res:
                return jsonify({"status":200, "info":"empty"})
            else:
                return jsonify({"status":200, "info":{res.name:{"author":res.author, "country":res.country}}})
        else:
            db.session.commit()
            res = BookInfo.query.all()
            books_info = {}
            for r in res:
                books_info[r.name] = {}
                books_info[r.name]["country"] = r.country
                books_info[r.name]["author"] = r.author
            return jsonify({"status":200, "info":books_info})

    if request.method == "POST":
        try:
            name = request.values.get("name")
            country = request.values.get("country")
            author = request.values.get("author")
            book_object = BookInfo(name,author,country)
            db.session.add(book_object)
            db.session.commit()
            return jsonify({"status":200, "info":"success"})
        except Exception as e:
            db.session.rollback() # 回滚
            return jsonify({"status":404, "info":"add error:" + str(e)})

    if request.method == "PUT":

        name = request.values.get("name", "")
        author = request.values.get("author", "")
        country = request.values.get("country", "")
        if not name:
            return jsonify({"status":404, "info":"please enter the book_name"})
        res = BookInfo.query.filter_by(name=name).first()
        if not res:
            return jsonify({"status":404, "info":"could not find the book info"})
        if author and country:
            res.author = author
            res.country = country
        elif author:
            res.author = author
        elif country:
            res.country = country
        else:
            return jsonify({"status":200, "info":"nothing update"})
        try:
            db.session.commit()
            return jsonify({"status":200, "info":"update success"})
        except Exception as e:
            db.session.rollback() # 回滚
            return jsonify({"status":404, "info":"update error:" + str(e)})

    if request.method == "DELETE":
  
        name = request.values.get("name", "")
        if not name:
            return jsonify({"status":404, "info":"please enter the book_name"})
        res = BookInfo.query.filter_by(name=name).first()
        if not res:
            return jsonify({"status":404, "info":"could not find the book info"})

        try:
            db.session.delete(res)
            db.session.commit()
            return jsonify({"status":200, "info":"delete success"})
        except Exception as e:
            db.session.rollback() # 回滚
            return jsonify({"status":404, "info":"delete error:" + str(e)})


def hero():

    '''

    restful风格接口

    GET:查询 
        查询单个 /book?name=xxx
        查询所有 /book

    POST:新增 /book
    post_data:{
        "name":xxx,
        "author":xxx,
        "country":xxx
    }

    PUT:修改 /book
    put_data:{
        "name":xxx, #必须字段
        "author":xxx,
        "country":xxx
    }

    DELETE:删除 /book
    delete_data:{
        "name":xxx # 必须字段
    }

    '''

    if request.method == "GET":
 
        if request.values.get("name", ""):
            db.session.commit() # 查询之前也要提交事务
            res = PersionInfo.query.filter_by(name=request.values.get("name")).first()
            if not res:
                return jsonify({"status":200, "info":"empty"})
            else:
                return jsonify({"status":200, "info":{res.name:{"bookname":res.book_name}}})
        else:
            db.session.commit()
            res = PersionInfo.query.all()
            books_info = {}
            for r in res:
                books_info[r.name] = {}
                books_info[r.name]["bookname"] = r.book_name
            return jsonify({"status":200, "info":books_info})

    if request.method == "POST":
        try:
            name = request.values.get("name")
            book_name = request.values.get("bookname")
            persion_object = PersionInfo(name,book_name)
            db.session.add(persion_object)
            db.session.commit()
            return jsonify({"status":200, "info":"success"})
        except Exception as e:
            db.session.rollback() # 回滚
            return jsonify({"status":404, "info":"add error:" + str(e)})

    if request.method == "PUT":

        name = request.values.get("name", "")
        book_name = request.values.get("bookname", "")

        if not name:
            return jsonify({"status":404, "info":"please enter the hero name"})
        res = PersionInfo.query.filter_by(name=name).first()
        if not res:
            return jsonify({"status":404, "info":"could not find the hero info"})
        if name and book_name:
            res.name = name
            res.book_name = book_name
        elif name:
            res.name = name
        elif country:
            res.book_name = book_name
        else:
            return jsonify({"status":200, "info":"nothing update"})
        try:
            db.session.commit()
            return jsonify({"status":200, "info":"update success"})
        except Exception as e:
            db.session.rollback() # 回滚
            return jsonify({"status":404, "info":"update error:" + str(e)})

    if request.method == "DELETE":
  
        name = request.values.get("name", "")
        if not name:
            return jsonify({"status":404, "info":"please enter the hero name"})
        res = PersionInfo.query.filter_by(name=name).first()
        if not res:
            return jsonify({"status":404, "info":"could not find the book info"})

        try:
            db.session.delete(res)
            db.session.commit()
            return jsonify({"status":200, "info":"delete success"})
        except Exception as e:
            db.session.rollback() # 回滚
            return jsonify({"status":404, "info":"delete error:" + str(e)})