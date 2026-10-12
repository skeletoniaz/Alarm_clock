import datetime
import time
import pygame

def set_alarm(alarm_time):
    #print(f"Alarm set for {alarm_time}")
    sound_file="shinra tensei.mp3"

    is_running = True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        # spaces between %H, %M, %S and : matter when you check if ther are same (==)
        #print(current_time)
        if current_time == alarm_time:
            #print("WAKEY WAKEY ELSE ILL BAKE YIU")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.3)
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            is_running = False
            
        time.sleep(1)

def main():
    alarm_time = input("Enter an alarm time (Hours:Minutes:Seconds): ")
    set_alarm(alarm_time=alarm_time)

if __name__=='__main__':
    main()