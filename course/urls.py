from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="CourseHome"),
    path("about/", views.about, name="AboutUS"),
    path("contact/", views.contact, name="Contactus"),
    path("search/", views.search, name="Search"),
    path("courseView/<int:myid>", views.courseView, name="CourseView"),
    path("courseDetails/<int:myid>", views.courseDetails, name="courseDetails"),
    path("add_courseContent/<int:myid>", views.add_courseContent, name="add_courseContent"),
    path("checkout/", views.checkout, name="Checkout"),
    path("logout/", views.handleLogout, name="handleLogout"),
    path("fix/", views.fix, name="fix"),
]
