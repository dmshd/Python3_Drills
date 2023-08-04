from datetime import timedelta


def hour_to_timed(i) -> str:
    """
    Takes an hour as for example : 12h39 and returns
    its timedelta equivalent
    """
    i_split = i.split("h")
    i_hour = timedelta(hours=int(i_split[0]))
    return i_hour + timedelta(minutes=int(i_split[1]))

ms = hour_to_timed(input("Day started  at (example : 08h30) : "))
me = hour_to_timed(input("Lunch started  at (example : 12h15) : "))
ans = hour_to_timed(input("Afternoon started at (example : 13h00) : "))
ane = hour_to_timed(input("Day ended  at (example : 16h45) : "))

morning_hours = me - ms
afternoon_hours = ane - ans
total_worked_time = morning_hours + afternoon_hours
print(f"You actually worked {total_worked_time} today!")
print(type(total_worked_time))
