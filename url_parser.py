from urlparse import urlparse
import os.path

path = urlparse('http://www.digikey.it/product-detail/it/kemet/C1206C823KARACTU/399-7093-1-ND/3439529').path


path = os.path.dirname(path)
digikeyid = os.path.basename(path)
path = os.path.dirname(path)
productid = os.path.basename(path)

print(digikeyid + '\n')
print(productid + '\n')
