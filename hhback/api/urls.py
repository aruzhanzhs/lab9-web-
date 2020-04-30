from django.urls import path
from api.views import companies_list, company_detail, company_vacancies, vacancies, vacancy, vacancies_top

urlpatterns = [
    path('companies/', companies_list),
    path('companies/<int:id>/', company_detail),
    path('companies/<int:id>/vacancies/', company_vacancies),
    path('vacancies/', vacancies),
    path('vacancies/<int:id>/', vacancy),
    path('vacancies/top_ten/', vacancies_top)
]