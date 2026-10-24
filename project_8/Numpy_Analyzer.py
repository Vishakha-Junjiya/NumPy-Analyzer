import numpy as np


class DataAnalytics:
    def __init__(self):
        self.array = None
        self.arr_type = None

    def create_array(self):
        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        self.arr_type = int(input("Enter your choice: "))

        if self.arr_type == 1:
            total = int(input("Enter the number of elements: "))
            shape = (total,)

        elif self.arr_type == 2:
            row = int(input("Enter the number of rows: "))
            column = int(input("Enter the number of columns: "))
            total = row * column
            shape = (row, column)

        elif self.arr_type == 3:
            depth = int(input("Enter the depth: "))
            row = int(input("Enter the number of rows: "))
            column = int(input("Enter the number of columns: "))
            total = depth * row * column
            shape = (depth, row, column)

        else:
            print("Invalid choice!")
            return

        f_arr = list(map(int, input(
            f"Enter {total} elements separated by space: "
        ).split()))

        if len(f_arr) != total:
            print(f"Please enter exactly {total} elements!")
            return

        self.array = np.array(f_arr).reshape(shape)

        print("\nArray:")
        print(self.array)
        print("Shape:", self.array.shape)
        
        print("\nChoose an operation:")
        print("1. Indexing")
        print("2. Slicing")
        print("3. Go back")
        choice = int(input("Enter your Choice: "))
        
        if choice == 1:
            if self.arr_type == 1:
                index = int(input("Enter the index: "))
                print("Element:", self.array[index])

            elif self.arr_type == 2:
                row = int(input("Enter the row index: "))
                column = int(input("Enter the column index: "))
                print("Element:", self.array[row, column])

            elif self.arr_type == 3:
                depth = int(input("Enter the depth index: "))
                row = int(input("Enter the row index: "))
                column = int(input("Enter the column index: "))
                print("Element:", self.array[depth, row, column])

        elif choice == 2:
            if self.arr_type == 1:
                r = input("Enter the range (start:end): ")
                start, end = map(int, r.split(":"))
                print("Sliced Array:")
                print(self.array[start:end])

            elif self.arr_type == 2:
                r = input("Enter the row range (start:end): ")
                row_start, row_end = map(int, r.split(":"))

                c = input("Enter the column range (start:end): ")
                col_start, col_end = map(int, c.split(":"))

                print("Sliced Array:")
                print(self.array[row_start:row_end, col_start:col_end])

            elif self.arr_type == 3:
                d = input("Enter the depth range (start:end): ")
                d_start, d_end = map(int, d.split(":"))

                r = input("Enter the row range (start:end): ")
                row_start, row_end = map(int, r.split(":"))

                c = input("Enter the column range (start:end): ")
                col_start, col_end = map(int, c.split(":"))

                print("Sliced Array:")
                print(self.array[d_start:d_end, row_start:row_end, col_start:col_end])

        elif choice == 3:
            return
        else:
            print("Invalid choice!")

    def mathematical_operation(self):
        print("\nChoose a mathematical operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = int(input("Enter your choice: "))

        if choice not in [1, 2, 3, 4]:
            print("Invalid choice!")
            return

        if self.array is None:
            print("Please create an array first!")
            return

        total = self.array.size

        f_arr = list(map(int, input(
            f"Enter the same-size array elements ({total} elements separated by space): "
        ).split()))

        if len(f_arr) != total:
            print(f"Please enter exactly {total} elements!")
            return

        array2 = np.array(f_arr).reshape(self.array.shape)

        print("\nOriginal Array:")
        print(self.array)

        print("\nSecond Array:")
        print(array2)

        if choice == 1:
            result = self.array + array2
            print("\nResult of Addition:")
            print(result)

        elif choice == 2:
            result = self.array - array2
            print("\nResult of Subtraction:")
            print(result)

        elif choice == 3:
            result = self.array * array2
            print("\nResult of Multiplication:")
            print(result)

        elif choice == 4:
            if np.any(array2 == 0):
                print("Division by zero is not allowed!")
                return

            result = self.array / array2
            print("\nResult of Division:")
            print(result)

    def combine_split_array(self):
        if self.array is None:
            print("Please create an array first!")
            return

        
        print("Choose an option:")
        print("1. Combine Arrays")
        print("2. Split Array")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            total = self.array.size
            f_arr = list(map(int, input(
                f"Enter the elements of another array to combine ({total} elements separated by space): "
            ).split()))

            if len(f_arr) != total:
                print(f"Please enter exactly {total} elements!")
                return

            array2 = np.array(f_arr).reshape(self.array.shape)

            print("\nOriginal Array:")
            print(self.array)

            print("\nSecond Array:")
            print(array2)

            combined_result = np.vstack((self.array, array2))
            print("\nCombined Array (Vertical Stack):")
            print(combined_result)

        elif choice == 2:
            sections = int(input("Enter the number of sections to split into: "))
            try:
                split_result = np.array_split(self.array, sections)
                print("\nOriginal Array:")
                print(self.array)
                print("\nSplit Arrays:")
                for i, arr in enumerate(split_result, 1):
                    print(f"Section {i}:")
                    print(arr)
            except Exception as e:
                print(f"Error during splitting: {e}")
        else:
            print("Invalid choice!")

    def search_sort_filter(self):
        if self.array is None:
            print("Please create an array first!")
            return

        print("\nSearch, Sort, and Filter:")
        print("Choose an option:")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            val = int(input("Enter the value to search: "))
            result = np.where(self.array == val)
            print("\nOriginal Array:")
            print(self.array)
            print(f"\nIndices where value {val} is found:")
            print(result)

        elif choice == 2:
            sorted_arr = np.sort(self.array)
            print("\nOriginal Array:")
            print(self.array)
            print("\nSorted Array:")
            print(sorted_arr)
            print("(Sorting applied row-wise.)")

        elif choice == 3:
            cond = int(input("Enter the value to filter elements greater than: "))
            filtered_arr = self.array[self.array > cond]
            print("\nOriginal Array:")
            print(self.array)
            print(f"\nFiltered Array (Elements > {cond}):")
            print(filtered_arr)

        else:
            print("Invalid choice!")
    def aggregates_statistics(self):
        if self.array is None:
            print("Please create an array first!")
            return

        print("\nAggregates and Statistics:")
        print("Choose an aggregate/statistical operation:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")

        choice = int(input("Enter your choice: "))

        print("\nOriginal Array:")
        print(self.array)

        if choice == 1:
            print("\nSum of Array:", np.sum(self.array))
        elif choice == 2:
            print("\nMean of Array:", np.mean(self.array))
        elif choice == 3:
            print("\nMedian of Array:", np.median(self.array))
        elif choice == 4:
            print("\nStandard Deviation of Array:", np.std(self.array))
        elif choice == 5:
            print("\nVariance of Array:", np.var(self.array))
        else:
            print("Invalid choice!")

# Main Program
if __name__ == "__main__":
    print("Welcome to the NumPy Analyzer!")
    print("----------------------------------")

    a1 = DataAnalytics()

    while True:
        print("\nChoose an option:")
        print("1. Create a NumPy Array")
        print("2. Perform Mathematical Operation")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            a1.create_array()

        elif choice == 2:
            a1.mathematical_operation()

        elif choice == 3:
            a1.combine_split_array()

        elif choice == 4:
            a1.search_sort_filter()

        elif choice == 5:
            a1.aggregates_statistics()

        elif choice == 6:
            print("Thank you for using the NumPy Analyzer! Goodbye!")
            break

        else:
            print("Invalid choice!")