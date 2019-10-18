from django.views.generic import TemplateView, CreateView
from donation.models import Donation, Institution
from django.shortcuts import render
from django.db.models import Sum



class IndexPage(TemplateView):
    template_name = "index.html"

    def get(self, request):
        institutions = Institution.objects.all()
        bag_amount = Donation.objects.aggregate(Sum('quantity'))
        institutions_amount = Institution.objects.all().count()
        ctx = {
            'institutions': institutions,
            'bags': bag_amount,
            'institutions_amount': institutions_amount

        }

        return render(request, self.template_name, ctx)


class AddDonationPage(TemplateView):
    template_name = "form.html"

class LoginPage(TemplateView):
    template_name = "login.html"

class RegisterPage(TemplateView):
    template_name = "register.html"

