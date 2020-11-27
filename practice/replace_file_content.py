f = open('replace_file_content_test.text', 'r')
data = f.read().replace("java", "python")
f.close()

f = open('replace_file_content_test.text', 'w')
f.write(data)
f.close()
