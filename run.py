from museums import museums, museum_id_list
from calculate_convinations import generate_and_save_possible_convinations
from find_valid_convinations import find_and_save_valid_itineraries
from find_my_itinerary import cyclic_find, convert_ids_to_names
from get_final_itinerary import get_complete_itinerary
from datetime import datetime, timedelta


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

if input1 == "n":
    

    print("Great! The data will now be filtered. This will take a while.")

    find_and_save_valid_itineraries(museums, start_time, end_time, time_at_museum, extra_travel_time)

print("Ok, finally done. Now it's time to find your ideal museum itinerary")

it_ids = cyclic_find(return_ids=True)
final_itinerary = get_complete_itinerary(it_ids, time_at_museum, extra_travel_time)
global_start_time = datetime.strptime(start_time, "%H:%M")

print("All done! Your itenerary is complete!")
final_input = input("Enter p to print it or s to save it as a file: ")

if final_input == "p":
    print("Start")
    for item in final_itinerary:
        print("  |")
        print("  V")
        print("--------------------------------")
        event_start_time = global_start_time + timedelta(minutes=item["start_time"])
        event_end_time = global_start_time + timedelta(minutes=item["start_time"] + item["duration"])
        print("From", event_start_time.strftime("%H:%M"), "to", event_end_time.strftime("%H:%M"))
        if item["type"] == "museum":
            item["museum"].print_data()
        else:
            print("Travel")

        print("--------------------------------")
else:
    file_name = input("Enter your files name: ")
    with open(file_name + ".txt", "w") as file:
        file.write("")

    with open(file_name + ".txt", "a") as file:
        file.write("MUSEUM SPEEDRUN CALCULATOR\n")

        file.write("\nDe " + start_time + " a " + end_time)
        file.write("\nTiempo por museo: " + str(time_at_museum))
        file.write("\nTiempo extra de transporte: " + str(extra_travel_time))
        
        file.write("\nItinerario:")
        file.write("\n\nInicio")
        for item in final_itinerary:
            file.write("\n  |")
            file.write("\n  V")
            file.write("\n--------------------------------")
            event_start_time = global_start_time + timedelta(minutes=item["start_time"])
            event_end_time = global_start_time + timedelta(minutes=item["start_time"] + item["duration"])
            file.write("\nDe " + event_start_time.strftime("%H:%M") + " a " + event_end_time.strftime("%H:%M"))
            file.write(" (" + str(item["duration"]) + " minutos)")
            if item["type"] == "museum":
                file.write("\n*Museo*\n")
                file.write(item["museum"].get_string())
            else:
                file.write("\nViaje")

            file.write("\n--------------------------------") 

        file.write("\n\n\nHecho por Alejandro de Ugarriza Mohnblatt") 


