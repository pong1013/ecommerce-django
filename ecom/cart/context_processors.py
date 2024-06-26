from .cart import Cart


# Create context processor so our cart can work on all page
def cart(request):
    # Return the default data from out Cart
    return {"cart": Cart(request)}
