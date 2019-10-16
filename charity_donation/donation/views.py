from django.views.generic import TemplateView, CreateView
from donation.models import Donation

class IndexPage(TemplateView):
    template_name = "index.html"

class AddDonation(CreateView):
    model = Donation
    fields = []
