import dashboard_client

robot1 = dashboard_client.DashboardClient("172.31.0.101")

robot1.connect()
print(robot1.isConnected())
robot1.loadURP("moveBToC.urp")
robot1.play()

while robot1.running():
    print("Program is running")
print("Program is finished")
