import csv

def remove_columns(input_file, output_file, columns_to_remove):
  """
  Reads a CSV file, removes specified columns, and writes the modified data to a new file.

  Args:
      input_file (str): Path to the input CSV file.
      output_file (str): Path to the output CSV file.
      columns_to_remove (list): List of column names to remove.

  Raises:
      ValueError: If the specified column is not found in the input file.
  """

  with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Get header row (assuming the CSV has a header)
    header = next(reader)

    # Validate column names to remove
    for col in columns_to_remove:
      if col not in header:
        raise ValueError(f"Column '{col}' not found in the input CSV.")

    # Write a new header row excluding the columns to remove
    new_header = [h for h in header if h not in columns_to_remove]
    writer.writerow(new_header)

    # Write remaining data rows, skipping the columns to remove
    for row in reader:
      new_row = [val for i, val in enumerate(row) if header[i] not in columns_to_remove]
      writer.writerow(new_row)

if __name__ == '__main__':
  input_file = 'projetos_unesco3.csv'
  output_file = 'projetos_unesco3_modified.csv'  # Create a new output file
  columns_to_remove = ['Cumulative Incurred Expenditures (USD)', 'Parent project ID', 'Cumulative Incurred Expenditure(USD)']

  remove_columns(input_file, output_file, columns_to_remove)

  print(f"CSV file modified successfully. New file: {output_file}")
