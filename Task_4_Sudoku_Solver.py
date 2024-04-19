# Sudoku solver using backtracking
SIZE = 9

def solve_sudoku(grid):
    # Find an empty location in the grid
    row, col = find_empty_location(grid)
    
    # If no empty location is found, the Sudoku puzzle is solved
    if row is None:
        return True
    
    # Try each number from 1 to 9 in the empty cell
    for num in range(1, SIZE + 1):
        # Check if placing the number in the cell is safe
        if is_safe(grid, row, col, num):
            # Place the number in the cell
            grid[row][col] = num
            
            # Recursively solve the rest of the Sudoku puzzle
            if solve_sudoku(grid):
                return True
            
            # If not solved, backtrack by resetting the cell
            grid[row][col] = 0
    
    # If no number is valid, return False
    return False

def find_empty_location(grid):
    # Iterate through the grid to find an empty cell (with value 0)
    for row in range(SIZE):
        for col in range(SIZE):
            if grid[row][col] == 0:
                return row, col
    
    # If no empty cell is found, return None
    return None, None

def is_safe(grid, row, col, num):
    # Check the row for the presence of the number
    if num in grid[row]:
        return False
    
    # Check the column for the presence of the number
    for r in range(SIZE):
        if grid[r][col] == num:
            return False
    
    # Check the 3x3 grid (box) for the presence of the number
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    
    # If the number is not found in the row, column, or 3x3 grid, it is safe
    return True

def print_grid(grid):
    # Print the Sudoku grid
    for row in grid:
        print(" ".join(str(num) for num in row))

def main():
    # Define the Sudoku puzzle as a 2D list
    puzzle = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0],
    ]

    # Solve the Sudoku puzzle
    if solve_sudoku(puzzle):
        print("Sudoku Solved Successfully")
        print_grid(puzzle)
    else:
        print("Sudoku puzzle cannot be solved.")
        print_grid(puzzle)

if __name__ == "__main__":
    main()
