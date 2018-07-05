import requests
import PyPDF2
import sys
import os
import re
import shelve


def get_regex(course):
	if course == 'BTECH.pdf':
		return re.compile(r'B\d+\w{2}\s.+\s-?\d+')
	elif course == 'PhD.pdf':
		return re.compile(r'P\d+\w{2}\s.+\s-?\d+')
	else:
		return re.compile(r'M\d+\w{2}\s.+\s-?\d+')


def main():
	URL = 'http://www.nitc.ac.in/app/webroot/img/upload/'
	COURSE = ['BTECH.pdf', 'PG.pdf', 'PhD.pdf']
	dues_list = shelve.open('dues')
	for course in COURSE:
		res = requests.get(URL+course)
		dues = open(course, 'wb')
		for chunk in res.iter_content(100000):
			dues.write(chunk)
		dues.close()

		pdf_file_obj = open(course, 'rb')
		pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
		total_pages = pdf_reader.numPages

		roll_rex = get_regex(course)
		for i in range(total_pages):
			page = pdf_reader.getPage(i)
			text = page.extractText()
			search_res = roll_rex.findall(text)

			for res in search_res:
				r = res.split('\n')
				dues_list[r[0]] = [r[1], r[2]]
	dues_list.close()


if __name__ == "__main__":
	main()
	sys.exit()
