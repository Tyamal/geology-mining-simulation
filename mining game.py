import random

class Resource:
    def __init__(self, name, rarity):
        self.name = name
        self.rarity = rarity

class Player:
    def __init__(self):
        self.inventory = {}
    
    def mine(self, resource):
        if resource.name in self.inventory:
            self.inventory[resource.name] += 1
        else:
            self.inventory[resource.name] = 1
        print(f"You mined a {resource.name}!")

    def show_inventory(self):
        print("Your inventory:")
        for resource, amount in self.inventory.items():
            print(f"{resource}: {amount}")

class MiningGame:
    def __init__(self):
        self.resources = [
            Resource("Gold", 0.1),
            Resource("Silver", 0.3),
            Resource("Copper", 0.5),
            Resource("Diamond", 0.05),
            Resource("Coal", 0.7)
        ]
        self.player = Player()

    def mine_resources(self):
        print("Mining...")
        found_resource = self.find_resource()
        if found_resource:
            self.player.mine(found_resource)
        else:
            print("You found nothing this time.")

    def find_resource(self):
        # Randomly determine if a resource is found based on its rarity
        for resource in self.resources:
            if random.random() < resource.rarity:
                return resource
        return None

    def play(self):
        while True:
            action = input("Enter 'mine' to mine resources, 'inventory' to check your inventory, or 'quit' to exit: ").strip().lower()
            if action == 'mine':
                self.mine_resources()
            elif action == 'inventory':
                self.player.show_inventory()
            elif action == 'quit':
                print("Thanks for playing!")
                break
            else:
                print("Invalid action. Please try again.")

if __name__ == "__main__":
    game = MiningGame()
    game.play()
