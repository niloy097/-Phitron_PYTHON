class User:
    def __init__(self, str_name, str_email, int_password, str_contact) -> None:
        self.str_name = str_name
        self.str_email = str_email
        self.int_password = int_password
        self.str_contact = str_contact

class Admin(User):
    seller_requests = [] #dic of seller prod.'s
    sellers = [] #current sellers
    delivery_man = []
    stocks =  [] #dictionary --> key catagory - val --> lsit of products
    def __init__(self, str_name, str_email, int_password, str_contact) -> None:
        super().__init__(str_name, str_email, int_password, str_contact) 
       
    
    def view_sellers(self):
        print("****************List of all Sellers****************")
        for seller in seller:
            print(seller)
    
    def view_delivary_man(self):
        print("****************List of all Delivery Man****************")
        for del_man in self.delivery_man:
            print(del_man)
            
    def view_seller_request(self):
        print(self.seller_requests)
        
    def add_seller_request(self): #seller_obj will be a class
        # quantity < 10 --> prob. will be not visible
        # el will be visible
        if se
        
        
    def all_delivery_man_request(self, obj_delivery_man): #obj_d_m
        self.delivery_man.append(obj_delivery_man)


''''
dict = {
    
    cat1 : [['pro_name1', 'pro_price1', 'pro_qunti1'],['pro_name2', 'pro_price2', 'pro_qunti2'],['pro_name3', 'pro_price3', 'pro_qunti3']]
    cat2 :
    cat3 :
    
}

'''
class Seller(User):
    total_list_porduct = []
    dd = {} #whole shop
    rattings = []
    products = [] #dict -- k(catagory) -- val(list of prodcnt)
    def __init__(self, str_name, str_email, int_password, str_contact, str_company, str_addresss) -> None:
        super().__init__(str_name, str_email, int_password, str_contact)
    
    def add_product(self, str_catagory, str_producnt_name, int_price, int_quantity):
        
        self.str_catagory = str_catagory
        self.str_producnt_name = str_producnt_name
        self.int_price = int_price
        self.int_quantity = int_quantity
        if str_catagory in self.dd:
            self.dd[str_catagory]['quantity'] += int_quantity
        else:
            self.dd[str_catagory] = {
                "product_name" : str_producnt_name,
                "price" : int_price,
                "quantity" : int_quantity
            }
            
    def request_admin_to_add_product(self, str_catagor): #container_request: 
        Admin.seller_requests.append(dict_pro_list)
        

class Buyer(User):
    def __init__(self, str_name, str_email, int_password, str_contact, int_wallet) -> None:
        self.int_wallet = int_wallet
        super().__init__(str_name, str_email, int_password, str_contact)
    
    def view_products(self):
        print("Which Catagory?")
        cat = (str)(input())