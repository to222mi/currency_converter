import sys
from forex_python.converter import CurrencyRates
c = CurrencyRates()

def main():
	amount=input("amount:")
	a=float(amount)
	curr1=input("input_currency: ")
	curr2=input("output currency: ")


	if curr2:
		res = c.get_rates(curr1) 
		for i in res:
			res[i]=res[i]*a

		res_filt = {k: v for k, v in res.items() if k.startswith('{}'.format(curr2))}
		result = dict(input=dict(amount=a,
								 currency=curr1),
					 output=dict(res_filt))
	else:
		res = c.get_rates(curr1)  
		for i in res:
			res[i]=res[i]*a
		
		result = dict(input=dict(amount=a,
								 currency=curr1),
					 output=dict(res))

	print(result)
	
while True:
	main()
	if input("Repeat? (Y/N)")== 'N':
		break