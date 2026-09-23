items=["pencil", "eraser", "glue","pen","ruler"]
stock_count=[6,0,2,7,3]
inventory={i:sc for i,sc in zip(items,stock_count)}
print(inventory)
in_stock=[i1 for i1 in items if inventory[i1]>0]
print(in_stock)
out_stock=[i2 for i2 in items if inventory[i2]<=0]
print(out_stock)
exit()