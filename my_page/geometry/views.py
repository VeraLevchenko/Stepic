from django.shortcuts import render
from django.http import HttpResponse
import math

# Create your views here.
def get_rectangle_area(request, w, h):
	s = w * h
	return HttpResponse(f'Площадь прямоугольника размером {w}x{h} равна {s}')


def get_square_area(request, h):
	s = h * h

	return HttpResponse(f'Площадь квадрата размером c Савелия {h}x{h} равна {s}')


def get_circle_area (request, r):
	s = r * r * math.pi()
	return HttpResponse(f'Площадь круга радиусом {r} равна {s}')
