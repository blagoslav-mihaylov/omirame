import matplotlib.pyplot as plt
import numpy as np
import locale
locale.setlocale(locale.LC_ALL, 'BG_bg')

majority_pop = []
minority_pop = []

for i in range(80):
    majority_pop.append({ "age": i, "count": 48000, "births": 0, "deaths": 0 })
    minority_pop.append({ "age": i, "count":  2000, "births": 0, "deaths": 0 })

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

    #for pop in new_population:
    #    print(pop)

    return new_population

x_values = []
y_values1 = []
y_values2 = []

plt.ion()
fig, ax = plt.subplots()
line1, = ax.plot(x_values, y_values1, label='Мнозинство')
line2, = ax.plot(x_values, y_values2, label='Малцинство')
ax.legend()
ax.grid(True)

ax.set_xlabel('Година')
ax.set_ylabel('Население (млн)')

plt.title('Симулация на демография')

start_year = 2022

for i in range(250):
    year = start_year + i

    # българска фертилност - 1,41
    # ромска фертилност - 2,25

    majority_birth_rates = [{**obj, "per_thousand": obj["per_thousand"] * 1.41 / 2} for obj in birth_rates]
    minority_birth_rates = [{**obj, "per_thousand": obj["per_thousand"] * 2.25 / 2} for obj in birth_rates]

    majority_pop = calculate_births(majority_pop, majority_birth_rates)
    majority_pop = calculate_deaths(majority_pop, death_rates)

    minority_pop = calculate_births(minority_pop, minority_birth_rates)
    minority_pop = calculate_deaths(minority_pop, death_rates)

    majority_fertility = round(sum([2 * obj['births'] / obj['count'] for obj in majority_pop]), 2)
    minority_fertility = round(sum([2 * obj['births'] / obj['count'] for obj in minority_pop]), 2)

    majority_pop_count = sum([obj["count"] for obj in majority_pop])
    minority_pop_count = sum([obj["count"] for obj in minority_pop])
    total_pop_count = majority_pop_count + minority_pop_count

    majority_percentage = round(100 * majority_pop_count / total_pop_count)
    minority_percentage = round(100 * minority_pop_count / total_pop_count)

    print(f'Година {year} – Население: {total_pop_count:n} – Мнозинство {majority_pop_count:n} ({majority_percentage}%) – Малцинство {minority_pop_count:n} ({minority_percentage}%) – Плодовитост (мно) {majority_fertility:n} – Плодовитост (мал) {minority_fertility:n}')

    majority_pop = update_population(majority_pop)
    minority_pop = update_population(minority_pop)

    x_values.append(year)
    y_values1.append(majority_pop_count)
    y_values2.append(minority_pop_count)

    line1.set_data(x_values, y_values1)
    line2.set_data(x_values, y_values2)
    ax.relim()
    ax.autoscale_view()

    plt.pause(0.05)

plt.ioff()
plt.show()