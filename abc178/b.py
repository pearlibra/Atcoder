def get_ints():
	return list(map(int,input().split()))
	
a,b,c,d = get_ints()
ans = max(a*c, a*d, b*c, b*d)
print(ans)