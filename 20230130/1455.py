# 김코딩은 용사가 되어 용을 잡으러 간다. 현재 skeleton을 실행하면 아래처럼 잡지 못하는 상황이다.
# 마법을 사용해서 용을 물리치려고 한다. 
# 스켈레톤 파일을 참고하여, 
# 용을 물리칠 수 있도록 Hero의 내장 함수의 set_magic_power를 완성하라.
# HINT: <code>Hero</code>, 그리고 <code>Dragon</code>이 
# 상속한 <code>Creature</code> 객체의 attack_target 함수 작동 원리를 분석하라.
# HINT: set_magic_power 함수가 실행되는 위치를 파악하라

class Creature:
	def __init__(self):
		self.hp = 0
		self.attack = 0
		self.deffence = 0

	def attack_target(self, target):
		print(f"{self} attack {target}")
		demage = self.attack - target.deffence
		target.hp -= demage if self.attack > target.deffence else 1
		if target.hp < 0:
			print(f"Oh, {target} is down! I repeat. {target} is down!")
		else:
			print(f"{target}'s hp: {target.hp}")


class Hero(Creature):
	def __init__(self):
		super().__init__()
		self.hp = 150
		self.attack = 10
		self.deffence = 10

	def __str__(self):
		return "Hero"

	def set_magic_power(self):
            self.attack = 500




class Dragon(Creature):
	def __init__(self):
		super().__init__()
		self.hp = 1000
		self.attack = 50
		self.deffence = 100

	def __str__(self):
		return "Dragon"


hero = Hero()
hero.set_magic_power()
dragon = Dragon()
while (hero.hp > 0) and (dragon.hp > 0):
	hero.attack_target(dragon)
	if dragon.hp > 0:
		dragon.attack_target(hero)