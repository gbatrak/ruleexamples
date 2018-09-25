def rule(row, aux):
    row['POLICY'] in aux('ae', 'POLICY') and row['PAID'] > 10000.0
