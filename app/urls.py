from django.urls import path

import app.views as appview

urlpatterns = [
    path('api/itemslist',appview.list_items),
    path('',appview.ItemsView.as_view(),name='items')
]
