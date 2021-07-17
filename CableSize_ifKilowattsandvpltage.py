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
    if I>=25 and I<=39 :
        print("Approximate Cable Size is 4 mm Square Cu")
        print("-----------------------------------------------")
    elif  I>=39 and  I<=49 :
        print("Approximate Cable Size is 6 mm Square Cu")
        print("-----------------------------------------------")
    elif  I>=49 and  I<=65 :
        print("Approximate Cable Size is 10 mm Square Cu")
        print("-------------------------------------------------")
    elif  I>=65 and  I<=85 :
        print("Approximate Cable Size is 16 mm Square Cu")
        print("-------------------------------------------------")
    elif I>=85 and I<=110 :
        print("Approximate Cable Size is 25 mm Square Cu")
        print("------------------------------------------------ ")
    elif I>=110 and I<= 130:
        print("Approximate Cable Size is 35 mm Square Cu")
        print("-------------------------------------------------")
    elif I>=130 and I<=155:
        print("Approximate Cable Size is 50 mm Square Cu")
        print("-------------------------------------------------")
    elif I>=155 and I<=190:
        print("Approximate Cable Size is 70 mm Square Cu")
        print("-------------------------------------------------")
    elif I>=190 and I<=220:
        print("Approximate Cable Size is 95 mm Square Cu")
        print("-------------------------------------------------")
    elif I>=220 and I<=250:
        print("Approximate Cable Size is 120 mm Square Cu")
        print("--------------------------------------------------")
    elif I>=250 and I<=280:
        print("Approximate Cable Size is 150 mm Square Cu")
        print("--------------------------------------------------")
    elif I>=280 and I<=305:
        print("Approximate Cable Size is 185 mm Square Cu")
        print("--------------------------------------------------")
    elif I>=305 and I<=345:
        print("Approximate Cable Size is 240 mm Square Cu")
        print("--------------------------------------------------")
    elif I>=345 and I<=375:
        print("Approximate Cable Size is 300 mm Square Cu")
        print("--------------------------------------------------")
    elif I>=375 and I<=400:
        print("Approximate Cable Size is 400 mm Square Cu")
        print("--------------------------------------------------")
    elif I>=400 and I<=425:
        print("Approximate Cable Size is 500 mm Square Cu")
        print("--------------------------------------------------")
    elif I>=425 and I<=470:
        print("Approximate Cable Size is 630 mm Square Cu")
        print("--------------------------------------------------")
    else:
        print("Data Not Available")
        print("--------------------------------------------------")
    