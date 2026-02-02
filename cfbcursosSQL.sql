/*
sum - soma
avg - media
count - contagem
round - arredondar
*/

select c.i_cliente_cliente, c.s_nome_cliente, v.i_venda_venda from cliente c inner join venda v on c.i_cliente_cliente = v.i_cliente_cliente;