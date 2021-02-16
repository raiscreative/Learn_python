name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'blue'
teeth = 'white'
hair = 'brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")


height_in_meters = round(height * 0.0254, 2)
print(height_in_meters)

weight_in_kg = round(weight * 0.453592)
print(weight_in_kg)