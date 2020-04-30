from django.shortcuts import render
from django.http.response import JsonResponse
from api.models import Company, Vacancy

def companies_list(request):
    companies = Company.objects.all()
    companies_json = [c.to_json() for c in companies]
    return JsonResponse(companies_json, safe=False)

def company_detail(request,id):
    try:
        company = Company.objects.get(id=id).to_json()
    except Company.DoesNotExist:
        return JsonResponse({'error': 'company does not exists'})
    return JsonResponse(company)

def company_vacancies(request,id):
    try:
        company = Company.objects.get(id=id)
        company_vacancies = company.vacancy.all()
        company_vacancies_json = [v.to_json() for v in company_vacancies]
    except:
        return JsonResponse({'error': 'no vacancy'})
    return JsonResponse(company_vacancies_json, safe=False)

def vacancies(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [v.to_json() for v in vacancies]
    return JsonResponse(vacancies_json, safe=False)

def vacancy(request,id):
    try:
        vacancy = Vacancy.objects.get(id=id).to_json()
    except Vacancy.DoesNotExist:
        return JsonResponse({'error': 'no vacancy'})
    return JsonResponse(vacancy)

def vacancies_top(request):
    vacancies_top = Vacancy.objects.order_by("-salary")[:10]
    vacancies_top_json = [v.to_json() for v in vacancies_top]
    return JsonResponse(vacancies_top_json, safe=False)
