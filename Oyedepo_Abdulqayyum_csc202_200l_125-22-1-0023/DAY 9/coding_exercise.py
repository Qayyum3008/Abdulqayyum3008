travel_log=[
   {
        "country": "France",
        "cities":["paris","Lille","Dijion" ],
        "visits":12
    } ,
    {
        "country":"Germany" ,
        "cities":["Berlin", "Hamburg","Stuttgart"],
        "vists":5
        },
] 
# travel_log.append(
#     {
#         "country":"Russia" ,
#         "cities_visted":["Moscow", "Saint petersburg","Stuttgart"],
#         "total_vists":2
#         }
# )

def add_new_country(country_visited,times_visited,cities_visited):
    new_country={}
    new_country["country"]=country_visited
    new_country["visits"]=times_visited
    new_country["cities"]=cities_visited
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow","Saint Petersburg"])
print(travel_log)