def make_readable(seconds):
    HOUR = 3600
    MIN = 60

    h = seconds // HOUR
    m = (seconds % HOUR) // MIN
    s = seconds % MIN
    
    return f"{h:02}:{m:02}:{s:02}"


print(make_readable(86400))