# Final Exam AIDI 2004 - Subash

class InventoryTracker:
    def addItem(self, name, quantity):
        print(f"Added {quantity} of {name}")
    
    def updateStock(self, item_name, new_quantity):
        """Updates the quantity of an existing inventory item."""
        print(f"Updated {item_name} to {new_quantity}")