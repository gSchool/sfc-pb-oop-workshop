"""
You are tasked with developing a system to manage shopping receipts.
The system should allow for adding items to a receipt, calculating subtotals,
and applying tax rates to get the total amount due.
You will need multiple classes in order to accomplish this and one will utilize the other when being invoked.
See example:

receipt = Receipt(.1)
receipt.add_item(ReceiptItem(4, 2.50))
receipt.add_item(ReceiptItem(2, 5.00))

print(receipt.get_subtotal())     # Prints 20
print(receipt.get_total())        # Prints 22


Once your classes are complete, copy and paste the above example below them in order to test their functionality
"""


"""
Write a class that meets these requirements.

Name:       Receipt

Required state:
   * tax rate, the percentage tax that should be applied to the total

Behavior:
   * add_item(item)   # Add a ReceiptItem to the Receipt
   * get_subtotal()   # Returns the total of all of the receipt items
   * get_total()      # Multiplies the subtotal by the 1 + tax rate

"""

"""
Write a class that meets these requirements.

Name:       ReceiptItem

Required state:
   * quantity, the amount of the item bought
   * price, the amount each one of the things cost

Behavior:
   * get_total()          # Returns the quantity * price

Example:
   item = ReceiptItem(10, 3.45)

   print(item.get_total())    # Prints 34.5

"""
class Receipt:
  def __init__(self, taxRate):
    self.taxRate = taxRate
    self.receipt_items = []
    self.subtotal = 0
    self.total = 0

  def add_item(self, item): # Add a ReceiptItem to the Receipt
   self.receipt_items.append(item)
   #return self.receipt_items

  def get_subtotal(self): # Returns the total of all of the receipt items
   for item in self.receipt_items: # list of objects
    self.subtotal = self.subtotal + item.get_total() # get_total from the class ReceiptItem
   return self.subtotal

  def get_total(self): # Multiplies the subtotal by the 1 + tax rate
   self.total = self.subtotal*(1 + self.taxRate)
   return self.total

class ReceiptItem:
   def __init__(self, price, quantity):
     self.price = price
     self.quantity = quantity
     self.total = 0

   def get_total(self):
     self.total = self.quantity*self.price
     return self.total

receipt = Receipt(.1)
receipt.add_item(ReceiptItem(4, 2.50))
receipt.add_item(ReceiptItem(2, 5.00))

print(receipt.get_subtotal())     # Prints 20
print(receipt.get_total())        # Prints 22

item = ReceiptItem(10, 3.45)
print(item.get_total())    # Prints 34.5