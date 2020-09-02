temperature = input("Enter temperature: ");
temperature = float(temperature);
unit = input("Enter unit in F/f or C/c: ");
if unit == "C" or unit == "c":
  answer=temperature*1.8+32;
  print(f"{temperature}° in Celsius is equivalent to {answer}° Fahrenheit.")
elif unit == "F" or unit == "f":
  answer=(temperature-32)*5/9;
  print(f"{temperature}° in Fahrenheit is equivalent to {answer}° Celsius.")
else:
  print(f"Invalid unit({unit}).")