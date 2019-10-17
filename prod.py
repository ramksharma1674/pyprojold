from objects import Product

prod2 = Product("laptop", 400, 5)
prod1 = Product("phone price", 250)
prod3 = Product()

print("name:          {:s}".format(prod1.name))
print("Price:        {:.2f}".format(prod1.price))
print("Discount Percent: {:d}%".format(prod1.discountPercent))
print("Discount amount: {:.2f}".format(prod1.getDiscAmount()))
print("Discount Price: {:.2f}".format(prod1.getDiscPrice()))


print("name:          {:s}".format(prod2.name))
print("Price:        {:.2f}".format(prod2.price))
print("Discount Percent: {:d}%".format(prod2.discountPercent))
print("Discount amount: {:.2f}".format(prod2.getDiscAmount()))
print("Discount Price: {:.2f}".format(prod2.getDiscPrice()))


print("name:          {:s}".format(prod3.name))
print("Price:        {:.2f}".format(prod3.price))
print("Discount Percent: {:d}%".format(prod3.discountPercent))
print("Discount amount: {:.2f}".format(prod3.getDiscAmount()))
print("Discount Price: {:.2f}".format(prod3.getDiscPrice()))
