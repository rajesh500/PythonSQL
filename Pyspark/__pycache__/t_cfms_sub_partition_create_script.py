##   create table batchuat.t_cfms_800 partition of batchuat.t_cfms for values in ('800');

create_tbl_str = 'create table batchuat.t_auth_encmbr_'
create_tbl_str2 = ' partition of batchuat.t_auth_encmbr for values in ('
single_quote = "'"
brace = ');'

iter_start = 901
iter_end = 1000
while iter_start < iter_end:
    main_string = create_tbl_str + str(iter_start) + create_tbl_str2 + single_quote + str(iter_start) + single_quote + brace
    iter_start = iter_start+1
    print(main_string)

 