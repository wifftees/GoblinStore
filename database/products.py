class Products: 
    def __init__(self, db) -> None:
        self._products_collection = db.products
    
    
    def get_product_by_id(self, id):
        return self._products_collection.find_one({
            "id": id
        })
        
        
    def get_products_by_category(self, category):
        return self._products_collection.find({
            "category": category
        })
    
    
    
    def add_product(self, product) -> None:
        self._products_collection.insert_one({
            "id": product["id"],
            "product_name": product["product_name"],
            "url": product["url"],
            "description": product["description"],
            "category": product["category"],
        })
        
    def clear_collection(self):
        self._products_collection.delete_many({})
        
    def test_collection(self):
        product = self.get_product_by_id("1")
        print(product["product_name"])