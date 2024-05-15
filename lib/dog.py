#!/usr/bin/env python

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    #sets default values for name and breed if none filled in
    def __init__(self, name = 'Fido', breed = 'Mastiff'):
        self.name = name
        self.breed = breed
    
    #getter and setter function for name
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if type(name) == str and (1 <= len(name) <= 25):
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")
    
    name = property(get_name, set_name)

    def get_breed(self):
        return self._breed
    
    #checks if dog name is in list of approved breeds 
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")
    
    breed = property(get_breed, set_breed)

        