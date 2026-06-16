select *, sum(amount_type) over(order by transaction_date rows between unbounded preceding and current row) as total
from(
select *, case when type = 'deposit' then amount else -amount end as amount_type
from lower_backup.running_total)


input:
id	type	amount	transaction_date
16,461	deposit	278	2022-07-08
29,776	withdrawal	25	2022-07-08
53,151	withdrawal	45	2022-07-08
19,153	deposit	65	2022-07-10
77,134	deposit	32	2022-07-10


id	    type	    amount	    transaction_date	amount_type	total
16,461	deposit	    278	        2022-07-08	        278	        278
29,776	withdrawal	25	        2022-07-08	        -25	        253
53,151	withdrawal	45	        2022-07-08	        -45	        208
19,153	deposit	    65	        2022-07-10	        65	        273
77,134	deposit	    32	        202207-10	        32	        305