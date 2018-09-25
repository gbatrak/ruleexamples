def rule(row, aux):
    row['POLICY'] in aux('ae', 'POLICY') and row['PAID'] < 20000.0
