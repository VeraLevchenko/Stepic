from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def day_info(request, day):
	signs = {
		"monday": "Понедельник - работать",
		"tuesday ": "Вторник - работать",
		"wednesday ": "Среда - работать",
		"thursday ": "Четверг - работать",
		"friday ": "Пятница - работать немного",
		"saturday ": "Суббота - работать",
		"sunday ": "Воскресенье - работать по дому",
	}

	if day in signs:
		return HttpResponse(signs[day])
	return HttpResponse("Неизвестный знак зодиака")


def day_info_by_number(request, day: int):
	if day in [1, 2, 3, 4, 5, 6, 7]:
		return HttpResponse(f'Сегодня {day} день недели')
	else:
		return HttpResponse(f'неверный номер дня - {day}')
