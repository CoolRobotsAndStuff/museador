from museums import museums, museum_id_list
from calculate_convinations import generate_and_save_possible_convinations
from find_valid_convinations import find_and_save_valid_itineraries
from find_my_itinerary import cyclic_find, convert_ids_to_names


print("Hello! Welcome to the Museum Speedrun Generator")
print("Visit the most museums in Salta city in the most efficient way possible!")
print('Enter "e" at any moment to exit')


print()
print("Now all possible convinations will be generated.")
print("This step takes a loooong time. If you have already done it you can skip it.")

input1 = input("Do you want to skip it? (y/n):")
if input1 == "e":
    raise Exception

if input1 == "n":
    generate_and_save_possible_convinations(museums, museum_id_list)

print()
print("Now the data will be filtered.")
input1 = input("Do you want to skip this step? (y/n):")
if input1 == "e":
    raise Exception

if input1 == "n":
    print("Ok. Please complete these fields:")

    start_time = input("When will you start going to the museums? (HH:MM): ")
    if start_time == "e":
        raise Exception
    end_time = input("When do you want to stop going to the museums? (HH:MM): ")
    if end_time == "e":
        raise Exception
    time_at_museum = int(input("How much time do you want to spend in each museum? (Number of minutes): "))
    if time_at_museum == "e":
        raise Exception
    extra_travel_time = int(input("How much extra time do you want to add to the expected travel times? (Number of minutes): "))
    if extra_travel_time == "e":
        raise Exception

    print("Great! The data will now be filtered. This will take a while.")

    find_and_save_valid_itineraries(museums, start_time, end_time, time_at_museum, extra_travel_time)

print("Ok, finally done. Now it's time to find your ideal museum itinerary")

final_itinerary = cyclic_find(False)
print("Super! Your final itinerary is:")

for item in final_itinerary:
    print(item)
    print("    |")
    print("    V")

print("Done!")

