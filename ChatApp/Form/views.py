from django.shortcuts import render
from django.http import HttpResponse

from Form.form import InputForm

def form_view(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid:
            form.save()
    form = InputForm()
    context = {"form" : form}
    return render(request, "home.html", context)

