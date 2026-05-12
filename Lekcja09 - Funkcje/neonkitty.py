import time

# --- FUNKCJA ANIMACJI CZEKANIA ---
def loading_anim(a):
    frames = ['*', '* *', '* * *']
    end_load = time.time() + a

    i = 0

    while time.time() < end_load:
        #frame = frames[i]
        frame = "* " * (i+1) + " " * 10
        
        print(frame + " " * 10, end="\r")
        time.sleep(0.2)

        i += 1
        i = i % 3 # pozwala cyklicznie chodzić po liście

    print("       ", end="\r")

loading_anim(3)
