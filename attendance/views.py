from django.shortcuts import render
from django.http import HttpResponse

from attendance.forms import EmployeeAddForm
from attendance.models import Employee


def process(request):
    card_id = request.GET.get('card_id')
    employee = Employee.objects.all()
    # for employee in employees:
    #     if employee.card_id == card_id:
    #         return HttpResponse('Этот пользователь уже существует')
    new_employee = employee(card_id=card_id)
    new_employee.save()
    form = EmployeeAddForm()
    context = {
        'form': form
    }
    return render(request, 'attendance/home.html', context)
