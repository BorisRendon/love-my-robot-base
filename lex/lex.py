
from flask import Flask,render_template, request
import json, sys, os
from datetime import datetime
app = Flask(__name__)

#sys.path.append('C:/Users/rmfer/Desktop/UFM/Sexto Semestre (2019)/Proyecto final P3/love-my-robot-base/lex/transpiled') #Hacerlo dinamico

big_string = ''
def generate_code(test, cond):
    asyncs = ["POP_A_WHEELIE", "ROLL_A_CUBE"]
    for i in test:
        if i[0] in asyncs:
            cond = False
    timestamp = str(datetime.now()).replace(' ', '_').replace(':','_')
    with open('transpiled/cozmo_generated_program.py', '+w') as f:
        if cond:
            big_string = 'import cozmo\nimport time \nfrom cozmo.util import degrees, distance_mm, speed_mmps\ndef cozmo_program(robot: cozmo.robot.Robot):\n' #verificar async functions
            f.write('import cozmo\nimport time \nfrom cozmo.util import degrees, distance_mm, speed_mmps\ndef cozmo_program(robot: cozmo.robot.Robot):\n')
            for x in test:
                try:
                    f.write('    '+data[x[0]].format(x[1])+'\n')
                    big_string = big_string +'    '+ data[x[0]].format(x[1])+'\n'
                except IndexError:
                    f.write('    '+data[x[0]]+'\n')
                    big_string = big_string +'    '+ data[x[0]]+'\n'
            f.write('\ndef run(cozmo_program):\n    cozmo.run_program(cozmo_program)')
            big_string = big_string + '\ndef run(cozmo_program):\n    cozmo.run_program(cozmo_program)'
        if not cond:
            big_string = 'import cozmo\nimport time \nfrom cozmo.util import degrees, distance_mm, speed_mmps\nasync def cozmo_program(robot: cozmo.robot.Robot):\n'
            f.write('import cozmo \nfrom cozmo.util import degrees, distance_mm, speed_mmps\ndef cozmo_program(robot: cozmo.robot.Robot):\n')
            for y in test:
                try:
                    f.write('    '+data[y[0]].format(y[1])+'\n')
                    big_string = big_string +'    '+ data[y[0]].format(y[1])+'\n'
                except IndexError:
                    f.write('    '+data[y[0]]+'\n')
                    big_string = big_string +'    '+ data[y[0]]+'\n'
            f.write('\ndef run(cozmo_program):\n    cozmo.run_program(cozmo_program)')
            big_string = big_string + '\ndef run(cozmo_program):\n    cozmo.run_program(cozmo_program)'   
    from transpiled import cozmo_generated_program as p
    try:
        p.run(p.cozmo_program)
    except:
        print('DIDNT FINISH')
    os.rename(r'transpiled/cozmo_generated_program.py', r'transpiled/cozmo_generated_program'+str(timestamp)+r'.py')
    return big_string
#reading json file



