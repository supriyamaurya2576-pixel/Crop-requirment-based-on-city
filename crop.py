print(" TO HEIP FARMER TO UNDERSTAND IN CROP GROWING")
# Select your city
city=input("Enter your city :")
print("Selecting the sutiable crop according to your city")

#cities
if city=="delhi":
    print("Climate:humid subtropical ,hot semi-arid")
    print("Sutiable: paddy , wheat, jowar")
    sutiable=["paddy","wheat","jowar"]

elif city=="surat":
    print("Climate:tropical climate ,humid")
    print("Sutiable: paddy , wheat, cotton")
    sutiable=["paddy","wheat","cotton"]

elif city=="mumbai":
    print("Climate:humid  ,dry season")
    print("Sutiable: root vegetable, pepper")
    sutiable=["root vegetable","pepper"]

elif city=="chennai":
    print("Climate:Tropical wet and dry climate")
    print("Sutiable: paddy , sugarcane ")
    sutiable=["paddy","sugarcane"]

elif city=="varanasi":
    print("Climate: humid subtropical climate with hot summers")
    print("Sutiable: paddy ,wheat, mustard ")
    sutiable=["paddy","wheat","mustard"]

elif city=="jaipur":
    print("Climate:Subtropical steppe climate  ")
    print("Sutiable:groundnut  ,wheat")
    sutiable=["groundnut","wheat"]

elif city=="bhopal":
    print("Climate:Mediterranean climate and hot summer ")
    print("Sutiable:paddy,maize,wheat")
    sutiable=["paddy","maize","wheat"]

else:
    print("City not found. Showing general crops.\n Your city will enter soon.")
    sutiable=["paddy","wheat"]

print("you can choose from:" ,(sutiable))
crop= input("Enter the crop name:")

print("Crop requirement")

if crop == "paddy":
    print("Soil: Clayey loam")
    print("Temp: 20-35°C")
    print("Water: High (requires standing water)")
    print("Rainfall: 1000-2000 mm")
    print("Season: Kharif")
    print("Growth: 90-180 days")

elif crop == "wheat":
    print("Soil: Loam to clay loam")
    print("Temp: 10-25°C")
    print("Rainfall: 450-650 mm")
    print("Season: Rabi")
    print("Growth: 100-140 days")

elif crop == "mustard":
    print("Soil: Alluvial, well-drained")
    print("Temp: 10-25°C")
    print("Rainfall: 350-450 mm")
    print("Season: Rabi")

elif crop == "sugarcane":
    print("Soil: Loamy soil")
    print("Temp: 20-30°C")
    print("Rainfall: 1200-1500 mm")

elif crop == "groundnut":
    print("Soil: Sandy loam")
    print("Temp: 20-30°C")
    print("Rainfall: 500-700 mm")

elif crop == "jowar":
    print("Soil: Loamy soil")
    print("Temp: 26-33°C")
    print("Rainfall: 400-700 mm")

elif crop == "cotton":
    print("Soil: black soil")
    print("Temp: 25-35°C")
    print("Rainfall: 600-1200 mm")

elif crop == "pepper":
    print("Soil: Loamy soil")
    print("Temp: 18-30°C")
    print("Rainfall: 600-900 mm")

elif crop == "root vegatabel":
    print("Soil: Loamy soil,loose")
    print("Temp: 15-30°C")
    print("Rainfall: 500-800 mm")

else:
    print("Crop details not available.")
    
    







