
  create or replace   view MY_DATABASE.MY_SCHEMA.my_second_dbt_model
  
   as (
    -- Use the `ref` function to select from other models

select *
from MY_DATABASE.MY_SCHEMA.my_first_dbt_model
where id = 1
  );

