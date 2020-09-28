import math

# test point charges locations
chargeLocations = [[1,1], [4,2], [-1,3]]

# test point charge values in coulombs
chargeValues = [-1, 5, -3]

# test infinite line charge parellel with the Y-Axis
# location it crosses the x-axis
veritcalLineLocation = 9
verticalCharge       = 3

# test infinite line charge parallel with the X-Axis
# locaiton it crosses the y-axis
horizontalLineLocation = -5
horizontalCharge       = -6

particleLocation = [8,9]

# Coulomb's constant (9x10E9)
K = 9000000000

def calculateChargeComponents(q, r, theta):

	charge = [0.0, 0.0]

	E = (K * q) / (float(r)**float(2.0))

	# x component
	charge[0] = E * math.cos(theta)

	# y component
	charge[1] = E * math.sin(theta)

	return charge

def caclulateTheta(chargeCoords, pointCoords):

	deltaX = abs(chargeCoords[0] - pointCoords[0])
	deltaY = abs(chargeCoords[1] - pointCoords[1])

	return math.atan(deltaY/deltaX)

def calculateDistance(chargeCoords, pointCoords):

	return math.hypot(chargeCoords[0] - pointCoords[0], chargeCoords[1] - pointCoords[1])

xCharge = 0.0
yCharge = 0.0

for index in range(0, 2):

	theta       = caclulateTheta(chargeLocations[index], particleLocation)
	distance    = calculateDistance(chargeLocations[index], particleLocation)
	chargeComps = calculateChargeComponents(chargeValues[index], distance,theta)

	xCharge += chargeComps[0]
	yCharge += chargeComps[1]

# handle the line charges
xCharge += (K * verticalCharge) / (float(abs(veritcalLineLocation - particleLocation[0]))**float(2.0))
yCharge += (K * horizontalCharge) / (float(abs(horizontalLineLocation - particleLocation[1]))**float(2.0))

print("X Charge Component: " + "{:.2e}".format(xCharge))
print("Y Charge Component: " + "{:.2e}".format(yCharge))
