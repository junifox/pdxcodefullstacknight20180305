
def km_m(distance):
    return(distance*1000)
def mi_m(distance):
    return(distance*1609.34)
def m_m(distance):
    return(distance*1)
def ft_m(distance):
    return(distance*0.3048)
def m_km(distance):
    return(distance/1000)
def m_mi(distance):
    return(distance/1609.34)
def m_m(distance):
    return(distance/1)
def ft_m(distance):
    return(distance/0.3048)


print("Welcome")
distance = int(input("What is the distance?"))
input_units = input("What are the input units?")
output_units = input("What are the output units?")
meter_conversion = 0


if input_units == "km":
    meter_conversion = km_m(distance)
elif input_units == "mi":
    meter_conversion = mi_m(distance)
elif input_units == "m":
    meter_conversion = m_m(distance)
elif input_units == "ft":
    meter_conversion = ft_m(distance)
else:
    print("Invalid")


if output_units == "km":
    print(m_km(meter_conversion), output_units)
elif output_units == "mi":
    print(m_mi(meter_conversion), output_units)
elif output_units == "m":
    print(m_m(meter_conversion), output_units)
elif output_units == "ft":
    print(m_ft(meter_conversion), output_units)
