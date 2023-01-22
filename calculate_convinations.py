import json
import pprint
from museums import museums, museum_id_list
from itertools import chain, combinations, permutations

#pp = pprint.PrettyPrinter()


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def depurate_museum_list(tags_to_exclude, museum_list, museum_id_list, avoid_appointment=False):
    if tags_to_exclude is not None:
        for m in museum_list:
            if m.requires_appointment and avoid_appointment:
                museum_id_list.remove(m.id)
                continue
            for t in m.tags:
                if t in tags_to_exclude:
                    museum_id_list.remove(m.id)
            
    return museum_id_list

def generate_and_save_possible_convinations(museums, museum_id_list):
    museum_id_list = depurate_museum_list("religion", museums, museum_id_list, avoid_appointment=True)

    museum_sets = powerset(museum_id_list)
    museum_sets = list(museum_sets)
    museum_set_lenght = len(museum_sets)
    for i, m_set in enumerate(museum_sets):
        with open("set_permutations/set" + str(i).zfill(6) + ".json", "w") as set_perm_file:
            json.dump(list(permutations(m_set)), set_perm_file)

        print("calculated set", i, "out of", museum_set_lenght)

if __name__ == "__main__":
    generate_and_save_possible_convinations(museums, museum_id_list)

