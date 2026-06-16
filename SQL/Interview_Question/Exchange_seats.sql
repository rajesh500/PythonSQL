---- exchange seats from first place to second and second to first.
---- similarly for three and four.
---- if no of rows is odd then last record we need to handle explicitly in the code.


case when id%2 !=0 and  id = (select max(id) from table) then id 
when id%2=0 then id-1
 when id%2!=0 then id+1
end
;



select case when id%2 !=0 and  id = (select max(id) from lower_backup.exchange_seats) then id 
when id%2=0 then id-1
 when id%2!=0 then id+1
end as flag, student
from lower_backup.exchange_seats
order by flag