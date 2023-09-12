#!/bin/bash

encrypt_directory() {
    echo "Enter a password to encrypt the directory:"
    read -s password
    echo "Enter the path to the directory you want to encrypt:"
    read source_directory
    echo "Enter the name of the encrypted ZIP file:"
    read output_zip_file
    echo "Enter the command to execute within the directory upon decryption:"
    read post_decrypt_command

    # Create a temporary script to execute the post-decryption command
    temp_script="post_decrypt_script.sh"
    echo "$post_decrypt_command" > "$temp_script"

    # Add the script to the directory
    cp "$temp_script" "$source_directory"

    # Encrypt the directory with the script
    zip -r -e -P "$password" "$output_zip_file" "$source_directory"

    # Remove the temporary script
    rm "$temp_script"

    echo "Directory encrypted and saved as $output_zip_file"
}

decrypt_directory() {
    echo "Enter the password to decrypt the ZIP file:"
    read -s password
    echo "Enter the name of the encrypted ZIP file:"
    read input_zip_file
    echo "Enter the path where you want to extract the decrypted directory:"
    read destination_directory

    # Decrypt the directory
    unzip -P "$password" -d "$destination_directory" "$input_zip_file"

    # Change to the decrypted directory
    cd "$destination_directory"

    # Execute the post-decryption command
    if [ -f "post_decrypt_script.sh" ]; then
        chmod +x post_decrypt_script.sh
        ./post_decrypt_script.sh
    fi

    echo "Directory decrypted and command executed in $destination_directory"
}

while true; do
    echo "Choose an option:"
    echo "1. Encrypt a directory"
    echo "2. Decrypt a directory"
    echo "3. Exit"
    read choice

    case $choice in
        1)
            encrypt_directory
            ;;
        2)
            decrypt_directory
            ;;
        3)
            exit 0
            ;;
        *)
            echo "Invalid choice, please try again."
            ;;
    esac
done
