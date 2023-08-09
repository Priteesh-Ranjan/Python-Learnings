# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 15:55:52 2023

@author: Lenovo
"""
import matplotlib.pyplot as plt
class PIDController:
    def __init__(self, Kp, Ki, Kd, setpoint):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint
        self.error_sum = 0
        self.last_error = 0

    def update(self, measured_value, dt):
        error = self.setpoint - measured_value
        self.error_sum += error * dt
        error_rate = (error - self.last_error) / dt

        control_output = self.Kp * error + self.Ki * self.error_sum + self.Kd * error_rate

        self.last_error = error
        return control_output

desired_value = 10
controller = PIDController(Kp = 1.5 , Ki=2.5, Kd = 0.35, setpoint=desired_value)

# Simulation loop
time_step = 0.01
current_value = 0.0
total_time = 10
total_steps = int(total_time / time_step)

for step in range(total_steps):
    control_output = controller.update(current_value, time_step)
    # Apply the control_output to the system or process, observe the new current_value
    # For simulation purposes, let's update the current_value based on a simple system:
    current_value += control_output * time_step

    print(f"Time: {step * time_step:.2f}, Current Value: {current_value:.2f}, Control Output: {control_output:.2f}")


# Lists to store data for plotting
time_list = []
value_list = []
setpoint_list = []
control_output_list = []

# Simulation loop
for step in range(total_steps):
    control_output = controller.update(current_value, time_step)
    current_value += control_output * time_step

    # Append data to lists for plotting
    time_list.append(step * time_step)
    value_list.append(current_value)
    setpoint_list.append(desired_value)
    control_output_list.append(control_output)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(time_list, value_list, label="Output")
plt.plot(time_list, setpoint_list, label="Setpoint", linestyle='--')
plt.xlabel("Time")
plt.ylabel("Value")
plt.title("PID Controller Output")
plt.legend()
plt.grid(True)
plt.show()