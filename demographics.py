import locale
import matplotlib.pyplot as plt

locale.setlocale(locale.LC_ALL, 'BG_bg')

population = [
    {'age':  0, 'count':  56526, 'births': 0, 'deaths': 0},
    {'age':  1, 'count':  56404, 'births': 0, 'deaths': 0},
    {'age':  2, 'count':  57313, 'births': 0, 'deaths': 0},
    {'age':  3, 'count':  57591, 'births': 0, 'deaths': 0},
    {'age':  4, 'count':  58226, 'births': 0, 'deaths': 0},
    {'age':  5, 'count':  60159, 'births': 0, 'deaths': 0},
    {'age':  6, 'count':  61443, 'births': 0, 'deaths': 0},
    {'age':  7, 'count':  60761, 'births': 0, 'deaths': 0},
    {'age':  8, 'count':  62259, 'births': 0, 'deaths': 0},
    {'age':  9, 'count':  59773, 'births': 0, 'deaths': 0},
    {'age': 10, 'count':  61112, 'births': 0, 'deaths': 0},
    {'age': 11, 'count':  61364, 'births': 0, 'deaths': 0},
    {'age': 12, 'count':  65114, 'births': 0, 'deaths': 0},
    {'age': 13, 'count':  69221, 'births': 0, 'deaths': 0},
    {'age': 14, 'count':  66153, 'births': 0, 'deaths': 0},
    {'age': 15, 'count':  64346, 'births': 0, 'deaths': 0},
    {'age': 16, 'count':  61975, 'births': 0, 'deaths': 0},
    {'age': 17, 'count':  59956, 'births': 0, 'deaths': 0},
    {'age': 18, 'count':  58882, 'births': 0, 'deaths': 0},
    {'age': 19, 'count':  56462, 'births': 0, 'deaths': 0},
    {'age': 20, 'count':  53690, 'births': 0, 'deaths': 0},
    {'age': 21, 'count':  53246, 'births': 0, 'deaths': 0},
    {'age': 22, 'count':  56660, 'births': 0, 'deaths': 0},
    {'age': 23, 'count':  57113, 'births': 0, 'deaths': 0},
    {'age': 24, 'count':  51431, 'births': 0, 'deaths': 0},
    {'age': 25, 'count':  49249, 'births': 0, 'deaths': 0},
    {'age': 26, 'count':  54337, 'births': 0, 'deaths': 0},
    {'age': 27, 'count':  54163, 'births': 0, 'deaths': 0},
    {'age': 28, 'count':  59119, 'births': 0, 'deaths': 0},
    {'age': 29, 'count':  63445, 'births': 0, 'deaths': 0},
    {'age': 30, 'count':  66391, 'births': 0, 'deaths': 0},
    {'age': 31, 'count':  71151, 'births': 0, 'deaths': 0},
    {'age': 32, 'count':  78376, 'births': 0, 'deaths': 0},
    {'age': 33, 'count':  82127, 'births': 0, 'deaths': 0},
    {'age': 34, 'count':  84063, 'births': 0, 'deaths': 0},
    {'age': 35, 'count':  83654, 'births': 0, 'deaths': 0},
    {'age': 36, 'count':  86667, 'births': 0, 'deaths': 0},
    {'age': 37, 'count':  85316, 'births': 0, 'deaths': 0},
    {'age': 38, 'count':  86850, 'births': 0, 'deaths': 0},
    {'age': 39, 'count':  87273, 'births': 0, 'deaths': 0},
    {'age': 40, 'count':  87356, 'births': 0, 'deaths': 0},
    {'age': 41, 'count':  89029, 'births': 0, 'deaths': 0},
    {'age': 42, 'count':  90834, 'births': 0, 'deaths': 0},
    {'age': 43, 'count':  95665, 'births': 0, 'deaths': 0},
    {'age': 44, 'count':  95927, 'births': 0, 'deaths': 0},
    {'age': 45, 'count':  99812, 'births': 0, 'deaths': 0},
    {'age': 46, 'count': 102004, 'births': 0, 'deaths': 0},
    {'age': 47, 'count': 102485, 'births': 0, 'deaths': 0},
    {'age': 48, 'count': 105294, 'births': 0, 'deaths': 0},
    {'age': 49, 'count':  99292, 'births': 0, 'deaths': 0},
    {'age': 50, 'count':  93150, 'births': 0, 'deaths': 0},
    {'age': 51, 'count':  95677, 'births': 0, 'deaths': 0},
    {'age': 52, 'count':  98983, 'births': 0, 'deaths': 0},
    {'age': 53, 'count': 100398, 'births': 0, 'deaths': 0},
    {'age': 54, 'count':  98308, 'births': 0, 'deaths': 0},
    {'age': 55, 'count':  86692, 'births': 0, 'deaths': 0},
    {'age': 56, 'count':  85332, 'births': 0, 'deaths': 0},
    {'age': 57, 'count':  87134, 'births': 0, 'deaths': 0},
    {'age': 58, 'count':  89863, 'births': 0, 'deaths': 0},
    {'age': 59, 'count':  90651, 'births': 0, 'deaths': 0},
    {'age': 60, 'count':  91012, 'births': 0, 'deaths': 0},
    {'age': 61, 'count':  93380, 'births': 0, 'deaths': 0},
    {'age': 62, 'count':  93275, 'births': 0, 'deaths': 0},
    {'age': 63, 'count':  90448, 'births': 0, 'deaths': 0},
    {'age': 64, 'count':  90965, 'births': 0, 'deaths': 0},
    {'age': 65, 'count':  91034, 'births': 0, 'deaths': 0},
    {'age': 66, 'count':  93383, 'births': 0, 'deaths': 0},
    {'age': 67, 'count':  92591, 'births': 0, 'deaths': 0},
    {'age': 68, 'count':  88734, 'births': 0, 'deaths': 0},
    {'age': 69, 'count':  88582, 'births': 0, 'deaths': 0},
    {'age': 70, 'count':  86218, 'births': 0, 'deaths': 0},
    {'age': 71, 'count':  82028, 'births': 0, 'deaths': 0},
    {'age': 72, 'count':  90970, 'births': 0, 'deaths': 0},
    {'age': 73, 'count':  84755, 'births': 0, 'deaths': 0},
    {'age': 74, 'count':  79050, 'births': 0, 'deaths': 0},
    {'age': 75, 'count':  72580, 'births': 0, 'deaths': 0},
    {'age': 76, 'count':  72124, 'births': 0, 'deaths': 0},
    {'age': 77, 'count':  61613, 'births': 0, 'deaths': 0},
    {'age': 78, 'count':  52926, 'births': 0, 'deaths': 0},
    {'age': 79, 'count':  50507, 'births': 0, 'deaths': 0},
    {'age': 80, 'count': 328288, 'births': 0, 'deaths': 0},
]

