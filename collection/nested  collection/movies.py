movies=[
    {"id":1,"title":"kgf","year":2018,"language":"kannada","run_time":150},
    {"id":2,"title":"kgf2","year":2023,"language":"kannada","run_time":160},
    {"id":3,"title":"goat life","year":2024,"language":"malayalam","run_time":120},
    {"id":4,"title":"avesham","year":2024,"language":"malayalam","run_time":130},
    {"id":5,"title":"vazha","year":2024,"language":"malayalam","run_time":140},
    {"id":6,"title":"arm","year":2024,"language":"malayalam","run_time":150},
    {"id":7,"title":"goat","year":2024,"language":"tamil","run_time":160},

]

print("Total number of movies:",len(movies))

print("Movie Title:", [m.get("title") for m in movies])

print("malayam movies:",[m.get("title") for m in products if m.get("language")=="malayalam" ])


