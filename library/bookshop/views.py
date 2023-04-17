from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views import View


from book.models import Author
from bookshop.models import BookProduct, AddToCart


class ProductsView(View):
    def get(self, request):
        products = BookProduct.objects.all()
        authors = Author.objects.all()
        context = {
            'products': products,
            'authors': authors,
        }
        return render(request, 'shop.html', context)

    def post(self, request):
        authors = Author.objects.all()
        selected_author = request.POST.get('author_id')
        if 'author' in request.POST:
            products = BookProduct.objects.filter(author=request.POST.get('author'))
            context = {
                'authors': authors,
                'products': products,
                'selected_author': selected_author,
            }
            return render(request, 'shop.html', context)
        elif 'product_id' in request.POST:
            product_id = request.POST['product_id']
            product = BookProduct.objects.get(id=product_id)
            addtocart, created = AddToCart.objects.get_or_create(user=request.user, product=product)
            if not created:
                addtocart.quantity += 1
                addtocart.save()
            data = {'success': True}
            return JsonResponse(data)

class ProductItemView(View):
    def get(self, request, product_id):
        product = BookProduct.objects.get(id=product_id)
        context = {
            'product': product
        }
        return render(request, 'productitem.html', context)




