# -*- coding: cp936 -*-
'''
Author: Wangke
Date: 20140709
Task: Seek file that match corresponding conditions
Version:20140711

Conditions:
	1) error*_GetNoArea.txt | get the id of these files
	2) ratio_*.*.txt | the folder id which NOT contains the file
	3) ratio_4.0.txt | the folder id which contains the file
	4) asc[id].txt | the folder id which contains file that bigger than 100M
'''

import os, re

def find_error_id(root_path, error_info):
	'''
	function: find the error file id that correspond with the error type(error_info) 
	parameters: 
		root_path: the root directory path
		error_info: the type name of error which should be check
	return:
		thelist: id list of the corresponding error files
	'''
	pattern_txt = re.compile('^(error\d+_%s)(\.txt)$' % error_info, re.I)
	thelist=[]
	for s in os.listdir(root_path):
		if not re.match(pattern_txt, s): continue
		thelist.append(s)
	print thelist
	return thelist

def folder_id_not_ratio(root_path):
	'''
	function: find the fold id that not contains ratio_*.*.txt, the fold name must be a number
	parameters:
		root_path: the root directory path
	retrun:
		fold id list
	'''
	thelist=[]
	pattern_onlynumber = re.compile('^\d+$')
	pattern_ratio = re.compile('^(ratio_\d\.\d\.txt)')
	for s in os.listdir(root_path):
		if not re.match(pattern_onlynumber, s): continue
		isexsit = False
		for f in os.listdir(os.path.join(root_path,s)):
			if re.match(pattern_ratio, f): 
				isexsit=True
		if not isexsit: thelist.append(s)
	print thelist
	return thelist
	
def folder_id_ratio40(root_path):
	'''
	function: find the fold id that contains ration_4.0.txt, the fold name must be a number
	parameters:
		root_path: the root directory path
	return:
		fold id list 
	'''
	thelist = []
	pattern_onlynumber = re.compile('^\d+$')
	pattern_ratio40 = re.compile('^(ratio_4.0\.txt)')
	for s in os.listdir(root_path):
		if not re.match(pattern_onlynumber, s): continue
		for f in os.listdir(os.path.join(root_path,s)):
			if re.match(pattern_ratio40, f): thelist.append(s)
	print thelist
	return thelist
    
    
def folder_id_ascid_bigger100m(root_path):
	'''
	function: find fold id that contains asc[id].txt which size bigger than 100M, the fold name must be a number
	parameters:
		root_path: the root directory path
	return:
	 fold id list
	'''
	thelist=[]
	pattern_asc = re.compile('^(asc(\d+)\.txt)')
	pattern_onlynumber = re.compile('^\d+$')
	for s in os.listdir(root_path):
		if not re.match(pattern_onlynumber, s): continue
		for f in os.listdir(os.path.join(root_path,s)):
			if (re.match(pattern_asc, f) and os.path.getsize(os.path.join(os.path.join(root_path, s), f)) > 100*1024*1024):
				thelist.append(s)
	print thelist
	return thelist

#def fileseek(root_path):
#    getnoarea_id=[]
#    not_exsit_ratio_dirid=[]
#    exsit_ratio40_dirid=[]
#    ascbigger100m_dirid=[]
#    pattern1 = re.compile('^(error(\d+)_GetNoArea\.txt)')
#    pattern2 = re.compile('^(ratio_\d\.\d\.txt)')
#    pattern3 = re.compile('^(ratio_4.0\.txt)')
#    pattern4 = re.compile('^(asc(\d+)\.txt)')
#    pattern_onlynumber = re.compile('^\d+$')
#    for path, dirs, files in os.walk(root_path):
#        not_exist = True
#        dirname = os.path.basename(path)
#        isnumber = re.match(pattern_onlynumber, dirname) is not None
#        for f in files:
#            if re.match(pattern1, f): getnoarea_id.append(f[5:-14])
#            if not isnumber: continue
#            if re.match(pattern2, f): not_exist = False
#            if re.match(pattern3, f): exsit_ratio40_dirid.append(dirname)
#            if os.path.getsize(os.path.join(path, f)) > 100*1024*1024: ascbigger100m_dirid.append(dirname)    
#        if isnumber and not_exist: not_exsit_ratio_dirid.append(dirname)
#    print r'列出所有“GetNoArea”错误的id'
#    print getnoarea_id
#    print r'列出所有不存在“ratio_*.*.txt”文件的单独子目录id'
#    print not_exsit_ratio_dirid
#    print r'列出所有存在“ratio_4.0.txt”文件的单独子目录id'
#    print exsit_ratio40_dirid
#    print r'列出所有“asc[id].txt”文件大小大于100M的单独子目录id'
#    print ascbigger100m_dirid
#
#    return getnoarea_id, not_exsit_ratio_dirid, exsit_ratio40_dirid, ascbigger100m_dirid
   
   
if __name__ == '__main__':
    root_path = raw_input('Please enter the root path: ')
    #root_path = r'D:\file\edison'
    error_info = raw_input('Enter the error type: ')
    find_error_id(root_path, error_info)
    folder_id_not_ratio(root_path)
    folder_id_ratio40(root_path)
    folder_id_ascid_bigger100m(root_path)
    raw_input("<Please Press Enter To End>_")
