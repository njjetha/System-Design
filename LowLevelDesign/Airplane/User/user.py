from abc import ABC
from enum_class import *
class User(ABC):
    def __init__(self, name, phone, email, proof:Proof):
        self.name = name
        self.phone = phone
        self.email = email
        self.proof = proof
