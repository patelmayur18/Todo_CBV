from django.urls import path
from . views import todo_list,todo_detail,todo_create,todo_update,todo_delete

app_name = 'TODOS_CBV_APP'

urlpatterns = [
   path('', todo_list.as_view(),name="todo-list"),
   path('create/', todo_create.as_view(),name="todo-create"),
   path('<int:pk>/', todo_detail.as_view(),name="todo-details"),
   path('<int:pk>/update/', todo_update.as_view(),name="todo-update"),
   path('<int:pk>/delete/', todo_delete.as_view(),name="todo-delete"),
]