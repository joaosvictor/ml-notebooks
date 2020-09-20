from random import seed
import math
from random import randint

nm= -1
ncount= 1
hcount= -1
lcount= 1
rcount= -1


	
# time execution O(n log n)
searched=[]
def machine(number,number2):
	for i in range(99999999990):# generate numbers for the search;
		nm = randint(0,999990)
		print('halt:',nm,ncount)
		while ncount > nm and lcount >= nm:
			# jump to all current states possible
			Math.sqrt(5,nm)
			ans = 0 
			if nm==max(ncount):
				ans+=1
				print(ans)
		#process to find lost number
		for j in range(rcount):
			ans = nm.popleft()
			if ans not in searched:
				print('finish process' + hcount)
				dp=[[0,0],[0,0]]
				ans=dp[i][j]+rcount+nm
				nm.sort()
				for i in range(2):
					for j in range(2):
						for k in range(2):
							dp[i][k]=(dp[i][k]+number[i][j]*number2[j][k])%10
							print(dp[j])
		
		while hcount >  nm:
			#nm.sort()
			dp=[[0,0],[0,0]]
			for i in range(1):
				dp[i]=100
				for j in range(1):
					dp[i][j]=(dp[i][j]+dp[i][j])+10
					print(dp)
				
def main():
	machine(7,7)
main()	
