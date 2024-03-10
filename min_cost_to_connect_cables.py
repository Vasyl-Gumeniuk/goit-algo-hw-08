import heapq

def min_cost_to_connect_cables(cables):
    total_cost = 0
    heapq.heapify(cables)  # перетворюємо список кабелів у пріоритетну чергу

    while len(cables) > 1:
        # Беремо два найкоротших кабелі та об'єднуємо їх
        shortest_one = heapq.heappop(cables)
        shortest_two = heapq.heappop(cables)
        total_cost += shortest_one + shortest_two
        # Додаємо новий кабель до списку
        heapq.heappush(cables, shortest_one + shortest_two)

    return total_cost

# Приклад використання:
def main():
    cables = [4, 3, 2, 6]  # припустимо, що це довжини кабелів
    print(f"Мінімальна сума витрат: {min_cost_to_connect_cables(cables)}")


if __name__ == "__main__":
    main()