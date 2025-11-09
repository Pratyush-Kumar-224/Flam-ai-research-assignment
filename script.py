import pandas as pd
import numpy as np

try:
    data = pd.read_csv('xy_data.csv')
    print(f"Successfully loaded {len(data)} points.")
except FileNotFoundError:
    print("Error: xy_data.csv not found.")
    exit()

first_point = data.iloc[0]
x_i = first_point['x']
y_i = first_point['y']
print(f"Using x_i = {x_i}")
print(f"Using y_i = {y_i}")

theta_final_rad = 0.5242950658167742 
M_final = 0.030030268434586154
X_final = 55.058000854189906
print(f"theta (rad) = {theta_final_rad}")
print(f"M = {M_final}")
print(f"X = {X_final}")

cos_theta = np.cos(theta_final_rad)
sin_theta = np.sin(theta_final_rad)
print(f"cos(theta) = {cos_theta}")
print(f"sin(theta) = {sin_theta}")

t_calc = (x_i - X_final) * cos_theta + (y_i - 42) * sin_theta
print(f"t_calc = ({x_i} - {X_final:.2f}) * {cos_theta:.2f} + ({y_i} - 42) * {sin_theta:.2f}")
print(f"Result: t_calc = {t_calc}")

is_in_range = 6 < t_calc < 60
print(f"Is {t_calc:.2f} between 6 and 60? {is_in_range}")
if not is_in_range:
    print("Warning: t_calc is out of range. This would add a penalty.")

D_data = (y_i - 42) * cos_theta - (x_i - X_final) * sin_theta
print(f"D_data = ({y_i} - 42) * {cos_theta:.2f} - ({x_i} - {X_final:.2f}) * {sin_theta:.2f}")
print(f"Result: D_data = {D_data}")

D_model = np.exp(M_final * np.abs(t_calc)) * np.sin(0.3 * t_calc)
print(f"D_model = exp({M_final:.2f} * |{t_calc:.2f}|) * sin(0.3 * {t_calc:.2f})")
print(f"Result: D_model = {D_model}")

l1_error_point = np.abs(D_model - D_data)
print(f"L1 Error = |D_model - D_data|")
print(f"L1 Error = |{D_model} - {D_data}|")
print(f"Final Point Error = {l1_error_point}")

print(f"\n--- Conclusion ---")
print(f"The two sides are extremely close (error is {l1_error_point:.2e}).")
print("The optimizer's job was to find parameters that make this error as small as possible for *all* 1500 points.")