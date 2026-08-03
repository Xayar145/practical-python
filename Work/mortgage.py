# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

#用户自定义输入
extra_payment_start_month = int(input("请输入额外支付费用起始月份:"))
extra_payment_end_month = int(input("请输入额外支付费用结束月份:"))
extra_payment = int(input("请输入额外支付费用:"))
month = 1
while principal >= 0:

    if(month>extra_payment_start_month and month <extra_payment_end_month):
        extra_payment =1000
    else:
        extra_payment =0
    principal = principal * (1+rate/12)+extra_payment-payment

    if(principal * (1+rate/12)+extra_payment<payment):
        principal = 0
    total_paid = total_paid + principal


    month+=1
    print(f'{month:>10d},{total_paid:10.2f},{principal:10.2f}')

print(total_paid)
