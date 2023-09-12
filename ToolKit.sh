#!/bin/bash

# Function to display usage instructions
display_usage() {
    echo "Usage: $0 [option]"
    echo "Options:"
    echo "  1. Mac Commands - provides real-time examples and usage explanations for every terminal command "
    echo "  2. Option 2 - Description 2"
    echo "  3. Option 3 - Description 3"
    echo "  4. Option 4 - Description 4"
    echo "  5. Option 5 - Description 5"
    echo "  6. Option 6 - Description 6"
    echo "  7. Option 7 - Description 7"
    echo "  8. Option 8 - Description 8"
    echo "  9. Option 9 - Description 9"
    echo "  10. Option 10 - Description 10"
    exit 1
}

# Check if an option is provided
if [ $# -eq 0 ]; then
    display_usage
fi

# Main switch case for options
case $1 in
    1)
        echo "Running Option 1 - Description 1"
        python3 "macCommands/comsearch.py"
        
        ;;
    2)
        echo "Running Option 2 - Description 2"
        # Add your command for option 2 here
        ;;
    3)
        echo "Running Option 3 - Description 3"
        # Add your command for option 3 here
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
        echo "Invalid option: $1"
        display_usage
        ;;
esac

# End of the script
