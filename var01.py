print("hola mundo")

vi=2 #int
vf= 2.3 #float (no tiene double)
vc= 'a' #str
vs= 'aaa' #str
vb= True #bool
#dkfjjdfvh

#no necesita espacio, la ',' hace del '+' en java.
print('vi:', vi) #con la , solo puedes concatenar cualq. tipo de dato.

"""
hacer cast (conversion de datos): en vez de ',' un '+' 
 y ahora si hace falta el espacio en lo quue esta entre comillas.
 (str lo convierte en string)

"""
print('vi: '+ str(vi))


vc='2' #una variable puede cambiar de valor durante la ejecucion del programa, antes valia 'a' y ahora '2'.

print('vc:'+ vc) #con el '+' solo puedes concatenar str.

vci=int(vc)
#para mostrar el tipo es 'type'.
print('type vc:' , type(vc))
print('type vci:' , type(vci))

#Phyton permite asignación dinámica de tipos.
vci= True
print('type vci:' , type(vci))

#dos formas de hacer print:
print('vi:', vi, 'vf:', vf, 'vb:', vb)
print(f'vi:{vi}, vf: {vf}, vb:{vb}')

#Expresiones:
a=2
b=3
c=a+b
print('c:', c )
c= a*b
print('c:', c )
c=2 / 3 #division real (decimales)
print('c:', c )
c=2 // 3 #division entera (el cociente y el resto a parte)
print('c:', c )
c= 3%2 #para sacar el resto de la division de esos nums.
print('c:', c )
c= a ** b #potencia (a elevado a b).
print('c:', c )


b0= 3<5 and 7<9
print('b0', b0)
b1= 30<5 and 7<9
print('b1', b1)
