nation_list = ["commonwealth", "italy", "usa", "pan_asia", "france",
               "ussr", "germany", "uk", "japan", "poland", "pan_america"]


def sort_nation(nation):
    """
    Receive nation and return the corresponding order as int
    """
    order_dict = {
        "usa": 1,
        "japan": 2,
        "ussr": 3,
        "germany": 4,
        "uk": 5,
        "poland": 6,
        "pan_asia": 7,
        "france": 8,
        "italy": 9,
        "commonwealth": 10,
        "pan_america": 11
    }
    return order_dict.get(nation, 12)
    

sorted_list = sorted(nation_list, key=sort_nation)
print(sorted_list)
