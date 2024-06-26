from store.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session

        # Get the current session key
        cart = self.session.get("session_key")

        # If the user is new, no session key!
        if "session_key" not in request.session:
            cart = self.session["session_key"] = {}

        # Make sure cart is available on all pages of site!
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)

        # Logic
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {"price": str(product.price)}
        # if updated the cart, session updated too
        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        # get id from cart
        product_ids = self.cart.keys()
        # use id to lookup prods in DB models by __in ORM method in Django
        products = Product.objects.filter(id__in=product_ids)

        return products
