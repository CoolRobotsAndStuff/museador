import json
from museums import museums
import copy


def convert_ids_to_names(id_list, museum_list):
    final_list = []
    for id in id_list:
        final_list.append(museum_list[id].name)
    
    return final_list

def convert_names_to_ids(name_list, museum_list):
    final_list = []
    for name in name_list:
        for museum in museum_list:
            if museum.name == name:
                final_list.append(museum.id)
    return final_list

"""
final_intineraries = copy.deepcopy(all_itineraries)
    
wanted_museums = []
while True:
    all_valid_museums = []
    for itinerary in final_intineraries:
        for item in itinerary:
            if item not in all_valid_museums:
                all_valid_museums.append(item)

    print("\n".join(all_valid_museums))

    final_intineraries = []
    for itinerary in all_itineraries:
        named_itinerary = convert_ids_to_names(itinerary, museums)
        if "MAAM" in named_itinerary and 'Museo de Ciencias Naturales “Lic. Miguel A. Arra”' in named_itinerary:
            final_intineraries.append(named_itinerary)

    print(len(final_intineraries))

    

    with open("final_itineraries.json", "w") as final_it_file:
        json.dump(final_intineraries, final_it_file)
"""

def cyclic_find(return_ids=False):
    with open("best_itineraries.json", "r") as it_file:
        all_itineraries_n = json.load(it_file)
    all_itineraries = []
    for itinerary in all_itineraries_n:
        named_itinerary = convert_ids_to_names(itinerary, museums)
        all_itineraries.append(named_itinerary)
    
    wanted_museums = []

    all_museums = []
    for itinerary in all_itineraries:
        for item in itinerary:
            if item not in all_museums:
                all_museums.append(item)

    possible_museums = copy.deepcopy(all_museums)

    possible_itineraries = copy.deepcopy(all_itineraries)

    while True:
        print()
        print()
        print("Great! There are", len(possible_itineraries), "possible itineraries remaining!")
        print("\n###################")
        print("Your wanted museums are:")
        print("\n".join(wanted_museums))
        print("")

        print("Select most wanted museum:")
        for i, it in enumerate(possible_museums):
            print(i, it)
        print("")
        wanted_museum_n = int(input("Museum number: "))
        wanted_museums.append(possible_museums.pop(wanted_museum_n))

        temp = copy.deepcopy(possible_itineraries)
        for possible_itinerary in temp:
            for wm in wanted_museums:
                if wm not in possible_itinerary:
                    possible_itineraries.remove(possible_itinerary)
                    break
        
        possible_museums = []
        for possible_itinerary in possible_itineraries:
            for item in possible_itinerary:
                if item not in possible_museums and item not in wanted_museums:
                    possible_museums.append(item)
        
        if len(possible_itineraries) <= 1:
            if return_ids:
                return convert_names_to_ids(possible_itineraries[0], museums)
            else:
                return possible_itineraries[0]


if __name__ == "__main__":
    final_itinerary = cyclic_find()
    print("Super! Your final itinerary is:")

    for item in final_itinerary:
        print(item)
        print("    |")
        print("    V")

    print("Done!")