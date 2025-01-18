
fileName = "Model.ext"



class ModelSingleton:
    def __init__(self):
        self.Model = None
        
        

    def getModel(self):
        if self.Model is None:
            self.Model = self.LoadModel(fileName)
        return self.Model
