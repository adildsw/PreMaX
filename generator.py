# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 12:59:06 2019

@author: AdilDSW
"""

import os
import numpy
import random
import pandas

class Generator:
    def __init__(self):
        
        return
    
    def sanityCheck(self):
        '''
            Input sanity checker
        '''
        
        if self.model != "AIRPRESSURE" and self.model != "PUMP":
            print("[ERROR] Incorrect Model Specified")
            
            return False
        
        if self.class_type != "NEGATIVE" and self.class_type != "POSITIVE":
            print("[ERROR] Incorrect Class Type Specified")
            
            return False
        
        if os.path.exists(self.dir) is not True:
            print("[ERROR] Model File Not Found")
            
            return False
        
        return True
        
    def generate(self, model, class_type):
        '''
            Function to return generated data based on the model type
            
            Parameter Description:
                model: Defines which model data to generate
                class_type: Defines which class data to generate
        '''
        
        self.model = model.upper()
        self.class_type = class_type.upper()
        self.dir = 'data/{}/'.format(self.model)
        
        if self.class_type == "RANDOM":
            rand = random.randint(0, 1)
            print(rand)
            if rand == 0:
                self.class_type = "NEGATIVE"
            else:
                self.class_type = "POSITIVE"
        
        if self.sanityCheck() is not True:
            
            return None
        
        if self.class_type == "POSITIVE":
            data = pandas.read_csv(self.dir + 'pos.csv')
        elif self.class_type == "NEGATIVE":
            data = pandas.read_csv(self.dir + 'neg.csv')
        
        rand = random.randint(0, (data.shape[0] - 1))
        generated_data = data.iloc[rand]
        generated_data = numpy.array(generated_data)
        generated_data = [str(i) for i in generated_data]
        generated_data = ','.join(generated_data)
        
        return generated_data
    
