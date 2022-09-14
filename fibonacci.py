import logging
logging.basicConfig(level=logging.DEBUG)



fibb_num = [1, 2]
total = 0

while fibb_num[-1] < 4000000:
	# Adds the last two numbers in the list and appends it.
	fibb_num.append(fibb_num[-1] + fibb_num[-2])

# Removes the last digit as it exceeds 4 million.
del fibb_num[-1]

for num in fibb_num:
	if num % 2 == 0:
		total += num

# print(fibb_num)
# print(total)

logging.debug(fibb_num)
logging.debug(total)