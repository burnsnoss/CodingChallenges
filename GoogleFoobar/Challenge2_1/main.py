class Radius:
    # ---------------- Attributes ------------------
    a = -1
    b = 1

    # ----------------- Methods --------------------
    def __init__(self, new_a = -1, new_b = 1):
        self.a = new_a
        self.b = new_b

    def __truediv__(self, other_radius):
        return self.getRadius('f') / other_radius.getRadius('f')

    def getRadius(self, rad_type):
        if rad_type == 'i':
            return self.a, self.b
        elif rad_type == 'f':
            return float(self.a) / float(self.b)
        elif rad_type == 's':
            return str(self.a) + ' / ' + str(self.b)
        elif rad_type == 'l':
            return [self.a, self.b]

    def setRadius(self, new_a, new_b):
        self.a = new_a
        self.b = new_b
        return

    def incrementA(self):
        self.a += 1
        return

    def incrementB(self):
        self.b *= 2



class Gear:
    # ---------------- Attributes ------------------
    positon = -1
    index = -1

    radius = Radius()
    minRadius = -1
    maxRadius = -1

    leftDist = -1
    rightDist = -1
    leftIndex = -1
    rightIndex = -1


    # ----------------- Methods --------------------
    def __init__(self, p, i, final = False):
        self.position = p
        self.index = i
        self.leftIndex = i - 1
        if not final:
            self.rightIndex = i + 1
        return

    # ------------------ Gets ----------------------
    def getRadius(self):
        return self.radius

    def getMinRadius(self):
        return self.minRadius

    def getMaxRadius(self):
        return self.maxRadius

    def getPosition(self):
        return self.position

    def getIndex(self):
        return self.index

    def getLeftIndex(self):
        return self.leftIndex

    def getRightIndex(self):
        return self.rightIndex

    def getLeftDist(self):
        return self.leftDist

    def getRightDist(self):
        return self.rightDist

    # ------------------ Sets ----------------------
    def setRadius(self, a, b):
        self.radius.setRadius(a, b)
        return

    def setMinRadius(self, r):
        self.minRadius = r
        return

    def setMaxRadius(self, r):
        self.maxRadius = r
        return

    def setRight(self, dist):
        self.rightDist = dist
        return

    def setLeft(self, dist):
        self.leftDist = dist
        return


    def printGear(self):
        print 'Radius:    ', '\t', self.radius.getRadius('s')
        print 'Position:  ', '\t', self.getPosition()
        print 'Index:     ', '\t', self.getIndex()
        print 'LeftIndex: ', '\t', self.getLeftIndex()
        print 'RightIndex:', '\t', self.getRightIndex()
        print 'LeftDist:  ', '\t', self.getLeftDist()
        print 'RightDist: ', '\t', self.getRightDist()
        print 'MinRadius: ', '\t', self.getMinRadius()
        print 'MaxRadius: ', '\t', self.getMaxRadius()
        



