import pandas as pd

def filter_puzzles_by_size(csv_path, min_size=8):
    """
    Filter puzzles.csv where size >= min_size and print row counts before and after.
    
    Args:
        csv_path: Path to the puzzles.csv file
        min_size: Minimum size threshold (default: 8)
    """
    df = pd.read_csv(csv_path)
    
    print(f"Rows before filtering: {len(df)}")
    
    df_filtered = df[df['size'] >= min_size]
    
    print(f"Rows after filtering: {len(df_filtered)}")
    
    return df_filtered 

def map_puzzle_columns(df):
    """
    Map filtered puzzles to keep only id, size, and solution count columns.
    
    Args:
        df: DataFrame with puzzle data
        
    Returns:
        DataFrame with id, size, and solutionCount columns
    """
    df_mapped = df[['id', 'size', 'solution', 'original']].copy()
    df_mapped['solutionCount'] = df_mapped['solution'].str.split('|').str.len()
    df_mapped = df_mapped.drop('solution', axis=1)
    
    return df_mapped

def compute_puzzle_statistics(df):
    """
    Compute and print statistics for filtered puzzles.
    
    Args:
        df: DataFrame with puzzle data (after mapping)
    """
    totalSolutions = df['solutionCount'].sum()
    totalCharactersInOriginal = df['original'].str.len().sum()
    maxSize = df['size'].max()
    
    print(f"totalSolutions: {totalSolutions}")
    print(f"totalCharactersInOriginal: {totalCharactersInOriginal}")
    print(f"maxSize: {maxSize}")

def sort_puzzles(df):
    """
    Sort puzzles by size descending, then by id ascending.
    
    Args:
        df: DataFrame with puzzle data
        
    Returns:
        Sorted DataFrame
    """
    df_sorted = df[['id', 'size', 'original']].sort_values(by=['size', 'id'], ascending=[False, True])
    return df_sorted


if __name__ == "__main__":
    filtered_puzzles = filter_puzzles_by_size('puzzles.csv')
    print(filtered_puzzles.head())
    print('---')
    mapped_puzzles = map_puzzle_columns(filtered_puzzles)
    print(mapped_puzzles.head())
    print('---')
    compute_puzzle_statistics(mapped_puzzles)
    print('---')
    sorted_puzzles = sort_puzzles(filtered_puzzles)
    print(sorted_puzzles.head(10))



#What is IIFE?
# IIFE stands for Immediately Invoked Function Expression. 
# It is a JavaScript design pattern that allows you to execute a function immediately after defining it. 
# An IIFE is typically used to create a new scope and avoid polluting the global namespace.

#Does Python have IIFE?
# Python does not have a direct equivalent to JavaScript's IIFE, but you can achieve similar functionality 
# using a lambda function or by defining a function and calling it immediately.