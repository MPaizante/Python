/*
sum - soma
avg - media
count - contagem
round - arredondar
*/

select * from cliente c1, cliente c2 where c1.i_tipo_cliente = c2.i_tipo_cliente and c1.s_nome_cliente = 'Matheus P' order by c1.i_tipo_cliente;