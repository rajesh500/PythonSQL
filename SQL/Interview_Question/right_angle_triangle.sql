𝐀𝐦𝐚𝐳𝐨𝐧 𝐒𝐐𝐋 𝐈𝐧𝐭𝐞𝐫𝐯𝐢𝐞𝐰 𝐂𝐡𝐚𝐥𝐥𝐞𝐧𝐠𝐞: How would you write a query to find out a combination that creates a valid right-angle triangle?🛑

📌 Input Table:
You are given a table named triangle with 3 columns 
(𝐂𝐨𝐦𝐛𝐢𝐧𝐚𝐭𝐢𝐨𝐧𝐈𝐃, 𝐒𝐢𝐝𝐞𝐈𝐃, 𝐒𝐢𝐝𝐞𝐋𝐞𝐧𝐠𝐭𝐡)

🎯Your Goal:
Write an SQL query to get the CombinationID that creates a valid right-angle triangle.

🧠Rule to apply (Pythagoras theorem):
H² = P² + B²
(where H is the longest side)



Input data:
combID   SideID     SideLength
1			A			3
1			B			4
1			C			5
2			A			2
2			B			3
2			C			6
3			A			13
3			B			5
3			C			12

out:
1
3


** Ask is to find any three side are getting equal or not.


with cte as (
select * from(
select combinationid, sideid as first_side, sidelength as fs_len,
lead(sideid, 1) over(partition by combinationid order by sideid) as second_side,
lead(sideid, 2) over(partition by combinationid order by sideid) as third_side,
lead(sidelength, 1) over(partition by combinationid order by sideid) as ss_len,
lead(sidelength, 2) over(partition by combinationid order by sideid) as ts_len
from lower_backup.right_triangle)sub1
where third_side is not null or ts_len is not null), 
cte2 as (
select combinationid, (fs_len * fs_len) as fs_len, 
(ss_len * ss_len) as ss_len, (ts_len * ts_len) as ts_len
from cte)
select * from cte2
where ((fs_len + ss_len) = ts_len) or 
((ss_len + ts_len) = fs_len) or 
((ts_len + fs_len) = ss_len)