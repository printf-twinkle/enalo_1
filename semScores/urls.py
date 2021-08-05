from django.urls import include, path
from semScores.views import CreateUserView, ProfileDelete, ProfileUpdate, ProfileView

urlpatterns = [
  path('signup/', CreateUserView.as_view()),
  path('profile/', ProfileView.as_view()),
  path('delete/', ProfileDelete.as_view()),
  path('update/',ProfileUpdate.as_view())
]