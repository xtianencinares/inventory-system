class InventorySystem:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_name, quantity):
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity
        print(f"Added {quantity} {item_name}(s) to the inventory.")

    def update_quantity(self, item_name, new_quantity):
        if item_name in self.inventory:
            self.inventory[item_name] = new_quantity
            print(f"Updated {item_name} quantity to {new_quantity}.")
        else:
            print(f"{item_name} not found in the inventory.")

    def display_inventory(self):
        print("Current Inventory:")
        for item_name, quantity in self.inventory.items():
            print(f"{item_name}: {quantity}")

# Example usage:
inventory_system = InventorySystem()

inventory_system.add_item("Laptop", 5)
inventory_system.add_item("Monitor", 10)
inventory_system.add_item("Keyboard", 20)

inventory_system.display_inventory()

inventory_system.update_quantity("Laptop", 3)
inventory_system.update_quantity("Mouse", 5)  # Item not in the inventory

inventory_system.display_inventory()
