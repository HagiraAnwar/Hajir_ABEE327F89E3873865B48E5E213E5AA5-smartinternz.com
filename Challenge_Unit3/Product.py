def linearSearchProduct(productList,targetProduct):
  indices = []
  for index,product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)
  return indices
products =["keyboard", "scanner", "mouse", "scanner", "scanner", "printer"]
target = "scanner"
result = linearSearchProduct(products,target)
print(result)
