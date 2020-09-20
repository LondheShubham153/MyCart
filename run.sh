#!/bin/bash

exec python schema/create_schema.py ./schema/mycartkb.sql
exec python myCart.py