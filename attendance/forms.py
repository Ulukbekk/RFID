from django import forms

from attendance.models import Employee


class EmployeeAddForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('uid',
                  'name',
                  'card_id',
                  'salary')