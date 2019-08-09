from flask import Blueprint

admin = Blueprint('admin', 'admin', url_prefix='/admin')


@admin.route("/")
@admin.route("/dashboard")
def dash_board():
    return "Trang admin"


@admin.route("/dangki")
def dang_ki():
    return "Đăng kí"


@admin.route("/dangnhap")
def dang_nhap():
    return "Đăng nhập"
