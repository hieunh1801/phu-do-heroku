from flask import Blueprint, render_template

page = Blueprint('page', __name__)


@page.route("/")
@page.route("/trang-chu")
def trang_chu():
    return render_template('pages/trangchu.html')


@page.route("/bat-dong-san")
def bat_dong_san():
    return "Bất động sản"


@page.route("/tin-tuc")
def bat_dong_san():
    return "Bất động sản"
