import googlemaps
from datetime import datetime
from datetime import timedelta
import museums
import copy
import pprint
import json


gmaps = googlemaps.Client(key="yourkeyhere")

def generate_and_save_id_times_dict():

    with open("times.json", "r") as file:
        times_dict = json.load(file)

    id_time_dict = {}

    for key in times_dict.keys():
        for k in times_dict[key].keys():
            times_dict[key][k] /= 60

    for key, value in times_dict.items():
        for m in museums:
            if key == m.name:
                id_time_dict[int(m.id)] = {}
                for key1, value1 in value.items():
                    for m1 in museums:
                        if key1 == m1.name:
                            id_time_dict[int(m.id)][int(m1.id)] = value1


    with open("id_times.json", "w") as id_times_file:
        json.dump(id_time_dict, id_times_file)


if __name__ == "__main__":

    """
    for m in museums:
        print("------------------")
        m.print_data()
    """

    #general_location = ", Salta, Salta, Argentina"

    dep_time = datetime.now() - timedelta(hours=11)

    print(dep_time)
    #print(datetime.strftime(dep_time, "%S"))

    final_dict = {}
    for i, m in enumerate(museums):
        """
        if "religion" in m.tags or m.requires_appointment or m.name != "MAAM":
            continue
        """
        dest_museums = copy.deepcopy(museums)
        del dest_museums[i]
        final_dict[m.name] = {}
        for dm in dest_museums:
            """
            if "religion" in m.tags or m.requires_appointment:
                continue
            """
            
            result = gmaps.directions(m.address, dm.address, mode="transit", departure_time=dep_time)

            final_dict[m.name][dm.name] = result[0]["legs"][0]["duration"]["value"]

    with open("times.json", "w") as file:
        json.dump(final_dict, file)

    """
    pp = pprint.PrettyPrinter()
    pp.pprint(final_dict)
    """

    generate_and_save_id_times_dict()
