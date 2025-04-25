import sys
sys.path.append("./modules/")
import testModule

exponentialIncludedLiteral=3.14e-12
print(exponentialIncludedLiteral+.12345+12.)
print(1.+.234)
print(1j**2)
print(not False)

print("-----------------")
print("test sentence 1")
print()
print("test sentence 2")
print("-----------------")
print("test sentence 1\n")
print("test sentence 2")
"""
2apple 숫자로 시작 불가
apple 2 공백 포함 불가
apple+ _이외의 기호 포함 불가
def 키워드라 사용 불가
"""
num=0
print(id(num))
print("org","psomipia","xspeed",sep=".")

print(testModule.rand(1,5))
print("이름: %s, 점수: %d" % ("Chansu", 90))
print('a' in 'apple')
print("abebsda".count("a"))
#✅ 문자열 메서드
#count(substr) → 특정 문자열의 개수

#find(substr) → 처음 나오는 위치 반환, 없으면 -1

#rfind(substr) → 뒤에서부터 검색

#replace(old, new) → 문자열 치환

#기타 메서드:

#upper(), lower(), strip(), split(), join() 등