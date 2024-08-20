from django.shortcuts import render
from .forms import MailForm
from .spam_detection import load_model


def index(request):
    result = 'Null'
    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['text']
            result = load_model(message)
            form.save()
    else:
        form = MailForm()
    return render(request, 'mail/index.html', {'form': form, 'result': result})
