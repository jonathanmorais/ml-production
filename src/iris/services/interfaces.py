from abc import ABC, abstractclassmethod

class ILabel(ABC):
    @abstractclassmethod
    def get_label(self):
        pass

class ITrainning:
    @abstractclassmethod    
    def model_training(self):
        pass

class IClassify:
    @abstractclassmethod    
    def classify(self):
        pass