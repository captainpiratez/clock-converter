import tkinter as tk
from tkinter import ttk
from datetime import datetime
from pytz import timezone

def time_in_timezone(tz_name):
    tz = timezone(tz_name)
    dt = datetime.now(tz)
    date_str = dt.strftime('%d.%m.%Y')
    time_str = dt.strftime('%H:%M:%S')
    zone_str = dt.strftime('%Z')
    return f"{time_str}  {date_str} {zone_str}"

def update_time():
    utc_time = time_in_timezone('UTC')
    est_time = time_in_timezone('US/Eastern')
    pst_time = time_in_timezone('US/Pacific')
    cet_time = time_in_timezone('CET')

    times = [utc_time, est_time, pst_time, cet_time]
    for i, (_, lbl_time) in enumerate(labels):
        lbl_time.config(text=times[i])

    root.after(1000, update_time)


root = tk.Tk()
root.title("World Digital Clock")
root.geometry("750x485")
root.minsize(750, 485)
root.configure(bg="#282828")
root.resizable(True, True)



# Set up the visual style to make everything look clean and modern
style = ttk.Style()
style.theme_use("clam")
style.configure("TFrame", background="#282828")
style.configure("Clock.TLabel", font=("Segoe UI", 18, "bold"), background="#3c3836", foreground="#ebdbb2", padding=18, relief="groove")
style.configure("Title.TLabel", font=("Segoe UI", 32, "bold"), background="#282828", foreground="#ebdbb2")

main_frame = ttk.Frame(root, style="TFrame")
main_frame.pack(expand=True, fill="both", padx=30, pady=30)

# Add the main title at the top of the window
title = ttk.Label(main_frame, text="World Digital Clock", style="Title.TLabel", anchor="center", justify="center")
title.grid(row=0, column=0, columnspan=2, pady=(0, 30), sticky="n")

# Create labels for each time zone, keeping them in a single column for simplicity
labels = []
zones = [
    ("UTC:", 'UTC'),
    ("US/Eastern:", 'US/Eastern'),
    ("US/Pacific:", 'US/Pacific'),
    ("CET:", 'CET'),
]
for i, (zone_name, tz) in enumerate(zones, start=1):
    lbl_head = ttk.Label(main_frame, text=zone_name, style="Clock.TLabel", anchor="e", justify="right", width=10)
    lbl_time = ttk.Label(main_frame, style="Clock.TLabel", anchor="w", justify="left", width=32)
    lbl_head.grid(row=i, column=0, padx=(25,5), pady=10, sticky="ew")
    lbl_time.grid(row=i, column=1, padx=(5,25), pady=10, sticky="ew")
    labels.append((lbl_head, lbl_time))

for i in range(1, 5):
    main_frame.rowconfigure(i, weight=1)
main_frame.columnconfigure(0, weight=0)
main_frame.columnconfigure(1, weight=1)

update_time()
root.mainloop()
