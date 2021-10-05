vazn = float(input('vazn khod ra vared konid :'))
qad = float(input('qad khod ra vared konid :'))
if(vazn/(qad*qad) <= 18.5):
    print('you are UnderWeight ')
elif(18.5 < vazn/(qad*qad) <= 24.9):
    print('you are Normal ')
elif(25 < vazn/(qad*qad) <= 29.9):
    print('you are OverWeight ')
elif(30 < vazn/(qad*qad) <= 34.9):
    print('you are Obese ')
elif(vazn/(qad*qad) > 35):
    print('you are ExtranllyObese ')