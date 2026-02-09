delimiter $$
create procedure loopLoop(in max int,out soma int)
begin
declare x int default 0;
	meuloop : loop
	if(x >=max) then
		leave meuloop;
	end if;
    set x = x + 1;
	end loop;
    set soma = x;
end $$
delimiter ;
call loopLoop(50,@ret);
select @ret;