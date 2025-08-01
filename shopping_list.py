import uuid



class ShoppingListService:
    """Manages a collection of shopping items with basic operations."""

    def __init__(self):
        # Initialize the shopping list with some default items
        self.items = [
            {"id": str(uuid.uuid4()), "name": "Milk", "quantity": 2, "purchased": True},
            {"id": str(uuid.uuid4()), "name": "Bread", "quantity": 1, "purchased": False},
            {"id": str(uuid.uuid4()), "name": "Eggs", "quantity": 12, "purchased": True},
            {"id": str(uuid.uuid4()), "name": "Apples", "quantity": 6, "purchased": False},
            {"id": str(uuid.uuid4()), "name": "Coffee", "quantity": 1, "purchased": False},
        ]

    def get_items(self, purchased=None):
        """Get all items, optionally filtered by completion status."""
        if purchased is None:
            return self.items
        return [item for item in self.items if item["purchased"] == purchased]

    def add_item(self, name, quantity):
        """Add a new item to the shopping list and return its ID."""
        new_item = {
            "id": str(uuid.uuid4()),
            "name": name,
            "quantity": quantity,
            "purchased": False
        }
        self.items.append(new_item)
        return new_item["id"]

    def remove_item(self, item_id):
        """Remove an item from the shopping list by its ID."""
        for i, item in enumerate(self.items):
            if item["id"] == item_id:
                del self.items[i]
                return True
        return False

    def set_purchased(self, item_id, purchased=True):
        """Mark an item as purchased or not purchased by its ID."""
        for item in self.items:
            if item["id"] == item_id:
                item["purchased"] = purchased
                return True
        return False