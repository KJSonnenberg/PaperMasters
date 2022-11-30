from django.shortcuts import render 
from topic_pages.models import Category
from resources.models import ResourceModel
from servicepages.models import Service

def prices(request):
    return render(request, 'toplevel/prices.html')  

def terms_service(request):
    return render(request, 'toplevel/terms-service.html') 

def contact(request):
    return render(request, 'toplevel/contact.html') 

def resources(request):
    resource_list = ResourceModel.objects.all()
    return render(request, 'toplevel/resources_page.html', {'resource_list':resource_list})  

def service_pages(request): 
    service_list = Service.objects.all()
    return render(request, 'toplevel/services_page.html', {'service_list':service_list})

def about_us(request):
    return render(request, 'toplevel/about-us.html') 

def terms_use(request):
    return render(request, 'toplevel/terms-service.html')  
    
def order(request):
    return render(request, 'toplevel/order.html') 
    
def privacy_policy(request):
    return render(request, 'toplevel/privacy.html') 

def guarantees(request):
    return render(request, 'toplevel/guarantees.html')

def writing_opp(request):
    return render(request, 'toplevel/writer-position.html') 
    
def faq(request):
    return render(request, 'toplevel/FAQ.html') 

def order(request):
    return render(request, 'toplevel/order.html') 

def subjects_page(request): 
    parent=None 
    subject_list = Category.objects.all().filter(parent=parent)
    
    return render (request, 'toplevel/subjects-page.html', {'subject_list':subject_list})
