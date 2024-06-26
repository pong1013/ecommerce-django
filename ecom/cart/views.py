from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse


def cart_summary(request):
    # Get the cart
    cart = Cart(request)
    cart_prods = cart.get_prods
    return render(request, "cart_summary.html", {"cart_products": cart_prods})


def cart_add(request):
    cart = Cart(request)
    if request.POST.get("action") == "post":
        # get stuff
        product_id = int(request.POST.get("product_id"))
        # lookup product from DB
        product = get_object_or_404(Product, id=product_id)

        # Save to session
        cart.add(product=product)

        # Get cart quantity
        cart_quentity = cart.__len__()

        # Return response
        # response = JsonResponse({"Product Name: ": product.name})
        response = JsonResponse({"Quantity: ": cart_quentity})
        return response


def cart_delete(request):
    pass


def cart_update(request):
    pass
