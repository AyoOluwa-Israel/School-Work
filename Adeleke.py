# Request for the sample data.
n = int(input("Enter the number of times to roll the dice: "))
# Create an empty list to store all the values.
values = []


# Function to confirm that the number of times to roll the dice
# is equal to the  number nof values entered.

def confirm_number():
  while True:
    r = int(input("Value of die thrown: "))
    # Add all values into the earlier declared empty list.
    values.append(r)

    if n == len(values):
      print("All Values Received")
      return


# Calculate the Arithmetic mean.
def mean():
  arithmetic_mean = sum(values) / n
  return arithmetic_mean


# Calculate the Median.
def median():
  # Determine the middle position.
  middle_position = len(values) / 2
  # Sort all the new values in the new_values list because it"s an ungrouped data.
  new_values = sorted(values)
  # Algorithim to confirm when middle_position is even.
  if n % 2 == 0:
    return (new_values[int(middle_position - 1)] + new_values[int(middle_position)]) / 2
  # Algorithim to confirm when middle_position is odd.
  elif n % 2 == 1:
    return new_values[int(middle_position)]


# Function to Calculate the Range.
def range():
  new_values = sorted(values)
  max_value = len(new_values)
  # Since all python indexing starts from 0 all arithemtic test by python is minus 1.
  range = new_values[int(max_value) - 1] - new_values[0]
  return range


# Function to calculate the mean deviation.
def mean_deviation():
  # Loop through the values List.
  global mean_value
  for value in values:
    mean_value = float(value - mean())
    # Algorithm to check if the vaLue if the mean_value
    # is negative or positive just to get the absolute.
    if mean_value < 0:
      return mean_value * -1
    elif mean_value > 0:
      return mean_value
    # Equation in stated here

  y = mean_value / n
  return y


# Function to calculate the Standard Deviation.
def standard_deviation():
  for value in values:
    mean_value = float(value - mean())
  x = ((mean_value) ** 2 / n) ** 0.5
  return x


# Function to calculate the Coefficient of Variation
def coefficient_of_variation():
  coefficient_of_variation = (standard_deviation() / mean()) * 100
  return coefficient_of_variation


# Invoke all the functions created.
confirm_number()
mean()
median()
range()
mean_deviation()
standard_deviation()
coefficient_of_variation()

# Display the Results in the console.
print(sum(values))
print("Length = ", len(values))
print("Mean = ", mean())
print("Median = ", median())
print("Range = ", range())
print("Mean Deviation = ", mean_deviation())
print("Standard Deviation = ", standard_deviation())
print("Coefficient of Variation =", coefficient_of_variation())
