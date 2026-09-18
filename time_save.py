from datetime import datetime

current_time = datetime.now()

with open("timer.txt", "w") as f:
    f.write(str(current_time))

print("Time Saved:", current_time)