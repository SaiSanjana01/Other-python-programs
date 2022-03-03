row1=['😇','😇','😇']
row2=['🧐','🧐','🧐']
row3=['😴','😴','😴']
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("where do you keep your treasure:  ")

#positions
horizontal= int(position[0])
vertical= int(position[1])

selected_row=map[vertical-1]
selected_row[horizontal-1]='X'

#method-2 
# row=int(input("row: "))
# col=int(input("Column: "))
# row_col=map[row-1][col-1] = 'Sanju'
# print(row_col)

print(f"{row1}\n{row2}\n{row3}")