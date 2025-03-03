class Resturant:
    def init(self, res_name, cusine_type):
        self.res_name = res_name
        self.cusine_type = cusine_type
    def describe_restaurant(self):
        print(f"{self.res_name} offers {self.cusine_type}")
    def open_restaurant(self):
        print(f"{self.res_name} is open for business from 9am")

eat = Resturant("Pizza hut", "italian")
eat.describe_restaurant()
eat.open_restaurant()

dine = Resturant("Sushi world", "Japanese")
dine.describe_restaurant()
dine.open_restaurant()

lunch = Resturant("Taco town", "Mexican")
lunch.describe_restaurant()
lunch.open_restaurant()