#!/bin/bash

cmd=$1

if [[ $cmd -eq 1 ]]; then
    if [[ "$VIRTUAL_ENV" == "" ]]; then
        
        source env/bin/activate
        
    else
        echo "Virtual environment is already activated."
    fi
else
    
    if [[ "$VIRTUAL_ENV" != "" ]]; then
        deactivate
    else
        echo "Virtual environment is not activated."
    fi
fi
