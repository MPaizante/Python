delimiter $$
create procedure idade(in idCliente int, out idade int, out res varchar(20))
begin
	declare dt datetime;
    set dt = (select d_nasc_cliente from cliente where i_cliente_cliente = idCliente);
	set idade = year(now()) - year(dt);
	if(idade >=18) then
    set res= 'Maior';
    else
    set res = 'menor';
    end if;
end $$
delimiter ;
call idade(1,@idadecliente,@resultado);
select @idadecliente, @resultado;