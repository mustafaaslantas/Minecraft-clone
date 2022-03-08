from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent = scene,
            model = 'cube',
            origin_y = 0.5,
            position= position,
            texture = 'white_cube',
            color = color.white,
            highlight_color= color.lime
            )

for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x,0,z))

player = FirstPersonController()

if player.y < 0:
    player.position = (0,0,0)
voxel = Voxel()
app.run()
        
