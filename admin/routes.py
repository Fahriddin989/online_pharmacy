from flask import url_for, redirect
from flask_admin import expose, BaseView, AdminIndexView
from sqlalchemy import desc

from models import Medicines


class MyMainView(AdminIndexView):
    @expose('/')
    def admin_main(self):
        # medicines = Medicines.query.order_by(desc(Medicines.name)).all()
        image = url_for('static', filename=f'storage/post_img')
        return self.render('admin/index.html', image=image)

