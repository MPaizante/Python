/*
sum - soma
avg - media
count - contagem
round - arredondar
*/

select 'Cliente' as Tabela,i_cliente_cliente,s_nome_cliente from cliente union select 'Cliente_aux' as Tabela,i_cliente_cliente,s_nome_cliente from cliente_aux union 
select  'Venda', i_cliente_cliente, i_venda_venda from venda v inner join cliente c on v.i_cliente_cliente = c.i_cliente_cliente;
