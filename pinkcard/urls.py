from django.urls import include,path

from .views import pinkcard, students, librarian

urlpatterns = [
	path('', pinkcard.home, name='home'),

	
	#path('students/', include(([
    #    path('', students.QuizListView.as_view(), name='quiz_list'),
    #], 'pinkcard'), namespace='students')),
    

    path('students/', include(([
        path('', students.Test, name='test'),
        path('map/',students.Map, name='map'),
        path('map/use',students.UseMap, name='usemap'),
        path('map/afteruse', students.AfterUseMap, name='afterusemap'),
        path('transfer/', students.Transfer, name='transfer'),
        path('transfer/transferhours/', students.TransferHours, name='transferhours'),
        path('transfer/transferringhours/', students.TransferringHours, name='transferringhours'),
        path('transfer/requesthours/', students.RequestHours, name='requesthours'),
    ], 'pinkcard'), namespace='students')),

	path('librarian/', include(([
        path('', librarian.Home, name='home'),
        path('deg_prog/', librarian.DegProgListView.as_view(), name="ViewingDegProgList"),
        path('deg_prog/<int:pk>/', librarian.DegProgStudentList.as_view(), name="DegProgStudentList"),
		path('elec_usage/', librarian.DisplayElecUsage, name="viewing-ElecUsageListView"),
		path('student/<int:pk>/', librarian.StudentDetailView.as_view(), name='StudentDetailView'),
		path('student/<int:pk>/update/', librarian.StudentUpdateView.as_view(), name='StudentUpdateView'),
		path('student/<int:pk>/delete/',librarian.StudentDeleteView.as_view(), name='StudentDeleteView'),
		path('student/new/',librarian.StudentCreateView.as_view(), name='StudentCreate'),
    ], 'pinkcard'), namespace='librarian')),
]