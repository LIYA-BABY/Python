class Engine():
    EngineType = 'V8'
    def common(self):
        print("In common engine")
    def getEngine(self):
        print("In engine class", self.EngineType)
        return(self.EngineType)

class Wheels():
    WheelType = 'rainTyres'
    def common(self):
        print("In common wheels")

    def getWheels(self):
        print("In wheels class", self.WheelType)
        return(self.WheelType)


class Transmission():
    TransmissionType = 'helical'
    def common(self):
        print("In common transmission")

    def getTransmission(self):
        print("In transmission class", self.TransmissionType)
        return(self.TransmissionType)

class car(Engine,Transmission, Wheels):
    def getCar(self):
        self.EngineType = super().getEngine()
        self.WheelType = super().getWheels()
        self.TransmissionType = super().getTransmission()
        return(self.EngineType, self.WheelType, self.TransmissionType)

car1 = car()
print(car1.getCar())
car1.common()