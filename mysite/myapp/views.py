from django.shortcuts import  render, redirect
from .forms import LoginForm
from .models import MyUserModel ,Product ,Cart
from django.contrib.auth.decorators import login_required


def register(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    address =request.POST.get('address')
    phone = request.POST.get('phone')  

    data = MyUserModel(Email=email, Username=username, Password=password , Address=address, Phone=phone)
    data.save()
    return render(request, 'myapp/signup.html') 
    
    
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = MyUserModel.objects.filter(Username=username, Password=password).first()
            if user:
                # set user session
                request.session['user_id'] = user.id # type: ignore
                return redirect('home')
            else:
                # invalid login
                return render(request, 'myapp/login.html', {'form': form, 'error': 'Invalid login credentials.'})
    else:
        form = LoginForm()
        return render(request, 'myapp/login.html', {'form': form})           


         
def home1(request):
    return render(request ,"myapp/home0.html")

def home(request):
    return render(request ,"myapp/home.html")

def menu(request):
    items = Product.objects.all()
    cont = { "items" : items}
    return render(request ,"myapp/menu.html" , cont )


def profile(request):
    user_id = request.session['user_id']
    user = MyUserModel.objects.get(id=user_id)
    return render(request, 'myapp/profile.html', {'user': user})

def add_to_cart(request):
    return render(request , "myapp/cart.html")


@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product) # type: ignore
    return redirect("home")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product) # type: ignore
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product) # type: ignore
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product) # type: ignore
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear() # type: ignore
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')