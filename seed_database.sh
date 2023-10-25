#! /bin/sh

rm puppies.db
sqlite3 puppies.db < puppy.sql
