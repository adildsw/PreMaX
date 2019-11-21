# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 13:32:08 2019

@author: AdilDSW
"""
import os
import numpy
import pickle
import pandas
import warnings

from sklearn.preprocessing import normalize

warnings.filterwarnings("ignore")

class Predictor:
    def __init__(self):
        self.init_constraints()
        
        return
    
    def init_constraints(self):
        '''
            Function to initialize constraints of different model inputs
        '''
        
        self.air_pressure_constraints = 170
        self.pump_constraints = 51
        
        return
    
    def sanityCheck(self):
        '''
            Input sanity checker
        '''
        
        if self.model != "AIRPRESSURE" and self.model != "PUMP":
            print("[ERROR] Incorrect Model Specified")
            
            return False
        
        if type(self.data) == type(None):
            print("[ERROR] Invalid Data Input")
                
            return False
        
        if self.data.shape[0] != 1:
            print("[ERROR] Invalid Data Input")
                
            return False
        
        if self.model == "AIRPRESSURE":
            if self.data.shape[1] != self.air_pressure_constraints:
                print("[ERROR] Invalid Data Input")
                
                return False
        elif self.model == "PUMP":
            if self.data.shape[1] != self.pump_constraints:
                print("[ERROR] Invalid Data Input")
                
                return False
        
        if os.path.exists(self.dir) is not True:
            print("[ERROR] Model File Not Found")
            
            return False
        
        return True
    
    def loadData(self, data_string):
        '''
            Function to load and process model
        '''
        
        try:
            data = numpy.array(data_string.split(',')).reshape(1, -1)
            data = pandas.DataFrame(data)
            data = pandas.DataFrame(normalize(data))
        except:
            data = None
        
        return data
    
    def predict(self, model, data):
        '''
            Function to predict the class
            
            Parameter Description:
                model : Defines the model used for prediction
                data  : Defines the data whose class is to be predicted
        '''
        
        self.model = model.upper()
        self.data = self.loadData(data)
        self.dir = 'models/{}.sav'.format(self.model)
        
        if self.sanityCheck() is not True:
            
            return None
        
        self.prediction_model = pickle.load(open(self.dir, 'rb'))
        self.predicted_class = self.prediction_model.predict(self.data)
        
        return self.predicted_class[0]
