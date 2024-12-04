orders=["tea","coffee","tea","coffee","ghee roast","plain roast","porotta","tea"]

order_summary={}

for order in orders:

    if order in order_summary:

        order_summary[order]+=1

    else:

        order_summary[order]=1

print(order_summary)