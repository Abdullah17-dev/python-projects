import time
def countdown_timer(total_time):
    try:
        while total_time:
            minutes, seconds = divmod(total_time,60)
            format_time = f"{minutes:02d}:{seconds:02d}"
            print(f"Remaining time: {format_time}", end='\r')
            time.sleep(1)
            total_time -= 1
        print("\ntime up!")
    except KeyboardInterrupt:
        print("Timer interrupted by user.")

try:
    minutes = int(input("Enter minuts: "))
    seconds = int(input("Enter seconds: "))
    total_time = minutes * 60 + seconds
    if total_time <=0:
        raise ValueError("Time must be greater than 0.")
    countdown_timer(total_time)
except ValueError as e:
    print("Invalid input", e)
