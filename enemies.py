

class Enemy:
    """base class """
    def __init__(self, name, hp, damage):
        """Notes

        :param name: the name of the enemy
        :param hp: the hit points of the enemy
        :param damage: the damage the enemy does with each attack
        """
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0


class Boar(Enemy):
    def __init__(self):
        super().__init__(name="Boar", hp=10, damage=2)


class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp=30, damage=15)
        
        
class Wolf(Enemy):
    def __init__(self):
        super().__init__(name="Wolf", hp=15, damage=5)
	
