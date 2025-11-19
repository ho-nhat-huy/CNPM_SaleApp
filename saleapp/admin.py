from flask_admin import Admin
from flask_admin.theme import Bootstrap4Theme
from flask_admin.contrib.sqla import ModelView
from saleapp import app, db
from saleapp.models import Category, Product

class MyCategoryView(ModelView):
    column_list = ['name', 'created_date', 'products']
    column_searchable_list = ['name']
    column_filters = ['name']

    column_labels = {
        "name": "Tên loại",
        "created_date": "Ngày tạo",
        "product": "Danh sách sản phẩm"
    }

admin =Admin(app=app, name="E-Commerce", theme=Bootstrap4Theme())

admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Product, db.session))