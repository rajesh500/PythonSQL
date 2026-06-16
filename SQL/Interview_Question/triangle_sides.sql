
Input data:
combID   SideID     SideLength
1			A			3
1			B			4
1			C			5
2			A			2
2			B			3
2			C			6
3			A		    6
3			B			7
3			C			10

out:
1
3


** ask to find all three conditions should get satisfied then only 
it forms a triangle.

with cte as (
select * from(
select combinationid, sideid as first_side, sidelength as fs_len,
lead(sideid, 1) over(partition by combinationid order by sideid) as second_side,
lead(sideid, 2) over(partition by combinationid order by sideid) as third_side,
lead(sidelength, 1) over(partition by combinationid order by sideid) as ss_len,
lead(sidelength, 2) over(partition by combinationid order by sideid) as ts_len
from lower_backup.triangle_sides) 
where third_side is not null or ts_len is not null)
select combinationid from cte 
where ((fs_len + ss_len) > ts_len) and  ((ss_len + ts_len) > fs_len)
and ((ts_len + fs_len) > ss_len)
;