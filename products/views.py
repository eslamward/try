from django.shortcuts import render
from .models import Product
from .forms import ProductCreateForm
# Create your views here.

def product_detail_view(request):
	obj = Product.objects.get(id=1)
	context = {
		'product':obj
	}
	return render(request,'product/detail.html',context)


def create_product_view(request):
	if request.method == "POST":
		form = ProductCreateForm(request.POST or None)
		if form.is_valid():
			Product.objects.create(**form.cleaned_data)

	else:
		form =ProductCreateForm()

	context = {
	"form":form
	}

	return render(request,"product/create_product.html",context)