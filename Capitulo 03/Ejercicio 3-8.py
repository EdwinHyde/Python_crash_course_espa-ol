# 3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
# Store the locations in a list. Make sure the list is not in alphabetical order.
lugares = ['paris', 'san gil', 'nueva zelanda', 'inglaterra', 'dinamarca']

# Print your list in its original order. Don’t worry about printing the list neatly,
# just print it as a raw Python list.
print(lugares)

# Use sorted() to print your list in alphabetical order without modifying the actual list.
print(sorted(lugares))

# show that your list is still in its original order by printing it.
print(lugares)

# Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
print(sorted(lugares, reverse=True))

# Show that your list is still in its original order by printing it again.
print(lugares)

# Use reverse() to change the order of your list. Print the list to show that its order has changed.
lugares.reverse()
print(lugares)

# Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
lugares.reverse()
print(lugares)

# Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
lugares.sort()
print(lugares)

# se sort() to change your list so it’s stored in reverse alphabetical order.
lugares.sort(reverse=True)
print(lugares)

# Print the list to show that its order has changed.
print(lugares)
print(len(lugares))
