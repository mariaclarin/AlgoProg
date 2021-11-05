v = float(input("Enter the plane's take off speed in m/s : "))
a = float(input("Enter the plane's acceleration in m/s**2 : "))

runway = (v**2)/(2*a)
print(f"The minimum runway length needed for this airplane is {format('{runway} = %.4f' % runway)} meters.")