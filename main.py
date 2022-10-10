import time
import dashboard_client
import rtde_receive

ipAddress = "172.31.0.101"

robot1 = dashboard_client.DashboardClient(ipAddress)
robot1_receive = rtde_receive.RTDEReceiveInterface(ipAddress)

robot1.connect()
print(robot1.isConnected())
robot1.loadURP("moveBToC.urp")
robot1.play()
print("Program is running")
time.sleep(1)
while robot1.running():
    if robot1_receive.getDigitalOutState(17):
        print("Tool digital out (17) is HIGH")
    else:
        print("Tool digital out (17) is LOW")

    time.sleep(0.05)
print("Program is finished")
