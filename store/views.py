from django.shortcuts import get_object_or_404, render
from .models import Category,Product

def categories(request):
    return{
        'categories': Category.objects.all()
    }

def all_products(request):
    products = Product.objects.all() # query sulla products table che colleziona tutti i prodotti
    return render(request, 'store/home.html', {'products':products}) # prende data prende templates e prepara il templates con i dati per inviarlo allo user

def product_detail(request,slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/detail.html', {'product':product})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category) #find anything in db that has this category
    return render(request, 'store/products/category.html',{'category': category,'products':products})


def search(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(title__icontains=query)  # Modify the filter condition based on your requirements
    else:
        products = Product.objects.all()
    return render(request, 'store/search_results.html', {'products': products})