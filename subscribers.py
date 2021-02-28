import time
import os
import random
rang = range(0,3)
Minecrafter1999_subscribers = 2000
DoctorHto_subscribers = 50
while True:
    Minecrafter1999_subscribers = Minecrafter1999_subscribers + random.choice(rang)
    DoctorHto_subscribers = DoctorHto_subscribers + random.choice(rang)
    dif_Minecrafter1999_subscribers_and_DoctorHto_subscribers = Minecrafter1999_subscribers - DoctorHto_subscribers
    print("у Minecrafter1999", Minecrafter1999_subscribers,"подписчиков")
    print("у DoctorHto", DoctorHto_subscribers,"подписчиков")
    print("У Minecrafter1999 на", dif_Minecrafter1999_subscribers_and_DoctorHto_subscribers,"чем у DoctorHto")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
    
    
    
