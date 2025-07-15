import random

class CloudTaskScheduler:
    def __init__(self, num_tasks=1000, num_vms=50):
        self.num_tasks = num_tasks
        self.num_vms = num_vms
        self.task_durations = [random.randint(1, 10) for _ in range(num_tasks)]
        self.best_makespans = []  # Stores best makespan of each generation

    def calculate_makespan(self, schedule):
        vm_times = [0] * self.num_vms
        for task, vm in enumerate(schedule):
            vm_times[vm] += self.task_durations[task]
        return max(vm_times)

    def create_initial_population(self, pop_size):
        return [[random.randint(0, self.num_vms-1) for _ in range(self.num_tasks)]
               for _ in range(pop_size)]

    def tournament_selection(self, population, tournament_size=10):
        tournament = random.sample(population, tournament_size)
        return min(tournament, key=self.calculate_makespan)

    def crossover(self, parent1, parent2):
        crossover_point = random.randint(1, self.num_tasks - 1)
        return (parent1[:crossover_point] + parent2[crossover_point:],
                parent2[:crossover_point] + parent1[crossover_point:])

    def mutate(self, individual, mutation_rate=0.01):
        for i in range(self.num_tasks):
            if random.random() < mutation_rate:
                individual[i] = random.randint(0, self.num_vms - 1)

    def run(self, num_iterations=100, pop_size=300):
        population = self.create_initial_population(pop_size)

        for generation in range(num_iterations):
            # Find best in current generation
            current_best = min(population, key=self.calculate_makespan)
            current_makespan = self.calculate_makespan(current_best)
            self.best_makespans.append(current_makespan)

            print(f"Generation {generation+1}: Best Makespan = {current_makespan}")

            # Create new population with elitism
            new_population = [current_best]
            while len(new_population) < pop_size:
                parent1 = self.tournament_selection(population)
                parent2 = self.tournament_selection(population)
                child1, child2 = self.crossover(parent1, parent2)
                self.mutate(child1)
                self.mutate(child2)
                new_population.extend([child1, child2])

            population = new_population[:pop_size]

        return population[0], self.best_makespans[-1]
