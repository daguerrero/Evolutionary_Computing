'''
NOMBRE: GUERRERO ROMERO DANIEL ALBERTO
MATERIA: EVOLUTIONARY COMPUTING
Programa: Practica 1

En ubuntu debemos instalar las siguientes librerias:

sudo apt-get install python python-tk idle python-pmw python-imaging
sudo apt-get install python-matplotlib
'''
import math
import matplotlib
from Tkinter import * 
matplotlib.use('TkAgg')

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
#from matplotlib.backend_bases import key_press_handler


from matplotlib.figure import Figure
																																				
import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

range_a = -10
range_b = 10
accuracy = 0.1


#--------------------------------   SET PARAMETERS -------------------------------------------------
def set_parameters():
	varText1
	global range_a
  	range_a = float(varText1.get())

  	global range_b
  	range_a = float(varText2.get())

  	global accuracy
  	range_a = float(varText3.get())


#--------------------------------   NUMERICAL METHODS -------------------------------------------------

def methods():
	print 'methods'

def exhaustive(a, b, n, nf):
	x1 = a
	dx = (b-a)/n

	x2 = x1 + dx
	x3 = x2 + dx

	while x3 <= b:
		if functions[nf](x1) >= functions[nf](x2) and functions[nf](x2) <= functions[nf](x3):
			print 'the minimum point lies between  ', x1,  x3
			print 'the minimum point lies between ' + str(x1) + ', ' + str(x3)
			return

		else:
			x1 = x2
			x2 = x3
			x3 = x2+dx

	print 'no minimum exists'

#--------------------------------   OTHERS FUCTIONS -------------------------------------------------

def type_function():
	opc = combo1.get()
  	print '--->', opc
  	options[int(opc)]()


def function1(x):
	return 0.65 - 0.75/(1+x**2) - (0.65*x*np.arctan(1/x))
	
def function2(x):
	return (1-x)**4-(2*x+10)**2

def function3(x):
	return 3*x**2 + 12/x**3 - 5

def function4(x):
	return x*(x-15)

def function5(x):
	return 3*x**4+(x-1)**2

def function6(x):
	return 10 +x**3 - 2*x - 5 * np.exp(x)

def function7(x):
	return x**2-10*np.exp(0.1*x)

def function8(x):
    return (10*x**3+3*x**2+5)**2
    
def function9(x):
    return 0.5/np.sqrt(1+x**2) - (np.sqrt(1-x**2))*(1-(0.5/1+x**2))+x
    
def function10(x):
    return np.e**x -x**3
    	

  #--------------------------------   INTERFACE MATPLOTLIB -------------------------------------------------
	
def plot_f1():
	x  = np.arange(-5.0,5.0,0.01)
	fx = function1(x)
	a.clear()
	a.plot(x,fx)
	fx = np.sin(2*np.pi*x)
	a.plot(x,fx)
	canvas.show()

def plot_f2():
	x  = np.arange(-10.0,10.0,0.01)
	fx =  function2(x)	
	#fx = (1-x)**4-(2*x+10)**2	
	a.clear()
	a.plot(x,fx)
	fx = np.sin(2*np.pi*x)
	a.plot(x,fx)
	canvas.show()

####--------	PARTE MODIFICADA	--------#########

def plot_f3():
	x  = np.arange(-0.5,0.5,0.01)
	fx = function3(x)
	a.clear()
	a.plot(x,fx)
	fx = np.sin(2*np.pi*x)
	
	a.plot(x,fx)
	canvas.show()

def plot_f4():
	x = np.arange(-5.0,5.0,0.01)
	fx = function4(x)
	a.clear()
	a.plot(x,fx)
	fx = np.sin(2*np.pi*x)
	a.plot(x,fx)
	canvas.show()

def plot_f5():
	x = np.arange(-1.0,1.0,0.01)
	fx = function5(x)
	a.clear()
	a.plot(x,fx)	
	fx = np.sin(2*np.pi*x)
	a.plot(x,fx)
	canvas.show()

def plot_f6():
	x = np.arange(-6.0,6.0,0.01)
	fx = function6(x)
	a.clear()
	a.plot(x,fx)
	fx = np.sin(2*np.pi*x)
	a.plot(x,fx)
	canvas.show()

def plot_f7():
	x = np.arange(-10.0,5.0,0.01)
	fx = function7(x) 
	a.clear()
	a.plot(x,fx)
	fx = np.sin(2*np.pi*x)
	a.plot(x,fx)
	canvas.show()

def plot_f8():
	x = np.arange(-2.0,2.0,0.01)
	fx = function8(x)
	a.clear()
	a.plot(x,fx)
	fx = np.sin(2*np.pi*x)
	a.plot(x,fx)
	canvas.show()

def plot_f9():
	x = np.arange(-1.0,1.0,0.01)
	fx = function9(x)
	a.clear()
	a.plot(x,fx)
	fx = np.sin(2*np.pi*x)
	a.plot(x,fx)
	canvas.show()

def plot_f10():
	x = np.arange(-3.0,5.0,0.01)
	fx = function10(x)
	a.clear()
	a.plot(x,fx)
	fx = np.sin(2*np.pi*x)
	a.plot(x,fx)
	canvas.show()


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


options = { 1: plot_f1,
  			2: plot_f2,
  			3: plot_f3,
  			4: plot_f4,
  			5: plot_f5,
  			6: plot_f6,
  			7: plot_f7,
  			8: plot_f8,
  			9: plot_f9,
  			10: plot_f10 }

functions = {
			1: function1,
			2: function2,
			3: function3,
			4: function4,
			5: function5,
			6: function6,
			7: function7,
			8: function8,
			9: function9,
			10: function10 }

#--------------------------------   GRAPHICAL USER INTERFACE Tk-------------------------------------------------

root = Tk.Tk()
root.wm_title('Numerical Methods Optimization')


# a tk.DrawingArea
#----

label1=Label(master=root,text="function")
label1.pack(side=Tk.TOP)

combo1 = Spinbox(master=root, from_=0, to=10, increment=1, textvariable='select...', command=type_function)
combo1.pack(side=Tk.TOP)

label2=Label(master=root,text="range: ")
label2.pack(side=Tk.TOP)

label3=Label(master=root,text="a: ")
label3.pack(side=Tk.TOP)

varText1 = StringVar()
varText1.set("0")

A = Entry(master=root,textvariable=varText1)
A.pack()

label4=Label(master=root,text="b: ")
label4.pack()

varText2 = StringVar()
varText2.set("10")

B = Entry(master=root,textvariable=varText2)
B.pack()


label5=Label(master=root,text="accuracy: ")
label5.pack()

varText3 = StringVar()
varText3.set("0.1")

E = Entry(master=root,textvariable=varText3)
E.pack()

label1=Label(master=root,text="method:")
label1.pack(side=Tk.TOP)

combo2 = Spinbox(master=root, values=('select...','Exhaustive', 'Bounding Phase', 'Bisection Method', 'Fibonacci', 'Golden Section'), command=methods)
combo2.pack(side=Tk.TOP)

button1 = Tk.Button(master=root, text='step by step', command=set_parameters())
button1.pack(side=Tk.TOP)



button2 = Tk.Button(master=root, text='Quit', command=_quit)
button2.pack(side=Tk.BOTTOM)


#--------------------------------   INTERFACE MATPLOTLIB -------------------------------------------------

f = Figure(figsize=(7,3), dpi=100)
a = f.add_subplot(111)
canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()	
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

toolbar = NavigationToolbar2TkAgg( canvas, root )
toolbar.update()
canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

Tk.mainloop()

