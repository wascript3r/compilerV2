import useles
import sys

if len(sys.argv) != 2:
    print("Please specify the input script")
    exit(1)

result, err = useles.run('<stdin>', 'RUN("' + sys.argv[1] + '")')
if err:
    print(err.as_string())

# while True:
# 	text = input('useles > ')
# 	if text.strip() == "": continue
# 	result, error = useles.run('<stdin>', text)
#
# 	if error:
# 		print(error.as_string())
# 	elif result:
# 		if len(result.elements) == 1:
# 			print(repr(result.elements[0]))
# 		else:
# 			print(repr(result))
