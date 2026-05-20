#Driver Code Starts
# Function to print hollow rectangle
#Driver Code Ends
def print_rectangle(rows, columns):

    for i in range(1, rows + 1):
        for j in range(1, columns + 1):

            # Print star at boundary positions
            if i == 1 or i == rows or j == 1 or j == columns:
                print("*", end="")
            else:
                print(" ", end="")

        # Move to the next line
        print()

#Driver Code Starts

def main():
    rows = 6
    columns = 20
    print_rectangle(rows, columns)


if __name__ == "__main__":
    main()

#Driver Code Ends