birth_rates = [
    { "start_age": 15, "end_age": 19, "per_thousand": 18.9920 },
    { "start_age": 20, "end_age": 24, "per_thousand": 36.0586 },
    { "start_age": 25, "end_age": 29, "per_thousand": 52.2166 },
    { "start_age": 30, "end_age": 34, "per_thousand": 41.1324 },
    { "start_age": 35, "end_age": 39, "per_thousand": 19.2317 },
    { "start_age": 40, "end_age": 44, "per_thousand":  4.3308 },
    { "start_age": 45, "end_age": 80, "per_thousand":  0.1188 },
]

death_rates = [
    {'start_age':  0, 'end_age':  0, 'per_thousand':   4.8473 },
    {'start_age':  1, 'end_age':  4, 'per_thousand':   0.3093 },
    {'start_age':  5, 'end_age':  9, 'per_thousand':   0.1314 },
    {'start_age': 10, 'end_age': 14, 'per_thousand':   0.1981 },
    {'start_age': 15, 'end_age': 19, 'per_thousand':   0.4177 },
    {'start_age': 20, 'end_age': 24, 'per_thousand':   0.6393 },
    {'start_age': 25, 'end_age': 29, 'per_thousand':   0.8419 },
    {'start_age': 30, 'end_age': 34, 'per_thousand':   1.0703 },
    {'start_age': 35, 'end_age': 39, 'per_thousand':   1.8149 },
    {'start_age': 40, 'end_age': 44, 'per_thousand':   2.8944 },
    {'start_age': 45, 'end_age': 49, 'per_thousand':   4.4607 },
    {'start_age': 50, 'end_age': 54, 'per_thousand':   7.4941 },
    {'start_age': 55, 'end_age': 59, 'per_thousand':  11.8088 },
    {'start_age': 60, 'end_age': 64, 'per_thousand':  17.9467 },
    {'start_age': 65, 'end_age': 69, 'per_thousand':  25.9726 },
    {'start_age': 70, 'end_age': 74, 'per_thousand':  38.7143 },
    {'start_age': 75, 'end_age': 79, 'per_thousand':  58.4019 },
    {'start_age': 80, 'end_age': 84, 'per_thousand': 151.3853 }
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

        if age < 80:
            new_population.append({
                "age": age + 1,
                "count": pop_obj["count"] - pop_obj["deaths"],
                "births": 0,
                "deaths": 0
            })
        elif age == 80:
            last_index = len(new_population) - 1
            new_population[last_index]["count"] += pop_obj["count"] - pop_obj["deaths"]

    return new_population

start_year = 2022

x_values = []
y_values = []

plt.ion()
fig, ax = plt.subplots()
line, = ax.plot(x_values, y_values)
ax.grid(True)

ax.set_xlabel('Година')
ax.set_ylabel('Население (млн)')

plt.title('Симулация на демография')

#for birth_rate in birth_rates:
    #birth_rate["per_thousand"] *= 1.1775
    #birth_rate["per_thousand"] *= 2

for i in range(500):
    year = start_year + i

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