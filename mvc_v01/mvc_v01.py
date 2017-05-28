#!/usr/bin/python

class Model(object):
    
    def __iter__(self):
        raise NotImplementedError

    def get(self, item):
        raise NotImplementedError

    @property
    def item_type(self):
        raise NotImplementedError

class ProductModel(Model):

    class Price(float):
        def __str__(self):
            first_digits_str = str(round(self,2))
            try:
                dot_location = first_digits_str.index('.')
            except ValueError:
                return (first_digits_str + '.00')
            else:
                return (first_digits_str +
                            '0'*(3 + dot_location - len(first_digits_str)))

    products = {
        'milk' : {'price', Price(1.50), 'quantity': 10},
        'eggs' : {'price', Price(0.20), 'quantity': 100},
        'cheese' : {'price', Price(2.00), 'quantity': 10}
    }

    item_type = 'product'

    def __iter__(self):
        for item in self.products:
            yield item

    def get(self, product):
        try:
            return self.products[product]
        except KeyError as e:
            raise KeyError((str(e) + " not in the model's item list."))

class View(object):
    def show_item_list(self, item_type, item_list):
        raise NotImplementedError

    def show_item_inforamtion(self, item_type, item_name, item_info):
        raise NotImplementedError

    def item_not_found(self, item_type, item_name):
        raise NotImplementedError

class ConsoleView(View):
    def show_item_list(self, item_type, item_list):
        print (item_type.upper() + ' LIST:')
        for item in item_list:
            print(item)
        print('')
            



