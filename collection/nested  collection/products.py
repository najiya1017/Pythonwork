products=[
    {"id":1,"title":"s23ultra","brand":"samsung","price":78000},
    {"id":2,"title":"a17","brand":"samsung","price":18000},
    {"id":3,"title":"m50","brand":"samsung","price":16000},
    {"id":4,"title":"pocom3","brand":"poco","price":15000},
    {"id":7,"title":"vivov50","brand":"vivo","price":25000},
    {"id":5,"title":"oppof19pro","brand":"oppo","price":27000},
    {"id":6,"title":"iphone16pro","brand":"apple","price":150000},
    {"id":8,"title":"nokia105","brand":"nokia","price":900},
    {"id":6,"title":"iphone16proplus","brand":"apple","price":150000},

]

# total number of mobiles

print("Total number of mobiles:",len(products))

# print mobile titles

print("Mobile Title:", [p.get("title") for p in products])

# print samsung mobiles

print("Samsung Mobiles:",[p.get("title") for p in products if p.get("brand")=="samsung" ])

#costly mobiles

costly_rate_phone=max(products,key=lambda d:d.get("price"))

costly_price=costly_rate_phone.get("price")

costly_mobiles=[p.get("title") for p in products if p.get("price")==costly_price]

print(costly_mobiles)


#count of samsung mobiles

samsung=[p for p in products if p.get("brand")=="samsung"]

print(len(samsung))

# count of each brand

all_brand=[p.get("brand") for p in products]

all_brand_count={p:all_brand.count(p) for p in all_brand}

print(all_brand_count)