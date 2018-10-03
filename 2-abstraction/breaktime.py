import time
import webbrowser

link = "https://www.youtube.com/watch?v=oHg5SJYRHA0" # link to video

wait_time = 20  # seconds
total_breaks = 3  # number of breaks throughout the day
break_count = 0  # initialize count

print("This program started on {}".format(time.ctime()))
while break_count < total_breaks:
	time.sleep(wait_time)
	webbrowser.open(link)
	break_count += 1
