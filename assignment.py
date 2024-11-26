def read_and_write_file():
    try:
        # Ask the user for the filename to read
        input_filename = input("Enter the filename to read from: ")
        
        # Open the input file for reading
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
        
        # Modify the content (e.g., convert to uppercase)
        modified_content = content.lower()
        
        # Ask the user for the filename to write to
        output_filename = input("Enter the filename to write to: ")
        
        # Open the output file for writing
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
        
        print(f"Modified content successfully written to {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    
    except IOError:
        print(f"Error: Could not read the file '{input_filename}'.")

if __name__ == "__main__":
    read_and_write_file()
