import turtle
import math

#all of this was shown in class
class SolarSystem:
        def __init__(self, width, height):
            self.thesun = None
            self.planets = []
            self.ssturtle = turtle.Turtle()
            self.ssturtle = turtle.hideturtle()
            self.ssscreen = turtle.Screen()
            self.ssscreen.setworldcoordinates(-width/2.0,-height/2.0,width/2.0,height/2.0)
            self.ssscreen.tracer(40)

        def addPlanets(self, aplanet):
            self.planets.append(aplanet)

        def addSun(self, asun):
            self.thesun = asun

        def movePlanets(self):
            G = .1
            dt = .001

            for p in self.planets:
                p.moveTo(p.getXPos() + dt * p.getXVel(), p.getYPos() + dt * p.getYVel())

                rx = self.thesun.getXPos() - p.getXPos()
                ry = self.thesun.getYPos() - p.getYPos()
                r = math.sqrt(rx**2 + ry**2)

                gravityx = G * self.thesun.getMass()*rx/r**3
                gravityy = G * self.thesun.getMass()*ry/r**3

                p.setXVel(p.getXVel() + dt * gravityx)

                p.setYVel(p.getYVel() + dt * gravityy)


#all of this was also shown in class 
class Sun:
    def __init__(self, sname, srad, smass):
        self.name = sname
        self.radius = srad
        self.mass = smass
        self.x = 0
        self.y = 0

        self.sturtle = turtle.Turtle()
        self.sturtle.color("yellow")
        self.sturtle.shape("circle")

    def getRadius(self):
        return self.radius
    def getMass(self):
        return self.mass
    def getXPos(self):
        return self.x
    def getYPos(self):
        return self.y
    
#this too was shown in class
class Planet:
    def __init__(self, pname, prad, pmass, pdist, pvx, pvy, pcolor):
        self.name = pname
        self.radius = prad
        self.mass = pmass
        self.distance = pdist
        self.x = pdist
        self.y = 0
        self.velocityx = pvx
        self.velocityy = pvy
        self.color = pcolor

        self.pturtle = turtle.Turtle()
        self.pturtle.up()
        self.pturtle.color(self.color)
        self.pturtle.shape("circle")
        self.pturtle.shapesize(self.radius / 100, self.radius / 100)
        self.pturtle.goto(self.x,self.y)
        self.pturtle.down()

    def getName(self):
        return self.name

    def getRadius(self):
        return self.radius
    
    def getMass(self):
        return self.mass
    
    def getDistance(self):
        return self.distance
    
    def getXPos(self):
        return self.x
    
    def getYPos(self):
        return self.y
    
    def getXVel(self):
        return self.velocityx
    
    def getYVel(self):
        return self.velocityy
    
    def moveTo(self, newx, newy):
        self.x = newx
        self.y = newy
        self.pturtle.goto(newx, newy)

    def setXVel(self, newvelx):
        self.velocityx = newvelx

    def setYVel(self, newvely):
        self.velocityy = newvely


def createSSandAnimate():
    ss = SolarSystem(2,2)

    sun = Sun("SUN", 5000, 10)
    ss.addSun(sun)

    m = Planet("MERCURY", 30.0, 2700, 0.125, 0, 2.5, "grey")
    ss.addPlanets(m)
    
    v = Planet("VENUS", 40.0, 2250, 0.2, 0.6, 2.0, "brown")
    ss.addPlanets(v)
    
    e = Planet("EARTH", 65.0, 5000, 0.3, 0, 2.0, "green")
    ss.addPlanets(e)

    a = Planet("MARS", 57.5, 4500, 0.5, 0, -1.45, "red")
    ss.addPlanets(a)

    j = Planet("JUPITER", 200, 12000, 0.8, 0.1, 1.2, "tan")
    ss.addPlanets(j)

#instead of going through the work to make a rings class, it's just a series of coloured circles overlapping
    sr1 = Planet("SATURNRING1", 190, 0, 0.95, 0.1, 1.15, "sienna")
    ss.addPlanets(sr1)

    sr2 = Planet("SATURNRING2", 180, 0, 0.95, 0.1, 1.15, "burlywood")
    ss.addPlanets(sr2)

    sr3 = Planet("SATURNRING3", 170, 0, 0.95, 0.1, 1.15, "tan")
    ss.addPlanets(sr3)

#and this layer of white just creates the gap between the planet and the rings, if they background of the program is anything other than white this'll look really goofy though
    srw = Planet("CHEESE", 150, 0, 0.95, 0.1, 1.15, "white")
    ss.addPlanets(srw)
    
    s = Planet("SATURN", 120, 75000, 0.95, 0.1, 1.15, "wheat")
    ss.addPlanets(s)
    
    
    numTimePeriods = 20000
    for amove in range(numTimePeriods):
        ss.movePlanets()

createSSandAnimate()
