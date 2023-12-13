# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Contact
from .forms import ContactForm

class ContactListView(ListView):
    model = Contact
    template_name = 'ContactMe/contact_list.html'
    context_object_name = 'contacts'

class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'ContactMe/contact_form.html'
    success_url = reverse_lazy('ContactMe:contact_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect(self.success_url)

    def form_invalid(self, form):
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))

class ContactDetailView(DetailView):
    model = Contact
    template_name = 'ContactMe/contact_detail.html'

class ContactUpdateView(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'ContactMe/contact_edit.html'
    
    def get_success_url(self):
        return reverse_lazy('ContactMe:contact_list')

class ContactDeleteView(DeleteView):
    model = Contact
    template_name = 'ContactMe/contact_confirm_delete.html'
    success_url = reverse_lazy('ContactMe:contact_list')

# Additional function-based views
def custom_view(request):
    # Your custom view logic here
    return render(request, 'ContactMe/custom_view.html', {})

def another_view(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    # Your logic using the 'contact' variable
    return render(request, 'ContactMe/another_view.html', {'contact': contact})
