def main():
    # Step 1: Ask user for filename
    filename = input("Enter the filename to read: ")

    try:
        # Step 2: Try opening and reading the file
        with open(filename, "r") as infile:
            content = infile.read()
        
        # Step 3: Modify the content (example: uppercase)
        modified_content = content.upper()

        # Step 4: Write modified content to new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"✅ Modified content written to '{new_filename}'")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: Permission denied when trying to read the file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()


