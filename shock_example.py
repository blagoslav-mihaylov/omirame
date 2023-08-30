import matplotlib.pyplot as plt
import numpy as np
import locale
locale.setlocale(locale.LC_ALL, 'BG_bg')

population = []

for i in range(80):
    population.append({ "age": i, "count": 50000, "births": 0, "deaths": 0 })

birth_rates = [
    { "start_age": 15, "end_age": 19, "per_thousand": 22 },
    { "start_age": 20, "end_age": 24, "per_thousand": 44 },
    { "start_age": 25, "end_age": 29, "per_thousand": 64 },
    { "start_age": 30, "end_age": 34, "per_thousand": 48 },
    { "start_age": 35, "end_age": 39, "per_thousand": 20 },
    { "start_age": 40, "end_age": 44, "per_thousand":  2 },
]

death_rates = [
    { 'start_age': 79, 'end_age': 79, 'per_thousand': 1000 }
]

start_year = 0

def calculate_births(population, birth_rates):
    for birth_rate in birth_rates:
        start_age = birth_rate['start_age']
        end_age = birth_rate['end_age']

        for age_count in population:
            if age_count['age'] >= start_age and age_count['age'] <= end_age:
                age_count['births'] += round(age_count['count'] / 1000 * birth_rate['per_thousand'])

    return population

def calculate_deaths(population, death_rates):
    for death_rate in death_rates:
        start_age = death_rate['start_age']
        end_age = death_rate['end_age']

        for age_count in population:
            if age_count['age'] >= start_age and age_count['age'] <= end_age:
                age_count['deaths'] += round(age_count['count'] / 1000 * death_rate['per_thousand'])

    return population

def update_population(population):
    total_births = sum([obj["births"] for obj in population])

    new_population = [{ "age": 0, "count": total_births, "births": 0, "deaths": 0 }]
    
    for pop_obj in population:
        age = pop_obj["age"]

        if age < 79:
            new_population.append({
                "age": age + 1,
                "count": pop_obj["count"] - pop_obj["deaths"],
                "births": 0,
                "deaths": 0
            })
        elif age == 79:
            last_index = len(new_population) - 1
            new_population[last_index]["count"] += pop_obj["count"] - pop_obj["deaths"]

    return new_population

x_values = []
y_values = []

plt.ion()
fig, ax = plt.subplots()
line, = ax.plot(x_values, y_values)
ax.grid(True)

ax.set_xlabel('Година')
ax.set_ylabel('Население (млн)')

plt.title('Демографски шок')

x_region = np.array([50, 60])
y_lower = np.full_like(x_region, 3000000)
y_upper = np.full_like(x_region, 5000000) 
plt.fill_between(x_region, y_lower, y_upper, color='gray', alpha=0.3, label='Marked Region')

for i in range(300):
    year = start_year + i

    if i >= 50 and i < 60:
        crisis_birth_rates = [{**obj, "per_thousand": obj["per_thousand"] * 0.75} for obj in birth_rates]
        population = calculate_births(population, crisis_birth_rates)
    else:
        population = calculate_births(population, birth_rates)
    
    population = calculate_deaths(population, death_rates)

    fertility = round(sum([2 * obj['births'] / obj['count'] for obj in population]), 2)

    pop_count = sum([obj["count"] for obj in population])
    birth_count = sum([obj["births"] for obj in population])
    death_count = sum([obj["deaths"] for obj in population])

    birth_ratio = birth_count / pop_count

    print(f'Година {year} – Население: {pop_count:n} – Раждания: {birth_count:n} – Умирания: {death_count:n} – Плодовитост: {fertility:n}')

    population = update_population(population)

    x_values.append(year)
    y_values.append(pop_count)

    line.set_data(x_values, y_values)
    ax.relim()
    ax.autoscale_view()

    plt.pause(0.05)

plt.ioff()
plt.show()