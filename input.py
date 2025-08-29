def process_file():
    try:
        # Ask the user for a filename
        filename = input("Enter the filename to read: ")

        # Try opening the file
        with open(filename, "r") as f:
            content = f.read()

        # Count words
        word_count = len(content.split())

        # Convert to uppercase
        processed_text = content.upper()

        # Write results to output.txt
        with open("output.txt", "w") as f:
            f.write(processed_text + "\n")
            f.write(f"\nWord Count: {word_count}\n")

        print("✅ File 'output.txt' created successfully with processed text and word count.")

    except FileNotFoundError:
        print("❌ Error: The file was not found. Please check the filename and try again.")
    except PermissionError:
        print("❌ Error: Permission denied. Cannot read the file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# Run the function
process_file()
