# youtube time:58:00

class ProductNameReader:
	def ReadFileDataToString(self, product_name):
		with open(product_name, 'r') as file:
			return file.read()
f = ProductNameReader()
print(f.ReadFileDataToString("products.txt"))