mosalas = True
x = float(input(' adad 1 ra vared konid : '))
y = float(input(' adad 2 ra vared konid: '))
z = float(input(' adad 3 ra vared konid : '))
if (x + y < z) :
    mosalas = False
if(z + y < x ):
    mosalas = False
if(z + x < y ):
    mosalas = False
if (mosalas):
    print('tashkil mosalas midahad.')
else:
    print('tashkil mosalas nemidahad!!!')