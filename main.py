import tkinter as tk
from datetime import datetime
from pytz import timezone
import pytz

def time_in_timezone(tz_name):
    tz = timezone(tz_name)
    time_now = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S %Z')
    return time_now

def update_time():
    utc_time = time_in_timezone('UTC')
    est_time = time_in_timezone('US/Eastern')
    pst_time = time_in_timezone('US/Pacific')
    cet_time = time_in_timezone('CET')

    label_utc.config(text=f"UTC: {utc_time}")
    label_est.config(text=f"US/Eastern: {est_time}")
    label_pst.config(text=f"US/Pacific: {pst_time}")
    label_cet.config(text=f"CET: {cet_time}")

    root.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock")

label_utc = tk.Label(root, font=('calibri', 40, 'bold'), background='purple', foreground='white')
label_utc.pack(anchor='center')
label_est = tk.Label(root, font=('calibri', 40, 'bold'), background='green', foreground='white')
label_est.pack(anchor='center')
label_pst = tk.Label(root, font=('calibri', 40, 'bold'), background='blue', foreground='white')
label_pst.pack(anchor='center')
label_cet = tk.Label(root, font=('calibri', 40, 'bold'), background='red', foreground='white')
label_cet.pack(anchor='center')


update_time()
root.mainloop()
