from django.shortcuts import render, redirect
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage


def index(request):
    """ Take in the user input in the form."""
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            firstName = form.cleaned_data["firstName"]
            lastName = form.cleaned_data["lastName"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            Form.objects.create(firstName=firstName, lastName=lastName,
                                email=email, date=date, occupation=occupation)

            message_body = f"A new job application was submitted. \nThank you, \n{firstName} {lastName}"

            email_message = EmailMessage("Form submission confirmation", message_body, to=[email])
            email_message.send()

            messages.success(request,"Form submitted successfully!")
            return redirect('/')
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")
