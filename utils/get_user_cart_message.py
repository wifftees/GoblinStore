def get_user_cart_message(products, user_cart):
    user_cart_products = [
        products.get_product_by_id(product_id) for product_id in user_cart
    ]
    user_cart_products_names = [product["product_name"] for product in user_cart_products]
    user_products_list = ""
    for i, product in enumerate(user_cart_products_names):
        user_products_list += f"{i + 1}.  {product}\n\n"
    return user_products_list
