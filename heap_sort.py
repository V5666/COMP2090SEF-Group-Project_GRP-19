class HeapSorter:
    def __init__(self, data=None, key=None):
        self.data = data if data is not None else []
        self.key = key 

    def heapify(self, arr, n, i, key_func):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and key_func(arr[left]) > key_func(arr[largest]):
            largest = left
        if right < n and key_func(arr[right]) > key_func(arr[largest]):
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest, key_func)

    def heap_sort(self):
        if not self.data:
            return []
        key_func = self.key if self.key else lambda x: x
        arr = self.data.copy()
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i, key_func)
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0, key_func)
        return arr


if __name__ == "__main__":
    print("Heap Sort Demo")
    print("=" * 30)

    nums = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", nums)
    s1 = HeapSorter(nums)
    print("Sorted:  ", s1.heap_sort())

    words = ["banana", "apple", "cherry", "date"]
    print("\nOriginal:", words)
    s2 = HeapSorter(words)
    print("Sorted:  ", s2.heap_sort())

    class Book:
        def __init__(self, title, author, year):
            self.title = title
            self.author = author
            self.year = year
        def __repr__(self):
            return f"{self.title} ({self.year})"

    books = [
        Book("The Hobbit", "Tolkien", 1937),
        Book("1984", "Orwell", 1949),
        Book("Pride and Prejudice", "Austen", 1813)
    ]
    print("\nOriginal books:", books)
    s3 = HeapSorter(books, key=lambda b: b.year)
    print("Sorted by year:", s3.heap_sort())
    s4 = HeapSorter(books, key=lambda b: b.title)
    print("Sorted by title:", s4.heap_sort())