#en el json falta poner los parámetros de cada funciones para leerlos y jalarlos
data = {
    'DRIVE':'robot.drive_straight(distance_mm({}),speed_mmps(50)).wait_for_completed()',
    'TURN':'robot.turn_in_place(degrees({})).wait_for_completed()',
    'ROLL_CUBE': "await robot.set_head_angle(degrees(-5.0)).wait_for_completed()\n" +
"    print(\"Cozmo is waiting until he sees a cube\")\n" +
"    cube = await robot.world.wait_for_observed_light_cube()\n" +
"    print(\"Cozmo found a cube, and will now attempt to roll with it:\")\n" +
"    action = robot.roll_cube(cube, check_for_object_on_top=True, num_retries=2)\n" +
"    await action.wait_for_completed()\n" +
"    print(\"result:\", action.result)\n",
    'SAY': 'robot.say_text("{}").wait_for_completed()',
    'COUNT': "for i in range({}):\n" +"\n" +"    robot.say_text(str(i+1)).wait_for_completed()\n",
    'SET_ALL_BACKPACK_LIGHTS': "robot.set_all_backpack_lights(cozmo.lights.red_light)\n" +"    time.sleep(2)\n" +"    robot.set_all_backpack_lights(cozmo.lights.green_light)\n" +"    time.sleep(2)\n" +"    robot.set_all_backpack_lights(cozmo.lights.blue_light)\n" +"    time.sleep(2)\n" +"    robot.set_center_backpack_lights(cozmo.lights.white_light)\n" +"    time.sleep(2)\n" +"    robot.set_all_backpack_lights(cozmo.lights.off_light)\n" +"    time.sleep(2)\n",
    'PLAY_ANIM' : "print(\"Playing Animation Trigger 1:\")\n" +"    robot.play_anim_trigger(cozmo.anim.Triggers.CubePounceLoseSession).wait_for_completed()\n" +"    \n" +"print(\"Playing Animation Trigger 2: (Ignoring the body track)\")\n" +"    robot.play_anim_trigger(cozmo.anim.Triggers.CubePounceLoseSession, ignore_body_track=True).wait_for_completed()\n" +"    \n" +"print(\"Playing Animation 3:\")\n" +"    robot.play_anim(name=\"anim_poked_giggle\").wait_for_completed()\n",
    'DRIVE_SQUARE': "for _ in range(4):\n" +
"        robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()\n" +
"        robot.turn_in_place(degrees(90)).wait_for_completed()\n",
    'MOVE_HEAD': "robot.move_head(-5)\n" +
"    robot.move_lift(-5)\n" +
"    robot.drive_wheels(25, 50)\n" +
"    time.sleep(3)\n" +
"    robot.move_head(5)\n" +
"    robot.move_lift(5)\n" +
"    robot.drive_wheels(50, -50)\n" +
"    time.sleep(3)\n",
    'STACK_AND_ROLL': "lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)\n" +
"    cubes = robot.world.wait_until_observe_num_objects(num=2, object_type=cozmo.objects.LightCube, timeout=10)\n" +
"    print(\"Found %s cubes\" % len(cubes))\n" +
"    lookaround.stop()\n" +
"    if len(cubes) == 0:\n" +
"        robot.play_anim_trigger(cozmo.anim.Triggers.MajorFail).wait_for_completed()\n" +
"    elif len(cubes) == 1:\n" +
"        robot.run_timed_behavior(cozmo.behavior.BehaviorTypes.RollBlock, active_time=60)\n" +
"    else:\n" +
"        robot.run_timed_behavior(cozmo.behavior.BehaviorTypes.StackBlocks, active_time=60)\n",
    'PICKUP_FURTHEST': "lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)\n" +
"    cubes = robot.world.wait_until_observe_num_objects(num=3, object_type=cozmo.objects.LightCube, timeout=60)\n" +
"    lookaround.stop()\n" +
"    max_dst, targ = 0, None\n" +
"    for cube in cubes:\n" +
"        translation = robot.pose - cube.pose\n" +
"        dst = translation.position.x ** 2 + translation.position.y ** 2\n" +
"        if dst > max_dst:\n" +
"            max_dst, targ = dst, cube\n" +
"    if len(cubes) < 3:\n" +
"        print(\"Error: need 3 Cubes but only found\", len(cubes), \"Cube(s)\")\n" +
"    else:\n" +
"        robot.pickup_object(targ, num_retries=3).wait_for_completed()\n",
    'POP_A_WHEELIE': "print(\"Cozmo is waiting until he sees a cube\")\n" +
"    cube = await robot.world.wait_for_observed_light_cube()\n" +
"    print(\"Cozmo found a cube, and will now attempt to pop a wheelie on it\")\n" +
"    action = robot.pop_a_wheelie(cube, num_retries=2)\n" +
"    await action.wait_for_completed()\n"
}

#revisar COZMO.UTIL para sacar medidas y datos
instruc = []
@app.route('/Lex', methods=['POST'])
def lex():
    global big_string
    global instruc
    boolean = True
    req_data = request.get_json()
    instrucciones = req_data['lmr']
    leer_instrucciones(instrucciones)
    big_string = generate_code(instruc, boolean)
    instruc = []
    return '{}'.format(big_string)
@app.route('/')
def hello_world():
   
    global big_string
    return render_template("index.html", big_string=big_string)

def leer_instrucciones(lista):
    for i in lista:
        instruc.append(i.split('&', 1))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
