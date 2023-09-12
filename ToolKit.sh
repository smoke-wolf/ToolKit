#!/bin/bash

# Function to display usage instructions
display_usage() {
    echo "Options:"
    echo "  1. Mac Commands - provides real-time examples and usage explanations for every terminal command "
    echo "  2. Speech2Text - a very capable tool for extracting text from audio while also having features for name corrections and commom error training "
    echo "  3. Advanced System Info - Get info about the local device, good for post access"
    echo "  4. Option 4 - Description 4"
    echo "  5. Option 5 - Description 5"
    echo "  6. Option 6 - Description 6"
    echo "  7. Option 7 - Description 7"
    echo "  8. Option 8 - Description 8"
    echo "  9. Option 9 - Description 9"
    echo "  10. Option 10 - Description 10"
}

# Display the menu of options
display_usage

# Prompt the user for their choice
read -p "Enter your choice (1-10): " choice

# Main switch case for options
case $choice in
    1)
        echo "Running Option 1 - Description 1"
        cd "macCommands"
        python3 "comsearch.py"
        ;;
    2)
        echo "Running Option 2 - Description 2"
        cd "Speech2Text"
        python3 "speech.py"
        ;;
    3)
        echo "Running Option 3 - Description 3"
        cd "AdvancedInfo"
        bash "SysFO.sh"
        ;;
    4)
        echo "Running Option 4 - Description 4"
        # Add your command for option 4 here
        ;;
    5)
        echo "Running Option 5 - Description 5"
        # Add your command for option 5 here
        ;;
    6)
        echo "Running Option 6 - Description 6"
        # Add your command for option 6 here
        ;;
    7)
        echo "Running Option 7 - Description 7"
        # Add your command for option 7 here
        ;;
    8)
        echo "Running Option 8 - Description 8"
        # Add your command for option 8 here
        ;;
    9)
        echo "Running Option 9 - Description 9"
        # Add your command for option 9 here
        ;;
    10)
        echo "Running Option 10 - Description 10"
        # Add your command for option 10 here
        ;;
    *)
        echo "Invalid option: $choice"
        ;;
esac

# End of the script
