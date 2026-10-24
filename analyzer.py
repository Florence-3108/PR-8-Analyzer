import numpy as np

class DataAnalytics:

    def __init__(self):
        self.__array = None
   
    def create_array(self):

        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            size = int(input("Enter the number of elements: "))

            values = list(map(int, input(
                "Enter elements separated by space: "
            ).split()))

            if len(values) != size:
                print("Error: Number of elements does not match.")
                return

            self.__array = np.array(values)

        elif choice == 2:

            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))

            values = list(map(int, input(f"Enter {rows * cols} elements separated by space: ").split()))

            if len(values) != rows * cols:
                print("Error: Number of elements does not match.")
                return

            self.__array = np.array(values).reshape(rows, cols)

        elif choice == 3:

            layers = int(input("Enter the number of layers: "))
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))

            total = layers * rows * cols

            values = list(map(int, input(f"Enter {total} elements separated by space: ").split()))

            if len(values) != total:
                print("Error: Number of elements does not match.")
                return

            self.__array = np.array(values).reshape(layers, rows, cols)
        else:
            print("Invalid choice!")
            return

        print("\nArray created successfully:")
        print(self.__array)

    def __check_array(self):

        if self.__array is None:
            print("\nPlease create an array first.")
            return False

        return True

    def display_array(self):

        if self.__check_array():
            print("\nOriginal Array:")
            print(self.__array)

    def indexing_slicing(self):

        if not self.__check_array():
            return

        print("\nChoose an operation:")
        print("1. Indexing")
        print("2. Slicing")
        print("3. Go Back")

        choice = int(input("Choose an operation: "))

        if choice == 1:

            if self.__array.ndim == 1:

                index = int(input("Enter the index: "))
                print("Element:", self.__array[index])

            else:

                row = int(input("Enter the row index: "))
                col = int(input("Enter the column index: "))

                print("Element:", self.__array[row, col])

        elif choice == 2:

            if self.__array.ndim == 1:

                start = int(input("Enter the start index: "))
                end = int(input("Enter the end index: "))

                print("Sliced Array:")
                print(self.__array[start:end])

            elif self.__array.ndim == 2:

                row_range = input(
                    "Enter the row range (start:end): "
                ).split(":")

                col_range = input(
                    "Enter the column range (start:end): "
                ).split(":")

                r1 = int(row_range[0])
                r2 = int(row_range[1])

                c1 = int(col_range[0])
                c2 = int(col_range[1])

                print("\nSliced Array:")
                print(self.__array[r1:r2, c1:c2])

            else:
                print("Use indexing and slicing for 3D arrays carefully.")
                print("Array:")
                print(self.__array)

        elif choice == 3:
            return

        else:
            print("Invalid choice!")

    def mathematical_operations(self):

        if not self.__check_array():
            return

        print("\nChoose a mathematical operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
       
        choice = int(input("Enter your choice: "))

        print("\nOriginal Array:")
        print(self.__array)

        values = list(map(float, input(
            f"Enter the same-size array elements "
            f"({self.__array.size} elements separated by space): "
        ).split()))

        if len(values) != self.__array.size:
            print("Error: Number of elements does not match.")
            return

        second_array = np.array(values).reshape(self.__array.shape)

        print("\nSecond Array:")
        print(second_array)

        if choice == 1:
            result = self.__array + second_array
            operation = "Addition"

        elif choice == 2:
            result = self.__array - second_array
            operation = "Subtraction"

        elif choice == 3:
            result = self.__array * second_array
            operation = "Multiplication"

        elif choice == 4:

            if np.any(second_array == 0):
                print("Error: Division by zero is not allowed.")
                return

            result = self.__array / second_array
            operation = "Division"
        
        else:
            print("Invalid choice!")
            return

        print(f"\nResult of {operation}:")
        print(result)

    def combine_split(self):

        if not self.__check_array():
            return

        print("\nChoose an option:")
        print("1. Combine Arrays")
        print("2. Split Array")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            values = list(map(int, input(
                f"Enter the elements of another array to combine "
                f"({self.__array.size} elements separated by space): "
            ).split()))

            if len(values) != self.__array.size:
                print("Error: Number of elements does not match.")
                return

            second_array = np.array(values).reshape(
                self.__array.shape
            )

            print("\nOriginal Array:")
            print(self.__array)

            print("\nSecond Array:")
            print(second_array)

            result = np.vstack((self.__array, second_array))

            print("\nCombined Array (Vertical Stack):")
            print(result)

        elif choice == 2:

            if self.__array.ndim != 2:
                print("Splitting in this requires a 2D array.")
                return

            if self.__array.shape[0] < 2:
                print("At least two rows are required to split.")
                return

            result = np.array_split(self.__array, 2, axis=0)

            print("\nFirst Split Array:")
            print(result[0])

            print("\nSecond Split Array:")
            print(result[1])

        else:
            print("Invalid choice!")

    def search_sort_filter(self):

        if not self.__check_array():
            return

        print("\nChoose an option:")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            value = int(input("Enter the value to search: "))

            positions = np.argwhere(self.__array == value)

            if positions.size > 0:
                print("Value found at index/indices:")
                print(positions)
            else:
                print("Value not found.")

        elif choice == 2:

            result = np.sort(self.__array, axis=-1)

            print("\nOriginal Array:")
            print(self.__array)

            print("\nSorted Array:")
            print(result)
            print("(Sorting applied row-wise.)")

        elif choice == 3:

            value = float(input("Enter the filter condition value: "))

            print("\nChoose a condition:")
            print("1. Greater than")
            print("2. Less than")
            print("3. Equal to")

            condition = int(input("Enter your choice: "))

            if condition == 1:
                result = self.__array[self.__array > value]

            elif condition == 2:
                result = self.__array[self.__array < value]

            elif condition == 3:
                result = self.__array[self.__array == value]

            else:
                print("Invalid condition!")
                return

            print("\nFiltered Values:")
            print(result)

        else:
            print("Invalid choice!")

    def aggregates_statistics(self):

        if not self.__check_array():
            return

        print("\nChoose an aggregate/statistical operation:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            result = np.sum(self.__array)
            name = "Sum"

        elif choice == 2:
            result = np.mean(self.__array)
            name = "Mean"

        elif choice == 3:
            result = np.median(self.__array)
            name = "Median"

        elif choice == 4:
            result = np.std(self.__array)
            name = "Standard Deviation"

        elif choice == 5:
            result = np.var(self.__array)
            name = "Variance"

        else:
            print("Invalid choice!")
            return

        print("\nOriginal Array:")
        print(self.__array)

        print(f"\n{name} of Array: {result}")

    @classmethod
    def project_name(cls):
        return "NumPy Analyzer"

    @staticmethod
    def show_message():
        print("Analyze your data easily using NumPy!")


def main():

    analyzer = DataAnalytics()

    print("Welcome to the", DataAnalytics.project_name(), "!")
    DataAnalytics.show_message()

    while True:

        print("\n" + "=" * 45)
        print("Choose an option:")
        print("1. Create a NumPy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                analyzer.create_array()
                analyzer.indexing_slicing()

            elif choice == 2:
                analyzer.mathematical_operations()

            elif choice == 3:
                analyzer.combine_split()

            elif choice == 4:
                analyzer.search_sort_filter()

            elif choice == 5:
                analyzer.aggregates_statistics()

            elif choice == 6:
                print("\nThank you for using the NumPy Analyzer! Goodbye!")
                break

            else:
                print("Invalid choice! Please try again.")

        except ValueError:
            print("Invalid input! Please enter a valid number.")

        except IndexError:
            print("Invalid index! Please enter a valid index.")

        except Exception as error:
            print("An error occurred:", error)


if __name__ == "__main__":
    main()