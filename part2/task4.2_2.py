import numpy as np

def calculate_route():
    lengths_input = "20 8 9 18 5 12 16 16 6 7"
    speeds_input = "44 70 44 66 46 38 38 37 66 67"
    k = 4
    p = 7
    
    lengths = np.array([float(x) for x in lengths_input.split()])
    speeds = np.array([float(x) for x in speeds_input.split()])
    
    start_idx = k - 1
    end_idx = p
    
    route_lengths = lengths[start_idx:end_idx]
    route_speeds = speeds[start_idx:end_idx]
    
    total_distance = np.sum(route_lengths)
    times = route_lengths / route_speeds
    total_time = np.sum(times)
    average_speed = total_distance / total_time
    
    print(f"S = {total_distance:.2f} км")
    print(f"T = {total_time:.2f} час")
    print(f"V = {average_speed:.2f} км/ч")

if __name__ == "__main__":
    calculate_route()