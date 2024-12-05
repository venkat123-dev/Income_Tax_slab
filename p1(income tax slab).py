salary=int(input("Enter how much salary do you draw per year: "))
if salary<=300000:                                    
           print("No need to pay income tax")


elif 300000<=salary<=700000:                                               
           tax1=(salary-300000)*0.05
           print(tax1,"Tax you need to pay") 
elif 700000<salary<=1000000:                                               
           tax2=(400000*0.05)+(salary-700000)*0.10
           print(tax2,"Tax you need to pay")
elif 1000000<salary<=1200000:                                 
           tax3=(400000*0.05)+(300000*0.10)+(salary-1000000)*0.15
           print(tax3,"Tax you need to pay") 
elif 1200000<salary<=1500000:
           tax4=(400000*0.05)+(300000*0.10)+(200000*0.15)+(salary-1200000)*0.20
           print(tax4,"Tax you need to pay") 
else:
        salary>=1500000
        tax5=(400000*0.05)+(300000*0.10)+(200000*0.15)+(300000*0.20)+(salary-1500000)*0.30
        print(tax5,"Tax you need to pay")          