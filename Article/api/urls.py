from Article.api.views import(
	api_detail_pet_view,
	api_update_pet_view,
	api_delete_pet_view,
	api_create_pet_view,
)
from django.urls import path

app_name = 'article'

urlpatterns = [
	path('<slug>/', api_detail_pet_view, name="detail"),
	path('<slug>/update', api_update_pet_view, name="update"),
	path('<slug>/delete', api_delete_pet_view, name="delete"),
	path('create', api_create_pet_view, name="create"),
]
