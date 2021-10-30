from django.urls import path
from testapp.views import AnsimView, PublicPView, DataInsertView, TestView, PtestView

urlpatterns = [

	path('ansimapi', AnsimView.as_view()),
	path('publicpapi', PublicPView.as_view()),
	path('testapi', TestView.as_view()),
	path('ptestapi', PtestView.as_view()),
 	path('insertcsv',DataInsertView.as_view()),
]
