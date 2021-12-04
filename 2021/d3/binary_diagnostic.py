from collections import Counter
# Power Consumption = PC
# PC = Gamma rate (GR) * epsilon rate (ER)
# GR = Most common bit in each corresponding position
# ER = Least common bit in each position 
# Output PC in decimal

def read_file():
    with open('input.txt') as f:
        report = f.read().splitlines()
        return report

def power_consumption():
    report = read_file()
    gamma, epsilon  = list('000000000000'), list('000000000000')
    num_ones = {i : int(bit) for i, bit in enumerate(gamma)} 
    for i in range(1, len(report)):
       # Keep track of max and min for each position 
       num = report[i]
       for j in range(0, len(num)):
           num_ones[j] += int(num[j])  
           num_zeros = (i + 1) - num_ones[j]
           gamma[j] = '1' if num_ones[j] > num_zeros else '0'
           epsilon[j] = '1' if num_ones[j] < num_zeros else '0'
    gr = "".join(map(str, gamma))
    er = "".join(map(str, epsilon))
    return int(gr, 2) * int(er, 2)

# Part 1
part1_output = power_consumption()
print("Part 1:", part1_output)

'''
- Only keep numbers selected by bit criteria

- If only one number left, this is the rating value

- Bit criteria depends on type of rating value

- Oxygen Generator Rating (OGR): most common value in current bit position
    - if 0 and 1 equally common, keep values w/ 1 in the current position

- CO2 Scrubber Rating (CSR): least common value in current bit position
    - if 0 and 1 equally common, keep values w/ 0 in the current position

- Convert OGR and CSR from binary to decimal

- Life Support Rating = OGR * CSR 
'''
def life_support():
    report = read_file()
    # OGR criteria = Oxygen Generator Rating
    ogr = report
    for i in range(len(ogr[0])):
        count = Counter([val[i] for val in ogr])
        if count['0'] > count['1']:
            ogr = [num for num in ogr if num[i] == '0'] 
        else:
            ogr = [num for num in ogr if num[i] == '1']

    # CSR criteria = CO2 Scrubber Rating
    csr = report
    for i in range(len(csr[0])):
        count = Counter([val[i] for val in csr])
        if count['0'] > count['1']:
            csr = [num for num in csr if num[i] == '1']
        else:
            csr = [num for num in csr if num[i] == '0']
        if len(csr) == 1:
            return int(ogr[0], 2) * int(csr[0], 2)

part2_output = life_support()
print("Part 2:", part2_output)
