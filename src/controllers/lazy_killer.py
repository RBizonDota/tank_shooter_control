from .defaults import ABSController

from math import atan, pi

ROT_LOSS = 1

class LazyKillerController(ABSController):
    def control(self, field):
        if not field.data:
            return 
        my_tank = field.data["tanks"].get(field.my_tank_id)
        if not my_tank:
            return
        if len(field.data["tanks"])<=1:
            print("No tanks found in area. Waiting enemies")
            return

        # Получение соперника
        enemy = next(iter(field.data["tanks"]))
        while enemy == my_tank["id"]:
            enemy = next(enemy)
        # print("ENEMY FOUND:", enemy, my_tank["id"])

        enemy_tank = field.data["tanks"][enemy]
        dx = enemy_tank["pos"]["x"] - my_tank["pos"]["x"]
        dy = enemy_tank["pos"]["y"] - my_tank["pos"]["y"]
        if dx == 0:
            target_b_az = 0
        else:
            target_b_az = atan(dy/dx)*180/pi
        
        # if dy<0:
        #     target_b_az+=180

        if target_b_az<0:
            target_b_az+=180
        if dy<0:
            target_b_az+=180

        print(target_b_az, my_tank["napr"]["b_az"], abs(my_tank["napr"]["b_az"] - target_b_az))
        if abs(my_tank["napr"]["b_az"] - target_b_az)>ROT_LOSS:
            return {"rotate":0, "b_rotate":1, "move":0, "fire":0}
        else:
            return {"rotate":0, "b_rotate":0, "move":0, "fire":1}