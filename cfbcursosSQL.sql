/*
sum - soma
avg - media
count - contagem
round - arredondar
*/
select round(avg(f_valor_venda),2) from venda where f_valor_venda > (select min(f_valor_venda)  from venda) and f_valor_venda < (select max(f_valor_venda)  from venda);