#!/bin/bash
check_returncode() {
    if [ $? -ne 0 ]; then
        echo "Error: Falló la ejecución del comando."
    fi
}

sudo netstat -tunapl | grep ESTABLISHED
check_returncode
