from math import ceil

from django.http import HttpResponse

from django.shortcuts import render
import json
from .models import Product, Contact, Orders, OrderUpdate
from .utils import find_state_name, dict_queryDict, queryDict_dict, userSearch


# Create your views here.
def index(request):
    product = Product.objects.all().values()
    list_of_products = []
    # To get the item category.
    catgory_of_products = Product.objects.all().values('category')
    # using set comprehensions we get unique category of products.
    unique_category = {items['category'] for items in catgory_of_products}
    unique_category = list(unique_category)
    # this logic is used to show product category wise.
    for cat in unique_category:
        product = Product.objects.filter(category=cat)
        # find the length of each category  product
        n = len(product)
        # To find the slides of each category product that we will require to show
        # the products.
        nslides = int(n // 4 + ceil((n / 4) - (n // 4)))
        list_of_products.append([product, range(1, nslides), nslides])

    params = {'allProds': list_of_products}
    return render(request, "eshop/index.html", params)


def about(request):
    return render(request, "eshop/about.html")


def contact(request):
    if request.method == "POST":
        user_name = request.POST.get('name', '')
        user_email = request.POST.get('email', '')
        user_contact_number = request.POST.get('number', '')
        user_desc = request.POST.get('query', '')
        user_data = Contact(name=user_name, email=user_email, phone=user_contact_number, desc=user_desc)
        # save the data into the database.
        user_data.save()
    return render(request, "eshop/contacts.html")


def tracker(request):
    if request.method == 'POST':
        user_order_id = request.POST.get('userOrderId', None)
        user_email = request.POST.get('email', None)
        # filter
        update = Orders.objects.filter(order_id=user_order_id, email=user_email)
        # this will get item_json column value.
        items = update[0].item_json
        # this will print all values of update object.
        try:
            if len(update) > 0:
                user_order_update = OrderUpdate.objects.filter(order_id=user_order_id)
                # print(user_order_update)
                # print(user_order_update.values())
                updates = []
                for item in user_order_update:
                    # create a list of dictionary
                    updates.append({'text': item.update_desc, 'time': item.timestamp})

                    # convert object into string
                    dct = {'status': 'success', 'response': items, 'updates': updates}
                    # response = json.dumps([updates, items], default=str)
                    server_response = json.dumps({'status': 'success', 'response': items, 'updates': updates},
                                                 default=str)
                    # here response is a json string that we will send to browser.
                return HttpResponse(server_response)
                # print(updates)
            else:


                # return JsonResponse({"error": "something has error.", "item": 'no item'})
                return HttpResponse({'status': "no Item"})
            # get the all the information about the user then we will do this
            # print(update.values())
        except Exception as e:
            return HttpResponse({'status': "Error"})
    # if request is GET then render this page.
    return render(request, 'eshop/tracker.html')


# is par abhi work karna hai.(design wrong input process.)
def search(request):
    user_product_search = request.GET.get('search', ' ')
    list_of_products = []
    # To get the item category.
    category_of_products = Product.objects.all().values('category')
    # using set comprehensions we get unique category of products.
    unique_category = {items['category'] for items in category_of_products}
    unique_category = list(unique_category)
    # this logic is used to show product category wise.
    for cat in unique_category:
        product_temp = Product.objects.filter(category=cat)
        # here item is each category product.that we are creating list.
        product = [item for item in product_temp if userSearch(user_product_search, item)]
        # find the length of each category  product
        n = len(product)
        # check that if length of products is greater than zero.
        # Then we will make slides otherwise not.
        if n > 0:
            nslides = int(n // 4 + ceil((n / 4) - (n // 4)))
            list_of_products.append([product, range(1, nslides), nslides])

    params = {'allProds': list_of_products, 'msg': ' '}
    if len(list_of_products) == 0:
        params['msg'] = None
    # print(len(list_of_products))
    # print(params)
    return render(request, "eshop/search.html", params)


def product_view(request, myid):
    # get the product with the help of id from database.
    product = Product.objects.filter(id=myid)
    context = {'products': product}
    return render(request, 'eshop/prod_view.html', context)


# this is done.
def checkOut(request):
    lst = ['Andhra Pradesh', 'arunachal pradesh', 'bihar', 'Karnatka', 'uttar pradesh', 'Uttrakhand']
    if request.method == "POST":
        product_json = request.POST.get('item-json', '')
        user_name = request.POST.get('fname', ' ') + " " + request.POST.get('lname', ' ')
        contact_number = request.POST.get('contact', ' ')
        user_email = request.POST.get('email', ' ')
        full_address = request.POST.get('address-1', ' ') + " " + request.POST.get('address-2', ' ')
        user_city = request.POST.get('city', ' ')
        user_state_num = request.POST.get('state', ' ')
        pin_code = request.POST.get('pin-code', ' ')
        state_name = find_state_name(lst, user_state_num)
        data = Orders(name=user_name, phone=contact_number, email=user_email, address=full_address, state=state_name,
                      zip_code=pin_code, city=user_city, item_json=product_json)
        # To save the data into database.
        data.save()
        print(Orders.order_id)
        # Update the orderUpdate database and save the order_id and desc.
        user_order = OrderUpdate(order_id=data.order_id, update_desc='Your order has been placed.')
        # save the user_order
        user_order.save()
        thank = True
        product_id = data.order_id
        context = {'thanks': thank, 'id': product_id, 'states': lst}
        # print('This is a order id:', data.order_id)
        return render(request, 'eshop/checkout.html', context)

    # When page is loaded then simply show the webpage(Because when request is get).
    product_price = Product.objects.all().values('prod_price', 'id')
    # print(product_price)
    params = {'states': lst, 'product_price': product_price}
    return render(request, 'eshop/checkout.html', params)


def practice(request):
    # is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest':
    if request.method == "POST":
        # convert Query dict into dict.
        user_data = request.POST.dict()
        # print(request.POST)
        name = user_data.get('name', None)
        email = user_data.get('email', None)
        query_dict = dict_queryDict(user_data)
        # print('This is query dict:', query_dict)
        a = queryDict_dict(request.POST)
        # print('This is dict:', a)
        # return HttpResponse to the client.
        return HttpResponse("Form Has been Submitted")
    return render(request, 'eshop/practice.html')
