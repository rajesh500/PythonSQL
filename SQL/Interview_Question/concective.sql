---- consective tax filing three year

select a.name from(
(select * from tax_filing_year) a, 
(select * from tax_filing_year) b,
(select * from tax_filing_year) c
) where a.name = b.name and b.name = c.name
and a.year::integer + 1 = b.year::integer  and b.year::integer + 1 = c.year::integer;



select * from tax_filing_year a
join tax_filing_year b on a.name = b.name 
join tax_filing_year c on b.name = c.name
where a.year::integer + 1 = b.year::integer
and a.year::integer + 1 = b.year::integer

---- two consective year    
select a.name from(
(select * from tax_filing_year) a,      
(select * from tax_filing_year) b
) where a.name = b.name
and a.year::integer + 1 = b.year::integer ;

-- another way
select a.name from tax_filing_year a        
join tax_filing_year b on a.name = b.name 
where a.year::integer + 1 = b.year::integer ;




-------  consective amount increases return product id.

select  product_id from (
    select * , case when unitsold > rnum then 'Y' else 'N' end as increase_flag
    FROM (
        select *, lag(unitsold) over (partition by product_id order by year) as rnum
        from sales_data
    ) sub1 where rnum is not null) where increase_flag = 'Y'; 



------ consective number:
seat_id  free
1           1
2           0
3           1
4           1
5           1

using Lead and lag this question can be solved
but multiple lead we need to write, here multiple means we dont know how many we have to write.


join be easy.

select c3.seat_id from consective_seats c1 inner join 
consective_seats c2 on 
c1.seat_id = c2.seat_id - 1 and c1.free = c2.free
inner join consective_seats c3 ON
c2.seat_id = c3.seat_id-1 and c2.free =  c3.free.


