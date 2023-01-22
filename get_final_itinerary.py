from museums import museums
import json
from find_my_itinerary import cyclic_find
from datetime import datetime, timedelta


# returns: [{type:"museum", start_time:60, duration:40, museum:museum}, {type:"travel", time:15},...]
def get_complete_itinerary(itinerary_ids, time_to_spend_at_museums, extra_travel_time):
    with open("id_times.json", "r") as f:
        id_times_dict = json.load(f)
    
    final_itinerary = []
    total_time = 0
    for index, id in enumerate(itinerary_ids):
        
        museum = museums[id]
        if index == 0:
            total_time += extra_travel_time
            final_itinerary.append({"type":"museum", "start_time":total_time, "duration":time_to_spend_at_museums, "museum":museum})
            total_time += time_to_spend_at_museums
            continue

        else:
            travel_time = id_times_dict[str(id)][str(itinerary_ids[index-1])] + extra_travel_time

            final_itinerary.append({"type":"travel", "start_time":total_time, "duration":travel_time})

            total_time += travel_time

            final_itinerary.append({"type":"museum", "start_time":total_time, "duration":time_to_spend_at_museums, "museum":museum})

            total_time += time_to_spend_at_museums

    return final_itinerary


if __name__ == "__main__":
    it_ids = cyclic_find(return_ids=True)
    final_itinerary = get_complete_itinerary(it_ids, 40, 5)
    global_start_time = datetime.strptime("14:00", "%H:%M")
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



