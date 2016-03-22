#!/bin/sh

if [ -e nengo.db ]; then
  echo "table cells already exists"
else
  ./scripts/create.py
  ./scripts/insert.py
fi
