from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . import models
from . import forms
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
 
# Create your views here.

def index(request):
        return render(request, 'index.html', {})
 
def product_list(request):
    return render(request, 'planner/product_list.html', {})

def login(request):
    return render(request, 'planner/login.html', {})

def logout(request):
    return render(request, 'planner/logout.html', {})

def registration_form(request):
    return render(request, 'planner/registration_form.html', {})

@method_decorator(login_required, 'dispatch')
class MealCreate(CreateView):
    """Widok dodawania produktow"""

    model = models.Meal
    form_class = forms.MealForm
    success_url = reverse_lazy('lista')   

    def get_context_data(self, **kwargs):
        context = super(ProductCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            context['info'] = forms.PFormSet(self.request.POST)
        else:
            context['info'] = forms.PFormSet()
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        info = forms.PFormSet(self.request.POST)
        if form.is_valid() and info.is_valid():
            return self.form_valid(form, info)
        else:
            return self.form_invalid(form, info)

    def form_valid(self, form, info):
        form.instance.autor = self.request.user
        self.object = form.save()
        info.instance = self.object
        info.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, info):
        return self.render_to_response(
            self.get_context_data(form=form, info=info)
        )