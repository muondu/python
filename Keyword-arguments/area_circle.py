import time
radious = int(input("Enter your radious: "))
def area_of_circle(radius = radious):
    """Area of a circle"""
    area = radius * radious * 3.142
    print("Calculating area...")
    time.sleep(2)
    return area
c = str(area_of_circle())
print("The area of the circle is " + c)