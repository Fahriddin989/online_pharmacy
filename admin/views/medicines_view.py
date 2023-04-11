from flask_admin.contrib.sqla import ModelView


class MedicinesView(ModelView):
    column_display_pk = True
    column_labels = {
        'id': 'ID',
        'name': 'Наименовавние',
        'category_id': 'Категория',
        'country': 'Страна Производства',
        'active_substance_id': 'Активные вещества',
        'representative': 'Представители',
        'manufacturer_id': 'Производитель',
        'code_atx': 'Штрих код',
        'price': 'Цена',
        'description': 'Описание',
        'image_url': 'Фото'
    }
