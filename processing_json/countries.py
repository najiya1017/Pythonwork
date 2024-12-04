from json import load

f=open("D:\\python\\luminar\\datasets\\datasets_json\\countries.json",encoding="utf-8")

data=load(f)

# print(len(data))

#print names of country

all_country=[country.get("name") for country in data]

# print(all_country)

#print all region

all_regions=[country.get("region") for country in data]

# print(set(all_regions))

region_count={region:all_regions.count(region) for region in all_regions}

# print(region_count)

#print region with maximum countries

max_country_region=max(region_count,key=lambda d:region_count.get(d))

# print(max_country_region,"-",region_count.get(max_country_region))

#capital of specific country

country="India"

capital=[countrys.get("capital") for countrys in data if countrys.get("name")==country]

# print(capital)

#country with maximum border

country_border={country.get("name"):len(country.get("borders",[])) for country in data}

max_border=max(country_border,key=lambda k:country_border.get(k))

# print(max_border,"-",country_border.get(max_border))

#OR

max_border=max(data,key=lambda country:len(country.get("borders",[]))).get("name")

# print(max_border)

#most populated country

most_populated=max(data,key=lambda country:country.get("population")).get("name")

# print(most_populated)

alpha_3_code=[country.get("borders") for country in data if country.get("name")=="India"][0]

for border in alpha_3_code:

    for country in data:

        if country.get("alpha3Code")==border:

            print(country.get("name"))