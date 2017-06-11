SET TIME ZONE 'UTC';

CREATE TABLE IF NOT EXISTS lang (
         id SERIAL PRIMARY KEY
       , iso_code VARCHAR(10) NOT NULL
       , name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS dish (
         id SERIAL PRIMARY KEY
       , name TEXT NOT NULL
       , lang_id INT REFERENCES lang (id)
       , create_date TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS recipe (
         id SERIAL PRIMARY KEY
       , name TEXT NOT NULL
       , create_date TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS dish_recipe (
         recipe_id INT REFERENCES recipe (id) ON UPDATE CASCADE ON DELETE CASCADE
       , dish_id INT REFERENCES dish (id) ON UPDATE CASCADE
       , CONSTRAINT recipe_dish_pkey PRIMARY KEY (recipe_id, dish_id)
);

CREATE TYPE e_unit AS ENUM (
         'big'
       , 'medium'
       , 'small'
       , 'cup'
       , 'tablespoon'
       , 'teaspoon'
       , 'liter'
       , 'kilo'
       , 'gram'
);

CREATE TABLE IF NOT EXISTS ingredient (
         id SERIAL PRIMARY KEY
       , name TEXT NOT NULL
       , kcal100 INT NOT NULL
       , protein100 INT NOT NULL
       , fat100 INT NOT NULL
       , carbs100 INT NOT NULL
);

CREATE TABLE IF NOT EXISTS unit (
         id SERIAL PRIMARY KEY
       , unit e_unit NOT NULL
       , val_in_gram FLOAT NOT NULL
       , ingredient INT REFERENCES ingredient (id)
);

CREATE TABLE IF NOT EXISTS amount_unit (
         id SERIAL PRIMARY KEY
       , amount FLOAT NOT NULL
       , recipe_id INT REFERENCES recipe (id)
       , unit_id INT REFERENCES unit (id)
);
