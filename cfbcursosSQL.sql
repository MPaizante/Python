/*
sum - soma
avg - media
count - contagem
round - arredondar
*/
select * from venda where d_data_venda between '2020-07-01' and '2020-11-01' and i_cliente_cliente not in (3,10) and f_valor_venda > 20;