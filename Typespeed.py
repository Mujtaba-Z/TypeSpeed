import time

input("After you click enter, your typing speed will start being counted ")
start = time.perf_counter()
words = input("Start typing: ")
end = time.perf_counter()
tme = end - start

lit = words.split()
abc = len(lit)
speed = abc/tme * 60
print(tme, '\t', abc, '\t', speed)