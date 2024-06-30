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

    def get_total(self):
        # Get id from cart
        product_ids = self.cart.keys()
        # use id to lookup prods in DB models by __in ORM method in Django
        products = Product.objects.filter(id__in=product_ids)
        quantities = self.cart

        total = 0

        for k, v in quantities.items():
            # key str -> int
            k = int(k)
            for prod in products:
                if prod.id == k:
                    if prod.is_sale:
                        total += prod.sale_price * v
                    else:
                        total += prod.price * v
        return total

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        # Logic
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {"price": str(product.price)}
            self.cart[product_id] = int(product_qty)
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

    def get_quants(self):
        # Get cart information in session
        quantities = self.cart
        return quantities

    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)
        # Get cart
        cart_stuff = self.cart
        # Update dict
        cart_stuff[product_id] = product_qty

        # if updated the cart, session updated too
        self.session.modified = True

        thing = self.cart
        return thing

    def delete(self, product):
        product_id = str(product)

        # Delete product from cart dict
        if product_id in self.cart:
            del self.cart[product_id]

        # if delete product from cart, session updated too
        self.session.modified = True
