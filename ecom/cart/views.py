from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.contrib import messages


def cart_summary(request):
    # Get the cart
    cart = Cart(request)
    cart_prods = cart.get_prods
    quantities = cart.get_quants
    totals = cart.get_total()
    return render(
        request,
        "cart_summary.html",
        {"cart_products": cart_prods, "quantities": quantities, "totals": totals},
    )


def cart_add(request):
    cart = Cart(request)
    if request.POST.get("action") == "post":
        # get stuff
        product_id = int(request.POST.get("product_id"))
        product_qty = int(request.POST.get("product_qty"))
        # lookup product from DB
        product = get_object_or_404(Product, id=product_id)

        # Save to session
        cart.add(product=product, quantity=product_qty)

        # Get cart quantity
        cart_quentity = cart.__len__()

        # Return response
        response = JsonResponse({"quantity": cart_quentity})
        messages.success(request, ("Product Added to Cart"))
        return response


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get("action") == "post":
        # get stuff
        product_id = int(request.POST.get("product_id"))

        # Save to session
        cart.delete(product=product_id)

        response = JsonResponse({"product": product_id})
        messages.success(request, ("Item Deleted"))
        return response


def cart_update(request):
    cart = Cart(request)
    if request.POST.get("action") == "post":
        # get stuff
        product_id = int(request.POST.get("product_id"))
        product_qty = int(request.POST.get("product_qty"))

        # Save to session
        cart.update(product=product_id, quantity=product_qty)

        # Return response
        response = JsonResponse({"quantity": product_qty})
        messages.success(request, ("Cart Updated"))
        return response
