---- consective numbers, 
---- min and max number of consective numbers, if number is not consective then itself will be min and max.

select min(id) as start, max(id)  as end from(	
select *, id - rank() over(order by id) as diffe from lower_backup.employees order by id)
group by diffe   order by min(id);

out:
101	107
110	110
121	122
129	131
135	135
137	138
140	140


----- consective numbers: min and max.

select min(id) as start, max(id)  as end, count(*) from(	
select *, id - rank() over(order by id) as diffe from lower_backup.employees order by id)
group by diffe  having count(*)>1 order by min(id);

out:
101	107	7
121	122	2
129	131	3
137	138	2