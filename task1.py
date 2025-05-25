import random
import math

def sphere_function(x):
    return sum(xi ** 2 for xi in x)

def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    current = [random.uniform(bound[0], bound[1]) for bound in bounds]
    current_value = func(current)
    
    for i in range(iterations):
        neighbor = []
        for j, bound in enumerate(bounds):
            step = random.uniform(-0.1, 0.1)
            new_coord = current[j] + step
            if new_coord < bound[0]:
                new_coord = bound[0]
            elif new_coord > bound[1]:
                new_coord = bound[1]
            neighbor.append(new_coord)
        
        neighbor_value = func(neighbor)
        
        if neighbor_value < current_value:
            if abs(current_value - neighbor_value) < epsilon:
                break
            current = neighbor
            current_value = neighbor_value
    
    return current, current_value

def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    best = [random.uniform(bound[0], bound[1]) for bound in bounds]
    best_value = func(best)
    
    for i in range(iterations):
        candidate = [random.uniform(bound[0], bound[1]) for bound in bounds]
        candidate_value = func(candidate)
        
        if candidate_value < best_value:
            if abs(best_value - candidate_value) < epsilon:
                break
            best = candidate
            best_value = candidate_value
    
    return best, best_value

def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    current = [random.uniform(bound[0], bound[1]) for bound in bounds]
    current_value = func(current)
    best = current[:]
    best_value = current_value
    temperature = temp
    
    for i in range(iterations):
        if temperature < epsilon:
            break
            
        neighbor = []
        for j, bound in enumerate(bounds):
            step = random.uniform(-0.5, 0.5)
            new_coord = current[j] + step
            if new_coord < bound[0]:
                new_coord = bound[0]
            elif new_coord > bound[1]:
                new_coord = bound[1]
            neighbor.append(new_coord)
        
        neighbor_value = func(neighbor)
        
        if neighbor_value < current_value:
            current = neighbor
            current_value = neighbor_value
            if neighbor_value < best_value:
                best = neighbor[:]
                best_value = neighbor_value
        else:
            delta = neighbor_value - current_value
            probability = math.exp(-delta / temperature)
            if random.random() < probability:
                current = neighbor
                current_value = neighbor_value
        
        temperature *= cooling_rate
    
    return best, best_value

bounds = [(-5, 5), (-5, 5)]

print("Hill Climbing:")
hc_solution, hc_value = hill_climbing(sphere_function, bounds)
print("Розв'язок:", hc_solution, "Значення:", hc_value)

print("\nRandom Local Search:")
rls_solution, rls_value = random_local_search(sphere_function, bounds)
print("Розв'язок:", rls_solution, "Значення:", rls_value)

print("\nSimulated Annealing:")
sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
print("Розв'язок:", sa_solution, "Значення:", sa_value)