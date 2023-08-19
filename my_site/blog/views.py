from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def main(request):
	return HttpResponse("Главная страница")

def all_posts(request):
	return HttpResponse("Все посты блога")

def post_details(request, name_post):
	return HttpResponse(f'Информация о посте {name_post}')

