from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sites.models import Site

def default(request):
    return {
        'site' : Site.objects.get_current(),
    }