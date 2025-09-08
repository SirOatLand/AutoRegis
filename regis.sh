#!/usr/bin/bash

iterator=0
while true
do
    response=$(bash -c $1 | sed -n '/{/,/}/p')

    # Print the iterator
    echo ""$iterator" - "$response""

    # Check if the response contains the specified message
    if echo ""$response"" | grep -q "You already have this schedule as your result."; then
        echo "Found message: 'you already have this schedule as your result.'"
        break  # Exit the loop
    fi

    # Increment the iterator
    ((iterator++))

done
