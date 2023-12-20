import matplotlib.pyplot as plt
categories=['Category A','Categorya B','Category C','Category D']
values=[25,30,5,40]
plt.bar(categories,values, width=0.2)
plt.xlabel('categories')
plt.ylabel('values')
plt.title('Bar plot Example')
plt.show()