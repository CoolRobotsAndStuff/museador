import json
from museums import museums
import datetime
from os import listdir
import os
import glob
import copy


def delete_all_files_in_folder(folder):
    files = glob.glob(folder + "*")
    for f in files:
        os.remove(f)

def filter_permutations(starting_time_str, ending_time_str, time_spent_at_museum, perm_list, museum_list, extra_travel_time=0):
    with open("id_times.json", "r") as f:
        id_times_dict = json.load(f)
    
    starting_time = datetime.datetime.strptime(starting_time_str, "%H:%M")
    ending_time = datetime.datetime.strptime(ending_time_str, "%H:%M")
    starting_time_minutes = starting_time.hour * 60 + starting_time.minute
    ending_time_minutes = ending_time.hour * 60 + ending_time.minute
    final_permutations = []

    for perm in perm_list:
        is_valid = True
        time_count = 0

        for index, item in enumerate(perm):
            closing_time_minutes = museum_list[item].closing_time.hour * 60 + museum_list[item].closing_time.minute
            opening_time_minutes = museum_list[item].opening_time.hour * 60 + museum_list[item].opening_time.minute

            if index == 0:
                travel_time_to_museum = extra_travel_time
            else:
                travel_time_to_museum = id_times_dict[str(perm[index - 1])][str(perm[index])] + extra_travel_time
            
            time_count += travel_time_to_museum

            if starting_time_minutes + time_count < opening_time_minutes:
                time_count = opening_time_minutes - starting_time_minutes
            
            time_count += time_spent_at_museum
            
            if starting_time_minutes + time_count > closing_time_minutes or starting_time_minutes + time_count > ending_time_minutes:
                is_valid = False
                break
            


        if is_valid:
            final_permutations.append(perm)
            
    return final_permutations


#print(len(my_perm_list))
#print(len(filter_permutations("14:00", "23:00", 40, my_perm_list, museums)))

def filter_and_save_permutation_sets(museums, start_time, end_time, time_spent_per_museum, extra_travel_time=0):
    delete_all_files_in_folder("valid_set_permutations/")
    
    all_permutation_files = listdir("set_permutations/")
    perm_files_lenght = len(all_permutation_files)

    file_index = 0
    for i, file_name in enumerate(all_permutation_files):
        with open("set_permutations/" + file_name, "r") as perm_set:
            filtered_permutations = filter_permutations(start_time, end_time, time_spent_per_museum, json.load(perm_set), museums, extra_travel_time=extra_travel_time)
            if len(filtered_permutations):
                with open("valid_set_permutations/set" + str(file_index).zfill(6) + ".json", "w") as valid_perm_set:
                    json.dump(filtered_permutations, valid_perm_set)
                    file_index += 1
        print("First filter: Filtered", i + 1, "out of", perm_files_lenght)

def find_best_itinenary(perm_list):
    with open("id_times.json", "r") as f:
        id_times_dict = json.load(f)
    perm_times = []
    for perm in perm_list:
        time_count = 0
        for index, item in enumerate(perm):
            if index == 0:
                travel_time_to_museum = 0
            else:
                travel_time_to_museum = id_times_dict[str(perm[index - 1])][str(perm[index])]
            time_count += travel_time_to_museum
        perm_times.append(time_count)
    
    min_perm_time = min(perm_times)

    return perm_list[perm_times.index(min_perm_time)]


def convert_ids_to_names(id_list, museum_list):
    final_list = []
    for id in id_list:
        final_list.append(museum_list[id].name)
    
    return final_list

def get_best_itinearies():
    all_permutation_files = listdir("valid_set_permutations/")
    perm_files_lenght = len(all_permutation_files)
    best_itinearies = []

    for i, file_name in enumerate(all_permutation_files):
        with open("valid_set_permutations/" + file_name, "r") as perm_set:
            best_it = find_best_itinenary(json.load(perm_set))
            best_itinearies.append(best_it)
        
        print("Second filter:", i + 1, "out of", perm_files_lenght)
    return best_itinearies

def filter_and_save_best_itineraries():
    itineraries = get_best_itinearies()

    filtered_itineraries = []

    for it in itineraries:
        temp_list = copy.deepcopy(itineraries)
        temp_list.remove(it)
        put_in_list = True
        for temp_it in temp_list:
            if all(item in temp_it for item in it):
                put_in_list = False
        if put_in_list:
            filtered_itineraries.append(it)

    print("Total itineraries:", len(itineraries))

    print("Filtered itineraries:", len(filtered_itineraries))

    with open("best_itineraries.json", "w") as best_it_file:
        json.dump(filtered_itineraries, best_it_file, sort_keys=True)


def find_and_save_valid_itineraries(museums, start_time, end_time, time_spent_per_museum, extra_travel_time=0):
    filter_and_save_permutation_sets(museums, start_time, end_time, time_spent_per_museum, extra_travel_time)
    filter_and_save_best_itineraries()

if __name__ == "__main__":
    find_and_save_valid_itineraries(museums, "14:00", "23:00", 40, 5)