class DoomsdayDevice:
    # ---------------- Attributes ------------------
    positions = []
    gears = []
    distances = []

    # ----------------- Methods --------------------
    # Initialize: read input list and generate gears 
    #  list that will become doomsday device
    def __init__(self, position_list):
        # Set positions list 
        self.positions = position_list

        

    def checkDeviceInputs(self):
        # Check for correct amount of gear positions
        if len(self.positions) < 2 or len(self.positions) > 20:
            return False
        
        for i in range(len(self.positions)):
            # Check to make sure numbers are within correct range
            if self.positions[i] < 1 or self.positions[i] > 10000:
                return False

            if not (i == 0):
                #  Check ascending order as well as being 1 away
                if self.positions[i] <= self.positions[i-1] + 1:
                    return False

        return True


    def generateGearList(self):
        # Generate gears list from positions
        index = 0
        final = False
        for pos in self.positions:
            if index >= (len(self.positions) - 1):
                final = True
            g = Gear(pos, index, final)
            self.gears.append(g)
            index += 1


    def calibrateDistances(self):
        for i in range(len(self.gears)):
            rightPos = self.gears[i+1].getPosition()
            leftPos = self.gears[i].getPosition()
            distance = rightPos - leftPos

            self.distances.append(distance)

            self.gears[i].setRight(distance)
            self.gears[i+1].setLeft(distance)

            if (i + 1) == (len(self.gears) - 1):
                break

        return

    def initializeGearSizeLimits(self):
        # Get gear size limits and run check to make sure radius's add up 
        minDist = min(self.distances)
        minIndex = self.distances.index(minDist)

        print 'MINDEX:', minIndex
        self.gears[minIndex].setMaxRadius(minDist - 1)
        self.gears[minIndex].setMinRadius(1)

        self.gears[minIndex + 1].setMaxRadius(minDist - 1)
        self.gears[minIndex + 1].setMinRadius(1)

        # Set gear ranges to the left
        for i in range(minIndex - 1, -1, -1):
            # diff - min_prev = max_next
            # diff - max_prev = min_next
            maxRad = self.gears[i].getRightDist() - self.gears[i + 1].getMinRadius()
            minRad = self.gears[i].getRightDist() - self.gears[i + 1].getMaxRadius()

            # Check to make sure gear assembly is possible
            if maxRad < minRad or maxRad < 1 or minRad < 1:
                return False
            
            self.gears[i].setMaxRadius(maxRad)
            self.gears[i].setMinRadius(minRad)


        # Set gear ranges to the right
        for i in range(minIndex + 2, len(self.gears)):
            maxRad = self.gears[i].getLeftDist() - self.gears[i - 1].getMinRadius()
            minRad = self.gears[i].getLeftDist() - self.gears[i - 1].getMaxRadius()

            # Check to make sure gear assembly is possible
            if maxRad < minRad or maxRad < 1 or minRad < 1:
                return False
            
            self.gears[i].setMaxRadius(maxRad)
            self.gears[i].setMinRadius(minRad)

        return True


    def simpleGearFitting(self):
        even = ((len(self.gears) % 2) == 0)

        firstGearMin = self.gears[0].getMinRadius()
        firstGearMax = self.gears[0].getMaxRadius()

        firstGearValues = range(firstGearMin, firstGearMax + 1)

        lastGearMin = self.gears[-1].getMinRadius()
        lastGearMax = self.gears[-1].getMaxRadius()

        if even:
            lastGearValues = range(lastGearMax, lastGearMin - 1, -1)
        else:
            lastGearValues = range(lastGearMin, lastGearMax + 1)

        for i in range(len(firstGearValues)):
            if float(firstGearValues[i]) / float(lastGearValues[i]) == 2.0:
                return Radius(firstGearValues[i], 1) 

        return Radius()



    def printDevice(self):
        for g in self.gears:
            print ' '
            print 'GEAR:', g.getIndex()
            g.printGear()
            print ' '
        return





def answer(pegs):
    # Sanitize pegs
    new_pegs = []
    for i in range(len(pegs)):
        peg_str = str(pegs[i])
        if not peg_str.isdigit():
            print 'FAILURE'
            return [-1, 1]
        new_pegs.append(int(pegs[i]))

    dd = DoomsdayDevice(new_pegs)
    check = dd.checkDeviceInputs()
    if not check:
        print 'FAILURE'
        return [-1, 1]
    
    dd.generateGearList()
    dd.calibrateDistances()

    check = dd.initializeGearSizeLimits()
    if not check:
        print 'FAILURE'
        return [-1, 1]

    result = dd.simpleGearFitting()
    dd.printDevice()
    print 'RADIUS:', result.getRadius('s')
    print result.getRadius('l')
    return result.getRadius('l')





if __name__ == '__main__':
    positions = [4, 30, 50]
    answer(positions)                        