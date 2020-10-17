import sys
#import matplotlib.pyplot as mpl
#import numpy as np
import time
import math

try:
    import sim
except:
    print ('Error import sim. Verify files and settings Coppelia.')

class Connection(object):
    def __init__(self, radius=7.5, showIm=False):
        self.showImage = showIm
        self.magnetStatus = False
        self.craneStatus = False
        self.connectionStatus = False
        self.distanceClaw = 2*math.pi*radius #0 a 360 verificar tamanho total e fazer a conta de comprimento 2*pi*r pra direita aumenta x. Pra esquerda diminui x se chegar ao total volta a 0 se for negativo vai pra 360
        self.currentDistanceClaw = 0  
        self.currentAngleClaw = 0
    def init_connection(self, ip = '127.0.0.1' , port = 19997):
        #print ('Program started')
        sim.simxFinish(-1) # just in case, close all opened connections
        clientID=sim.simxStart(ip, port,True,True,5000,5) # Connect to CoppeliaSim
        if clientID==-1:
            return -1, False
        self.clientID = clientID
        self.connectionStatus = True
        # Get Coppelia Objects ID
        self.boom =  sim.simxGetObjectHandle(clientID,'Atuador_braco',sim.simx_opmode_blocking)[-1]
        self.claw = sim.simxGetObjectHandle(clientID,'Atuador_garra',sim.simx_opmode_blocking)[-1] 
        self.crane = sim.simxGetObjectHandle(clientID,'Atuador_guindaste',sim.simx_opmode_blocking)[-1]
        self.magnet = sim.simxGetObjectHandle(clientID,'suctionPad',sim.simx_opmode_blocking)[-1]
        self.cam = sim.simxGetObjectHandle(clientID,'Vision_sensor',sim.simx_opmode_blocking)[-1]
        self.proximity_sensor = sim.simxGetObjectHandle(clientID,'Proximity_sensor',sim.simx_opmode_blocking)[-1]
        self.err_code,resolution,image = sim.simxGetVisionSensorImage(clientID,self.cam,0,sim.simx_opmode_streaming)
        self.status = sim.simxReadProximitySensor(clientID,self.proximity_sensor,sim.simx_opmode_streaming)[1]

        #if self.showImage:
            # Enables interactive mode for imshow
            #mpl.ion()
        
        return clientID, self.connectionStatus
    
    def convertDistAngle(self, step):
        stepT = step % self.distanceClaw
        self.currentDistanceClaw += stepT
        if self.currentDistanceClaw < 0:
            self.currentDistanceClaw+=self.distanceClaw
        elif self.currentDistanceClaw > self.distanceClaw:
            self.currentDistanceClaw-=self.distanceClaw
        
        self.currentAngleClaw = 360 * self.currentDistanceClaw / self.distanceClaw

        return self.currentAngleClaw

    def actionBoom(self, step):
        if self.craneStatus and self.connectionStatus:
            step *= 0.1
            sim.simxSetJointTargetVelocity(self.clientID,self.boom,step,sim.simx_opmode_oneshot)
            time.sleep(0.2)
            sim.simxSetJointTargetVelocity(self.clientID,self.boom,0,sim.simx_opmode_oneshot)
            ##implement code to calculate the angle
            ##value to circle = v and 0 
            ##self.currentAngleClaw
            self.convertDistAngle(step)

        return self.craneStatus

    def actionCrane(self, step):
        if self.craneStatus and self.connectionStatus:
            step *= 0.1
            sim.simxSetJointTargetVelocity(self.clientID,self.crane,step,sim.simx_opmode_oneshot)
            time.sleep(0.2)
            sim.simxSetJointTargetVelocity(self.clientID,self.crane,0,sim.simx_opmode_oneshot)
        return self.craneStatus

    def actionClaw(self, step):
        if self.craneStatus and self.connectionStatus:
            step *= 0.1
            sim.simxSetJointTargetVelocity(self.clientID, self.claw, step, sim.simx_opmode_oneshot)
            time.sleep(0.2)
            sim.simxSetJointTargetVelocity(self.clientID, self.claw,0,sim.simx_opmode_oneshot)
        return self.craneStatus

    def commandUp(self, step=1):
        return self.actionCrane(step)

    def commandDown(self, step=1):
        stepDown = step*-1
        return self.actionCrane(stepDown)
    
    def commandRight(self, step=1):
        stepLeft = step*-1
        status = self.actionBoom(stepLeft)
        print(status)
        return status

    def commandLeft(self, step=1):
        return self.actionBoom(step)
    
    def commandCraneOnOff(self):
        if self.connectionStatus:
            self.craneStatus= not self.craneStatus
        return self.craneStatus

    def commandMagnetOnOff(self):
        if self.craneStatus and self.connectionStatus:
            sim.simxCallScriptFunction(self.clientID,'Base',sim.sim_scripttype_childscript,'AtuadorIma',[],[],[],bytearray(),sim.simx_opmode_blocking)
            self.magnetStatus = not self.magnetStatus
        return self.magnetStatus

    def commandClawUp(self, step=1):
        return self.actionBoom(step)
    
    def commandClawDown(self, step):
        return self.actionClaw(step*-1)
    
    def getCurrentAngleClaw(self):
        return self.currentAngleClaw
    
    #no implemention yet
    def getCamImage(self, plot = False, save = False):
        # Save or print Sensor Vision Image
        image = None
        if self.craneStatus and self.connectionStatus:
            err_code,resolution,image = self.sim.simxGetVisionSensorImage(self.clientID,self.cam,0,sim.simx_opmode_buffer)
            #img = np.array(image, dtype = np.uint8)
            #img = img.resize([resolution[0],resolution[1],3])
            #mpl.imshow(img,origin='lower')
            #if plot:
            #    mpl.show()
            #if save:
            #    mpl.savefig("teste.jpg")
        return image
    
    def getStatusDist(self):
        if self.craneStatus and self.connectionStatus:
            # Get proximity sensor status
            status = sim.simxReadProximitySensor(self.clientID,self.proximity_sensor,sim.simx_opmode_buffer)[1]
            return status
        return -1
    
    def closeConnection(self):    
        # Before closing the connection to CoppeliaSim, make sure that the last command sent out had time to arrive. You can guarantee this with (for example):
        sim.simxGetPingTime(self.clientID)
        # Now close the connection to CoppeliaSim:
        sim.simxFinish(self.clientID)
