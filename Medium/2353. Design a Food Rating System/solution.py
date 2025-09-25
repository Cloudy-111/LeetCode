class FoodRatings:
    cuisine_food_and_rate = {}
    food_and_rate = defaultdict(int)
    food_and_cuisine = {}

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        n = len(foods)

        self.food_and_rate = defaultdict(int)
        self.food_and_cuisine = {}
        for i in range(n):
            if foods[i] not in self.food_and_cuisine:
                self.food_and_cuisine[foods[i]] = cuisines[i]

        for i in range(n):
            self.food_and_rate[foods[i]] = ratings[i]
            if cuisines[i] not in self.cuisine_food_and_rate:
                self.cuisine_food_and_rate[cuisines[i]] = []
            heapq.heappush(
                self.cuisine_food_and_rate[cuisines[i]], [-ratings[i], foods[i]])

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_and_rate[food] = newRating
        heapq.heappush(
            self.cuisine_food_and_rate[self.food_and_cuisine[food]], [-newRating, food])

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_food_and_rate[cuisine]
        while heap and -heap[0][0] != self.food_and_rate[heap[0][1]]:
            heapq.heappop(heap)

        return heap[0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
