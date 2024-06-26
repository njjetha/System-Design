from Component import Character

class BasicCharacter(Character):
    def get_description(self):
        return f"Basic Character"
    
    def get_damage(self):
        return 20