from django.http import QueryDict


# from django.http.request import MultiValueDict
# this we will fix .
def queryDict_dict(query_dict):
    """
    desc:This function convert queryDict into dict.
    param:query dictionary.
    return:dict
    """
    print('this is query dict that we get', query_dict)
    query = query_dict.dict()
    print('Here is query', query)
    return query


# OK Tested.
def dict_queryDict(dct):
    """
    desc:This function is used to dict to query_dct.
    parm:dct->This is a dictionary.
    return:query_dict
    """
    queryDict = QueryDict('', mutable=True)
    return queryDict.update(dct)


def find_state_name(state_list, value):
    # To decrease the value because index is start 0 and before convert into int.
    value = int(value) - 1
    for i in range(len(state_list)):
        if value == i:
            return state_list[i].title()


def advanceSearch(query, *desc):
    # converting a string into lower case str list.
    query_list = query.lower().split()
    for item in desc:
        # item = item.lower()
        for search in query_list:
            if search in item.lower():
                return True
    else:
        return False


def userSearch(query, each_product_info):
    """
    parms: query-> This is a user search. each_product_info-> This is an product information(combination)
    like:product information, product name, product description etc...
    return:bool
    """
    # converting each information about product in lowercase.
    product_name_lst = each_product_info.prod_name.lower()
    product_category_lst = each_product_info.category.lower()
    product_desc_lst = each_product_info.prod_desc.lower()
    # calling the advanceSearch() function
    if advanceSearch(query, product_name_lst, product_category_lst, product_desc_lst):
        return True
    return False
    # This is Normal search function.
    # query = query.lower()
    # if query in product_name_lst or query in product_desc_lst or query in product_category_lst:
    #     return True
    # else:
    #     return False
