from src.scheduler import CloudTaskScheduler
import matplotlib.pyplot as plt

# Run the optimization
print("Starting Genetic Algorithm Optimization...")
scheduler = CloudTaskScheduler(num_tasks=1000, num_vms=50)
best_schedule, final_makespan = scheduler.run()

# Results
print(f"\nOptimization Complete!\nFinal Best Makespan: {final_makespan}")

# Plotting the convergence graph
plt.figure(figsize=(10, 5))
plt.plot(range(1, len(scheduler.best_makespans)+1), scheduler.best_makespans,
         marker='o', linestyle='-', color='blue', linewidth=2, markersize=5)
plt.title('Task Scheduling Optimization Convergence', fontsize=14)
plt.xlabel('Generation', fontsize=12)
plt.ylabel('Best Makespan', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Highlight the best point
min_makespan = min(scheduler.best_makespans)
min_gen = scheduler.best_makespans.index(min_makespan) + 1
plt.scatter(min_gen, min_makespan, color='red', s=100, zorder=5,
            label=f'Best: {min_makespan} (Gen {min_gen})')
plt.legend(fontsize=10)

plt.tight_layout()
plt.show()

