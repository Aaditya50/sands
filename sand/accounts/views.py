from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .form import CustomerSignUpForm, DealerSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User , Contact , Product
from math import ceil

from django.http import HttpResponse

def register(request):
    return render(request, '../templates/register.html')

class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = '../templates/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class dealer_register(CreateView):
    model = User
    form_class = DealerSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)

                print(username)
                if user.is_customer is True:
                    print(1)
                    user = User.objects.filter(username=username)

                    allProds = []
                    catprods = Product.objects.values('category', 'id')
                    cats = {item['category'] for item in catprods}
                    for cat in cats:
                        prod = Product.objects.filter(category=cat)
                        n = len(prod)
                        nSlides = n // 4 + ceil((n / 4) - (n // 4))
                        allProds.append([prod, range(1, nSlides), nSlides])

                    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
                    # allProds = [[products, range(1, nSlides), nSlides],
                    #             [products, range(1, nSlides), nSlides]]
                    params = {'allProds': allProds,'me': user[0]}
                    return render(request, '../templates/order.html', params)


                    #return render(request, '../templates/order.html', {'me': user[0]}, params)
                if user.is_dealer is True:
                    print(2)
                    user = User.objects.filter(username=username)


                    return render(request, '../templates/dealar.html',{'me': user[0]})

            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, '../templates/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')
def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request,'contact.html')

def feedback(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address','')
        desc = request.POST.get('desc', '')
        feedback = feedback(name=name, email=email, phone=phone ,address=address, desc=desc )
        feedback.save()
    return render(request,'feedback.html')      


def order(request):
        if request.method=="POST":
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            phone = request.POST.get('phone', '')
            address = request.POST.get('address', '')
            city = request.POST.get('city', '') 
            state = request.POST.get('state', '')  
            zip =  request.POST.get('zip', '')
            cardname =  request.POST.get('cardname', '')
            cardnumber =  request.POST.get('cardnumber', '')
            month = request.POST.get('month', '')
            year =  request.POST.get('year', '')
            cvv =  request.POST.get('cvv', '')
            order = order(name=name, email=email, phone=phone, address=address, city=city, state=state, zip=zip, cardname=cardname, cardnumber=cardnumber, month=month, year=year, cvv=cvv)
            order.save()
            messages.success(request, 'SUCCESS! Order Placed. Amazing things will happen when we got consumers like you. Thank You!')
            
        return render(request,'order.html')


def product(request):
    return render(request,'../templates/product.html')    

def profile(request):
    return render(request,'../templates/profile.html') 

def about(request):
    return render(request, '../templates/about.html')