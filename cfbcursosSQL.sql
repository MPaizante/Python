select count(v.i_venda_venda), v.d_data_venda as Vendas from venda v group by v.d_data_venda having count(v.i_venda_venda)>1;



