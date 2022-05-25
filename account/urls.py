from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name = 'login_view'),
    path('register/', views.register, name = 'register'),
    path('admin/', views.admin, name = 'admin'),
    path('learner/', views.learner, name = 'learner'),
    path('instructor/', views.instructor, name = 'instructor'),
    path('learnerprofile/', views.learnerprofile, name = 'learnerprofile'),
    path('learnernotes/', views.learnernotes, name = 'learnernotes'),
    path('pickcourse/', views.pickcourse, name = 'pickcourse'),
    path('instructorprofile/', views.instructorprofile, name = 'instructorprofile'), 
    path('instructorCourseContent/<int:myid>', views.instructorCourseContent, name = 'instructorCourseContent'), 
    path('instructorCourseAuthorizedBook/<int:myid>', views.instructorCourseAuthorizedBook, name = 'instructorCourseAuthorizedBook'), 
    path('instructorCourseProvidedContent/<int:myid>', views.instructorCourseProvidedContent, name = 'instructorCourseProvidedContent'),
    path('learner_list/<int:myid>', views.learner_list, name = 'learner_list'),  
    path('friends_list/<int:myid>', views.friends_list, name = 'friends_list'),  
    path('TMA-1/course-<int:myid>', views.tma1, name = 'TMA1'), 
    path('TMA-2/course-<int:myid>', views.tma2, name = 'TMA2'), 
    path('learnerCourseContent/i-<str:iid>/ac-<int:acid>', views.learnerCourseContent, name = 'learnerCourseContent'),  
    path('TMA-1/i-<str:iid>/ac-<int:acid>', views.tma1learner, name = 'tma1learner'),   
    path('TMA-2/i-<str:iid>/ac-<int:acid>', views.tma2learner, name = 'tma2learner'),   
    path('manageCourse/', views.manageCourse, name = 'manageCourse'), 
    path('myCourses/', views.myCourses, name = 'myCourses'),
    path("logout/", views.handleLogout, name="handleLogout"),

    # Account active and change or reset password
    path("change_password/", views.change_password, name="change_password"),
    path("activate/<uidb64>/<token>/", views.activate, name="activate"),
    path("reset/password/", PasswordResetView.as_view(template_name = 'reset_pass.html'), name="password_reset"),
    path("reset/password/done/", PasswordResetDoneView.as_view(template_name = 'reset_pass_done.html'), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", PasswordResetConfirmView.as_view(template_name = 'password_reset_confirm.html'), name="password_reset_confirm"),
    path("reset/done/", PasswordResetView.as_view(template_name = 'password_reset_complete.html'), name="password_reset_complete"), 
    
    # Add Paths
    path("add_studyCenter/", views.add_studyCenter, name="add_studyCenter"), 
    path("add_books/", views.add_books, name="add_books"),
    path("add_course/", views.add_course, name="add_course"),    
    path("add_routines/", views.add_routines, name="add_routines"),  
    

    # Delete Paths  
    path("delete_routine/<int:id>/", views.delete_routine, name="delete_routine"),    
    path("delete_book/<int:id>/", views.delete_book, name="delete_book"),    
    path("delete_studyCenter/<int:id>/", views.delete_studyCenter, name="delete_studyCenter"),    
    path("delete_course/<int:id>/", views.delete_course, name="delete_course"),    

    # Update or Edit Paths 
    path("update_routine/<int:id>/", views.update_routine, name="update_routine"),    
    path("update_routineFile/<int:id>/", views.update_routineFile, name="update_routineFile"),    
    path("update_book/<int:id>/", views.update_book, name="update_book"),   
    path("update_bookFile/<int:id>/", views.update_bookFile, name="update_bookFile"),   
    path("update_studycenter/<int:id>/", views.update_studycenter, name="update_studycenter"),    
    path("update_course/<int:id>/", views.update_course, name="update_course"),   
    path("update_courseFile/<int:id>/", views.update_courseFile, name="update_courseFile"),   
]