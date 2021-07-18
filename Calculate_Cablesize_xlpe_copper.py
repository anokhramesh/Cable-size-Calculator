#https://electricalnotes.wordpress.com/2011/04/24/xlpe-cable-current-rating/
print("\nProgram for Calculate the Cable size- if Line Voltage and Kilo Watts are known")
print("---------------------------------------------------------------------------------------------")
while True:
    pf = 0.8 # power factor
    eff = 0.94 # Efficiency in %(94%)
    V = float(input("Enter The Line Voltage\n"))# User input-Voltage 
    P = float(input("Enter the Total Kilo Watts \n"))# User input-Kilo watts 
    I = P/(1.732*V*pf*eff)*1000
#Load current = Power/(1.732 *Voltage * Power Factor * efficiency)*1000
    print('Calculated Current is = %0.3f'%(I),'Ampere')
    if I>=25 and I<=37 :
        print("Approximate Cable Size is 4 mm Square Cu/XLPE")
        print("-----------------------------------------------")
    elif  I>=37 and  I<=47 :
        print("Approximate Cable Size is 6 mm Square Cu/XLPE")
        print("-----------------------------------------------")
    elif  I>=47 and  I<=67 :
        print("Approximate Cable Size is 10 mm Square Cu/XLPE")
        print("-------------------------------------------------")
    elif  I>=67 and  I<=78 :
        print("Approximate Cable Size is 16 mm Square Cu/XLPE")
        print("-------------------------------------------------")
    elif I>=78 and I<=100 :
        print("Approximate Cable Size is 25 mm Square Cu/XLPE")
        print("------------------------------------------------ ")
    elif I>=100 and I<= 120:
        print("Approximate Cable Size is 35 mm Square Cu/XLPE")
        print("-------------------------------------------------")
    elif I>=120 and I<=145:
        print("Approximate Cable Size is 50 mm Square Cu/XLPE")
        print("-------------------------------------------------")
    elif I>=145 and I<=175:
        print("Approximate Cable Size is 70 mm Square Cu/XLPE")
        print("-------------------------------------------------")
    elif I>=175 and I<=210:
        print("Approximate Cable Size is 95 mm Square Cu/XLPE")
        print("-------------------------------------------------")
    elif I>=210 and I<=240:
        print("Approximate Cable Size is 120 mm Square Cu/XLPE")
        print("--------------------------------------------------")
    elif I>=240 and I<=270:
        print("Approximate Cable Size is 150 mm Square Cu/XLPE")
        print("--------------------------------------------------")
    elif I>=270 and I<=300:
        print("Approximate Cable Size is 185 mm Square Cu/XLPE")
        print("--------------------------------------------------")
    elif I>=300 and I<=350:
        print("Approximate Cable Size is 240 mm Square Cu/XLPE")
        print("--------------------------------------------------")
    elif I>=350 and I<=390:
        print("Approximate Cable Size is 300 mm Square Cu/XLPE")
        print("--------------------------------------------------")
    elif I>=390 and I<=440:
        print("Approximate Cable Size is 400 mm Square Cu/XLPE")
        print("--------------------------------------------------")
    elif I>=440 and I<=480:
        print("Approximate Cable Size is 500 mm Square Cu/XLPE")
        print("--------------------------------------------------")
    elif I>=480 and I<=575:
        print("Approximate Cable Size is 630 mm Square Cu/XLPE")
        print("--------------------------------------------------")
    else:
        print("Data Not Available")
        print("--------------------------------------------------")
    