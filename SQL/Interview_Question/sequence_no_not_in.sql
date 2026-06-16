---- Find the sequence numbers not in the field.
---- 1 ----
select * from(

    select generate_series(1,10) as seq)sub where seq not in (
        select id from table
    );
)



---- 2 ----
with recursive cte_main as (select 1 as id
union 
select id + 1 from cte_main where id < 100
) select * from cte_main where id not in (select id from table);